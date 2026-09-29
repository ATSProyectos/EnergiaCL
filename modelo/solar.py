"""
Modelo horario de generacion FV - Nueva Victoria / Pozo Almonte, Region de Tarapaca.
Sitio: lat -20.70, lon -69.78, ~1.000 msnm. Zona horaria UTC-4.

El desierto de Atacama tiene irradiancia casi permanentemente de cielo claro, por lo que
un modelo de cielo claro (ASHRAE/Bird simplificado) con factor de disponibilidad-suciedad
reproduce bien la forma horaria. El total anual se CALIBRA contra dos referencias conocidas:
  - 170 GWh/ano para 76,5 MWp  (DIA SQM, estructura fija)  -> 2.222 kWh/kWp
  - 220 GWh/ano para 76,5 MWp  (simulacion Grenergy)       -> 2.876 kWh/kWp (seguidor 1 eje)
"""
import numpy as np

LAT = -20.70
LON = -69.78
TZ = -4.0          # hora oficial de Chile continental (sin DST, criterio conservador)
ALBEDO = 0.28      # desierto/salar
NOCT = 45.0
GAMMA_P = -0.0034  # coef. de temperatura de potencia, %/C

def _solar_vectors(n_hours=8760, year=2027):
    """Devuelve (u_E, u_N, u_U) del vector solar en coordenadas ENU, por hora."""
    h = np.arange(n_hours)
    doy = h // 24 + 1
    hour_local = h % 24 + 0.5                      # centro de hora

    # Ecuacion del tiempo (Spencer)
    B = 2 * np.pi * (doy - 1) / 365.0
    eot = 229.18 * (0.000075 + 0.001868*np.cos(B) - 0.032077*np.sin(B)
                    - 0.014615*np.cos(2*B) - 0.040849*np.sin(2*B))   # minutos
    # Hora solar verdadera
    t_solar = hour_local + (4.0 * (LON - 15.0 * TZ) + eot) / 60.0
    omega = np.deg2rad(15.0 * (t_solar - 12.0))    # angulo horario (<0 manana)

    decl = np.deg2rad(23.45) * np.sin(2*np.pi*(284 + doy)/365.0)
    phi = np.deg2rad(LAT)

    u_E = -np.cos(decl) * np.sin(omega)
    u_N = np.sin(decl)*np.cos(phi) - np.cos(decl)*np.sin(phi)*np.cos(omega)
    u_U = np.sin(phi)*np.sin(decl) + np.cos(phi)*np.cos(decl)*np.cos(omega)
    return u_E, u_N, u_U, doy, hour_local


def _clear_sky(u_U):
    """DNI y DHI de cielo claro (ASHRAE alta altitud, aire muy limpio)."""
    A, Bcoef, C = 1180.0, 0.14, 0.085
    sin_alpha = np.clip(u_U, 1e-6, None)
    dni = np.where(u_U > 0.02, A * np.exp(-Bcoef / sin_alpha), 0.0)
    dhi = np.where(u_U > 0.02, C * A * sin_alpha**0.5, 0.0)   # difusa horizontal
    ghi = dni * np.clip(u_U, 0, None) + dhi
    return dni, dhi, ghi


def _ambient_temp(doy, hour_local):
    """Temperatura ambiente sintetica del Tamarugal: media anual ~17 C, amplitud diaria alta."""
    t_mean = 17.0 + 4.5 * np.cos(2*np.pi*(doy - 15)/365.0)      # verano (ene) mas calido
    t_daily = 8.0 * np.sin(2*np.pi*(hour_local - 9.0)/24.0)
    return t_mean + t_daily


def generate(kwp, config="tracker", dc_ac_ratio=1.30, target_yield=None,
             soiling_avail=0.965, other_losses=0.115, max_tilt=55.0, gcr=0.33):
    """
    config: 'fixed' (estructura fija, 20 grados norte) o 'tracker' (1 eje N-S con backtracking)
    target_yield: kWh/kWp/ano objetivo para calibrar (si None, no calibra)
    Devuelve dict con serie horaria de potencia AC [MW] y metricas.
    """
    u_E, u_N, u_U, doy, hour_local = _solar_vectors()
    dni, dhi, ghi = _clear_sky(u_U)

    if config == "fixed":
        beta = np.deg2rad(20.0)
        n = np.array([0.0, np.sin(beta), np.cos(beta)])
        cos_inc = np.clip(u_E*n[0] + u_N*n[1] + u_U*n[2], 0, None)
        tilt = beta * np.ones_like(u_U)
    else:
        # seguidor de 1 eje horizontal N-S, rotacion E-O, con backtracking
        R_ideal = np.arctan2(u_E, np.clip(u_U, 1e-6, None))
        R = np.clip(R_ideal, -np.deg2rad(max_tilt), np.deg2rad(max_tilt))
        # backtracking: evita sombreado entre filas
        with np.errstate(invalid="ignore"):
            cos_arg = np.clip(np.cos(R_ideal) / gcr, -1, 1)
            R_bt = R_ideal - np.sign(R_ideal) * np.arccos(cos_arg)
        need_bt = np.abs(np.cos(R_ideal)) < gcr
        R = np.where(need_bt & (u_U > 0.02), R_bt, R)
        cos_inc = np.clip(u_E*np.sin(R) + u_U*np.cos(R), 0, None)
        tilt = np.abs(R)

    poa = (dni * cos_inc
           + dhi * (1 + np.cos(tilt)) / 2.0
           + ghi * ALBEDO * (1 - np.cos(tilt)) / 2.0)
    poa = np.where(u_U > 0.02, poa, 0.0)

    t_amb = _ambient_temp(doy, hour_local)
    t_cell = t_amb + poa / 800.0 * (NOCT - 20.0)
    temp_derate = 1 + GAMMA_P * (t_cell - 25.0)

    dc_mw = kwp/1000.0 * poa/1000.0 * temp_derate * (1 - other_losses) * soiling_avail

    if target_yield is not None:
        scale = target_yield / (dc_mw.sum() * 1000.0 / kwp)
        dc_mw *= scale

    ac_cap = kwp/1000.0 / dc_ac_ratio
    ac_mw = np.minimum(dc_mw, ac_cap)

    return {
        "ac_mw": ac_mw, "dc_mw": dc_mw, "ac_cap_mw": ac_cap,
        "ghi_kwh_m2": ghi.sum()/1000.0, "poa_kwh_m2": poa.sum()/1000.0,
        "gwh": ac_mw.sum()/1000.0, "yield": ac_mw.sum()*1000.0/kwp,
        "clip_gwh": (dc_mw - ac_mw).sum()/1000.0,
        "cf": ac_mw.sum()/(ac_cap*8760),
    }

if __name__ == "__main__":
    for cfg, dcac in [("fixed", 1.20), ("tracker", 1.30)]:
        r = generate(76_500, config=cfg, dc_ac_ratio=dcac)
        print(f"{cfg:8s} DC/AC={dcac}  GHI={r['ghi_kwh_m2']:.0f} kWh/m2  "
              f"POA={r['poa_kwh_m2']:.0f}  gen={r['gwh']:.1f} GWh  "
              f"yield={r['yield']:.0f} kWh/kWp  clip={r['clip_gwh']:.1f} GWh  FC={r['cf']:.1%}")
