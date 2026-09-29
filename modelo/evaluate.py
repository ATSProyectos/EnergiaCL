"""Evaluacion economica integrada de las configuraciones FV+BESS para el PPA SQM."""
import numpy as np
from solar import generate
from model import load_profile, capex, opex, levelized, Costs, crf, tax_factor
from market import cmg_profile
from dispatch_lp import solve

# --- Parametros de mercado --------------------------------------------------
TOLLS        = 18.0    # peajes tx + cargo servicio publico + perdidas, USD/MWh
CMG_MEAN     = 60.0    # cmg medio barra Tarapaca, USD/MWh
PN_USD_KW_MO = 8.5     # precio de potencia de suficiencia, USD/kW-mes
H_PUNTA      = 4.0     # duracion del bloque de demanda maxima del SEN, horas
FR_PV        = 0.10    # reconocimiento de potencia firme del FV en el norte (punta vespertina)
SSCC_USD_KW_Y= 20.0    # ingreso por servicios complementarios del BESS, USD/kW-ano
SSCC_MW_CAP  = 30.0    # tope de potencia que coloca SSCC de forma sostenible

LOAD_MW = 19.0
load = load_profile(LOAD_MW)
cmg  = cmg_profile(CMG_MEAN)
E_LOAD = load.sum()

_pv = {}
def pv_series(mwp, tracker=True, dcac=1.30):
    k = (round(mwp,2), tracker, dcac)
    if k not in _pv:
        _pv[k] = generate(mwp*1000, config="tracker" if tracker else "fixed",
                          dc_ac_ratio=dcac)["ac_mw"]
    return _pv[k]

def evaluate(pv_mwp, bess_mwh, bess_mw, tracker=True, dcac=1.30,
             inj_limit=40.0, coordinated=True, grid_charge=True, label=""):
    pv = pv_series(pv_mwp, tracker, dcac)
    d  = solve(pv, load, cmg, bess_mwh, bess_mw, tolls=TOLLS,
               inj_limit=inj_limit if coordinated else 0.0,
               grid_charge=grid_charge and coordinated)
    cx = capex(pv_mwp*1000, bess_mwh, bess_mw, tracker=tracker)
    ox = opex(pv_mwp*1000, bess_mwh, cx["total"], cycles=d["cycles"])

    e_imp = d["imp"].sum(); e_exp = d["exp"].sum()
    e_local = d["served_local"].sum(); e_curt = d["curt"].sum()
    c_imp = ((cmg + TOLLS)*d["imp"]).sum()
    r_exp = (cmg*d["exp"]).sum()

    # Ingresos de capacidad y SSCC (solo si el sistema esta coordinado con el CEN).
    # Potencia de suficiencia del BESS: limitada por (i) su potencia nominal,
    # (ii) la energia que sostiene durante el bloque de punta y (iii) el alivio
    # maximo que el sistema puede ver = consumo local + capacidad de inyeccion.
    ac_mw = pv.max()
    firm_bess = min(bess_mw, bess_mwh*0.94/H_PUNTA, load.mean() + inj_limit) if bess_mwh else 0.0
    firm_pv = ac_mw*FR_PV
    r_pot = (firm_bess + firm_pv)*1000*PN_USD_KW_MO*12 if coordinated else 0.0
    r_sscc = (min(bess_mw, SSCC_MW_CAP)*1000*SSCC_USD_KW_Y
              if (coordinated and bess_mwh > 0) else 0.0)

    annual_capital = cx["total"]*crf(Costs.wacc, Costs.life)*tax_factor()
    cost_total = annual_capital + ox + c_imp - r_exp - r_pot - r_sscc
    cts = cost_total / E_LOAD

    lcoe_asset = levelized(cx["total"], ox, e_local + e_exp)
    return dict(label=label, pv=pv_mwp, bess_mwh=bess_mwh, bess_mw=bess_mw,
                gen=pv.sum()/1000, capex=cx["total"]/1e6, opex=ox/1e6,
                cap_pv=cx["pv"]/1e6, cap_bess=cx["bess"]/1e6,
                e_local=e_local/1000, e_imp=e_imp/1000, e_exp=e_exp/1000,
                e_curt=e_curt/1000, autosuf=e_local/E_LOAD, cycles=d["cycles"],
                c_imp=c_imp/1e6, r_exp=r_exp/1e6, r_pot=r_pot/1e6, r_sscc=r_sscc/1e6,
                capital=annual_capital/1e6, cts=cts, lcoe=lcoe_asset,
                firm_bess=firm_bess, firm_pv=firm_pv,
                p_imp=(cmg*d["imp"]).sum()/max(e_imp,1e-9),
                p_exp=r_exp/max(e_exp,1e-9), d=d)

def show(r):
    print(f"--- {r['label']}")
    dur = r['bess_mwh']/r['bess_mw'] if r['bess_mw'] else 0
    print(f"    FV {r['pv']:.1f} MWp ({r['gen']:.0f} GWh) | BESS {r['bess_mwh']:.0f} MWh / "
          f"{r['bess_mw']:.0f} MW ({dur:.0f} h) | CAPEX US$ {r['capex']:.1f} M")
    print(f"    Autosuficiencia {r['autosuf']:.1%} | importa {r['e_imp']:.1f} GWh @ {r['p_imp']:.0f} "
          f"| exporta {r['e_exp']:.1f} GWh @ {r['p_exp']:.0f} | vertido {r['e_curt']:.1f} GWh "
          f"| {r['cycles']:.0f} ciclos/a")
    print(f"    Costos US$M/a: capital {r['capital']:.2f} + opex {r['opex']:.2f} + compras {r['c_imp']:.2f}"
          f"  |  Ingresos: export {r['r_exp']:.2f} + potencia {r['r_pot']:.2f} + SSCC {r['r_sscc']:.2f}")
    print(f"    >> COSTO DE SERVIR: {r['cts']:.1f} USD/MWh   (LCOE del activo {r['lcoe']:.1f})\n")

if __name__ == "__main__":
    print(f"Consumo SQM: {E_LOAD/1000:.1f} GWh/ano | cmg medio {cmg.mean():.1f} USD/MWh")
    print(f"Referencia: comprar todo de la red al spot = {((cmg+TOLLS)*load).sum()/E_LOAD:.1f} USD/MWh\n")
    print("="*100)
    print("CASO 0 - Diseno SQM tal cual: 76,5 MWp fija + 320 MWh/20 MW, autoconsumo puro sin inyeccion")
    print("="*100)
    show(evaluate(76.5, 320, 20, tracker=False, dcac=1.20, coordinated=False,
                  label="Caso 0 - diseno SQM, off-grid"))
    print("="*100)
    print("ALTERNATIVA 1 - Producto 24/7, BESS de 16 h, deficit desde Grenergy Power")
    print("="*100)
    show(evaluate(76.5, 320, 20, tracker=False, dcac=1.20, coordinated=True, inj_limit=17,
                  label="A1.a - hardware SQM (fija) coordinado, POI 17 MW"))
    show(evaluate(76.5, 320, 20, tracker=True, dcac=1.30, coordinated=True, inj_limit=17,
                  label="A1.b - repotenciado a seguidor 1 eje, POI 17 MW"))
    show(evaluate(76.5, 320, 20, tracker=True, dcac=1.30, coordinated=True, inj_limit=40,
                  label="A1.c - seguidor + POI ampliado a 40 MW"))
