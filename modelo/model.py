"""
Modelo de despacho horario y economia PPA - Proyecto SQM Nueva Victoria / Grenergy.
Todos los valores en USD reales de 2026.
"""
import numpy as np
from solar import generate

# ---------------------------------------------------------------- CONSUMO SQM
def load_profile(mw_avg=19.0, seed=7):
    """
    Perfil de consumo del Tap Off Nueva Victoria 110 kV.
    Calibrado contra los medidores 2026 (proceso continuo de lixiviacion / yoduro /
    recursos hidricos): forma diaria practicamente plana, variabilidad por campanas
    de planta, maximo horario observado 31,3 MW sobre media ~20 MW.
    """
    rng = np.random.default_rng(seed)
    # ruido autocorrelacionado (campanas de planta de varios dias)
    n = 8760
    w = rng.normal(0, 1, n)
    k = 72                                  # ventana ~3 dias
    kern = np.exp(-np.arange(k)/24.0)
    kern /= kern.sum()
    slow = np.convolve(w, kern, mode="same")
    slow = slow / slow.std()
    fast = rng.normal(0, 1, n)
    x = 0.82*slow + 0.18*fast
    load = mw_avg * (1 + 0.105 * x)          # sd ~10,5% -> rango 15-26 MW
    load = np.clip(load, 0.55*mw_avg, 1.65*mw_avg)
    load *= mw_avg / load.mean()             # renormaliza la media exacta
    return load


# ------------------------------------------------------------------- DESPACHO
def dispatch(pv_mw, load_mw, bess_mwh, bess_mw, rte=0.88, dod=0.94,
             inj_limit_mw=None, allow_injection=True, soc0=0.5):
    """
    Prioridad: (1) FV directo al consumo, (2) excedente carga BESS,
    (3) BESS descarga para cubrir deficit, (4) excedente remanente -> inyeccion o vertido,
    (5) deficit remanente -> suministro de Grenergy Power (retiro de red).
    """
    n = len(pv_mw)
    usable = bess_mwh * dod
    eta = np.sqrt(rte)
    soc = usable * soc0

    direct = np.minimum(pv_mw, load_mw)
    surplus = pv_mw - direct
    deficit = load_mw - direct

    charge = np.zeros(n); discharge = np.zeros(n)
    inject = np.zeros(n); curtail = np.zeros(n); grid = np.zeros(n)

    for t in range(n):
        # carga del BESS con excedente FV
        if surplus[t] > 0 and usable > 0:
            room = (usable - soc) / eta
            c = min(surplus[t], bess_mw, room)
            charge[t] = c
            soc += c * eta
            rest = surplus[t] - c
        else:
            rest = surplus[t]
        if rest > 0:
            if allow_injection:
                cap = inj_limit_mw if inj_limit_mw is not None else rest
                inject[t] = min(rest, cap)
                curtail[t] = rest - inject[t]
            else:
                curtail[t] = rest

        # descarga del BESS contra deficit
        if deficit[t] > 0 and usable > 0:
            d = min(deficit[t], bess_mw, soc * eta)
            discharge[t] = d
            soc -= d / eta
            grid[t] = deficit[t] - d
        else:
            grid[t] = deficit[t]

    served_local = direct + discharge
    return dict(direct=direct, charge=charge, discharge=discharge, inject=inject,
                curtail=curtail, grid=grid, served_local=served_local,
                cycles=discharge.sum()/max(usable, 1e-9))


# ------------------------------------------------------------------- ECONOMIA
class Costs:
    # CAPEX unitarios (USD) - calibrados contra la DIA de SQM: US$111 M declarados
    pv_fixed      = 620.0     # USD/kWp estructura fija
    pv_tracker    = 690.0     # USD/kWp seguidor 1 eje
    bess_power    = 95.0      # USD/kW  (PCS, MT, BOP de potencia)
    bess_energy   = 138.0     # USD/kWh (bloques DC, contenedores, obra civil)
    infra         = 9.5e6     # LT 66 kV 6,6 km + SE seccionadora + caminos + conexion
    dev_owner     = 0.08      # desarrollo + owner's cost + contingencia (% del subtotal)
    # OPEX
    opex_pv       = 11.5      # USD/kWp/ano
    opex_bess_fix = 4.0       # USD/kWh/ano O&M
    opex_bess_aug = 3.5       # USD/kWh/ano reserva de aumentacion (ciclado moderado)
    opex_common   = 0.35e6    # USD/ano (LT/SE, terrenos, admin, SEC/CEN)
    insurance     = 0.0045    # % del CAPEX/ano
    # Financieros
    wacc          = 0.070     # real, despues de impuestos
    life          = 25        # anos de vida economica
    tax           = 0.27
    depr_years    = 10
    degr_pv       = 0.0045    # /ano


def capex(pv_kwp, bess_mwh, bess_mw, tracker=True, c=Costs):
    pv = pv_kwp * (c.pv_tracker if tracker else c.pv_fixed)
    bess = bess_mw*1000*c.bess_power + bess_mwh*1000*c.bess_energy
    sub = pv + bess + c.infra
    return dict(pv=pv, bess=bess, infra=c.infra, total=sub*(1+c.dev_owner))


def opex(pv_kwp, bess_mwh, capex_total, cycles=250, c=Costs):
    aug = c.opex_bess_aug * max(0.6, min(1.8, cycles/250.0))
    return (pv_kwp*c.opex_pv + bess_mwh*1000*(c.opex_bess_fix + aug)
            + c.opex_common + capex_total*c.insurance)


def crf(rate, n):
    return rate / (1 - (1+rate)**-n)


def tax_factor(c=Costs):
    """Gross-up por impuestos neto del escudo de depreciacion lineal."""
    pv_depr = sum(1/(1+c.wacc)**t for t in range(1, c.depr_years+1)) / c.depr_years
    return (1 - c.tax*pv_depr) / (1 - c.tax)


def levelized(capex_total, opex_annual, energy_mwh_y0, c=Costs):
    """LCOE real despues de impuestos, con degradacion FV."""
    d = sum((1-c.degr_pv)**t / (1+c.wacc)**t for t in range(1, c.life+1))
    e_lev = energy_mwh_y0 * d * crf(c.wacc, c.life)
    cost = capex_total * crf(c.wacc, c.life) * tax_factor(c) + opex_annual
    return cost / e_lev
