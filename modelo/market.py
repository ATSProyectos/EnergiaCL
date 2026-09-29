"""
Senal horaria de costo marginal - barra Tarapaca / Nueva Victoria 110-220 kV.
Calibrada a: cmg medio 2025-26 en torno a 55-64 USD/MWh (CNE: Tarapaca 53,5 dic-25;
63,6 may-26), con la forma tipica del norte del SEN: horas solares deprimidas por
saturacion FV, rampa vespertina alta y noche intermedia.
"""
import numpy as np

def cmg_profile(annual_mean=60.0, seed=11):
    rng = np.random.default_rng(seed)
    h = np.arange(8760)
    hod = h % 24
    doy = h // 24 + 1

    # Forma horaria base (indice relativo antes de normalizar)
    shape = np.array([
        0.95, 0.90, 0.86, 0.84, 0.84, 0.88,   # 00-05 noche
        0.95, 0.80, 0.45, 0.22, 0.12, 0.08,   # 06-11 entrada solar
        0.07, 0.07, 0.08, 0.12, 0.28, 0.70,   # 12-17 valle solar
        1.85, 2.25, 2.05, 1.70, 1.35, 1.10,   # 18-23 rampa vespertina
    ])
    base = shape[hod]

    # Estacionalidad: invierno mas caro (menos sol, mas demanda de rampa)
    seas = 1 + 0.18*np.cos(2*np.pi*(doy - 182)/365.0)
    # Volatilidad: eventos de congestion / indisponibilidad
    noise = np.exp(rng.normal(0, 0.38, 8760))
    cmg = base * seas * noise
    # Piso de vertimiento: en el norte hay horas solares a precio ~0
    cmg = np.where((cmg < 0.10) , cmg*0.25, cmg)
    cmg *= annual_mean / cmg.mean()
    return np.clip(cmg, 0.0, 400.0)

if __name__ == "__main__":
    c = cmg_profile()
    hod = np.arange(8760) % 24
    print(f"cmg medio {c.mean():.1f} USD/MWh | mediana {np.median(c):.1f} | "
          f"p5 {np.percentile(c,5):.1f} | p95 {np.percentile(c,95):.1f}")
    print(f"horas bajo 10 USD/MWh: {(c<10).sum()} ({(c<10).mean():.1%})")
    print("\nPerfil medio por hora del dia:")
    for i in range(0, 24, 2):
        print(f"  {i:02d}h {c[hod==i].mean():6.1f}   {i+1:02d}h {c[hod==i+1].mean():6.1f}")
    print(f"\nMedia horas solares (09-17): {c[(hod>=9)&(hod<=17)].mean():.1f}")
    print(f"Media rampa vespertina (18-22): {c[(hod>=18)&(hod<=22)].mean():.1f}")
    print(f"Media noche (23-08): {c[(hod>=23)|(hod<=8)].mean():.1f}")
