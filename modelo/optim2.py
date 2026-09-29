import numpy as np
from evaluate import evaluate, E_LOAD, cmg, load, TOLLS

print("="*104)
print("BARRIDO A - Duracion del BESS (FV 76,5 MWp seguidor, 20 MW de potencia BESS, POI 40 MW)")
print("="*104)
print(f"{'MWh':>6} {'h':>4} {'CAPEX':>7} {'Autosuf':>8} {'Ciclos':>7} {'Import':>8} {'Export':>8} "
      f"{'Vert':>6} {'LCOE':>7} {'CtS':>7} {'Delta':>7}")
base = None
rows_a = []
for mwh in [0, 40, 80, 120, 160, 200, 240, 280, 320, 400]:
    r = evaluate(76.5, mwh, 20 if mwh else 0, inj_limit=40)
    if base is None: base = r["cts"]
    h = mwh/20 if mwh else 0
    rows_a.append(r)
    print(f"{mwh:>6} {h:>4.0f} {r['capex']:>7.1f} {r['autosuf']:>7.1%} {r['cycles']:>7.0f} "
          f"{r['e_imp']:>8.1f} {r['e_exp']:>8.1f} {r['e_curt']:>6.1f} {r['lcoe']:>7.1f} "
          f"{r['cts']:>7.1f} {r['cts']-base:>+7.1f}")

print()
print("="*104)
print("BARRIDO B - Potencia del BESS (energia fija 120 MWh, FV 76,5 MWp, POI 40 MW)")
print("="*104)
print(f"{'MW':>5} {'h':>5} {'CAPEX':>7} {'Autosuf':>8} {'Ciclos':>7} {'Import':>8} {'Export':>8} {'CtS':>7}")
for mw in [10, 15, 20, 25, 30, 40]:
    r = evaluate(76.5, 120, mw, inj_limit=40)
    print(f"{mw:>5} {120/mw:>5.1f} {r['capex']:>7.1f} {r['autosuf']:>7.1%} {r['cycles']:>7.0f} "
          f"{r['e_imp']:>8.1f} {r['e_exp']:>8.1f} {r['cts']:>7.1f}")

print()
print("="*104)
print("BARRIDO C - Superficie FV x BESS: costo de servir el bloque 24/7 (USD/MWh), POI 40 MW")
print("="*104)
pvs = [76.5, 90, 105, 120, 140, 160]
bs  = [(0,0),(40,20),(80,20),(120,20),(160,20),(200,25),(240,30),(320,20)]
print("  FV MWp |" + "".join(f"{(f'{m}MWh' if m else 'sin BESS'):>10}" for m,_ in bs))
best = None; grid = {}
for mwp in pvs:
    row = f"{mwp:>8.1f} |"
    for mwh, mw in bs:
        r = evaluate(mwp, mwh, mw, inj_limit=40)
        grid[(mwp,mwh)] = r
        row += f"{r['cts']:>10.1f}"
        if best is None or r["cts"] < best["cts"]: best = r
    print(row)

print(f"\n>>> OPTIMO: FV {best['pv']:.1f} MWp + BESS {best['bess_mwh']:.0f} MWh / {best['bess_mw']:.0f} MW"
      f"  ->  {best['cts']:.1f} USD/MWh")
print(f"    CAPEX US$ {best['capex']:.1f} M | autosuficiencia {best['autosuf']:.1%} | "
      f"{best['cycles']:.0f} ciclos/ano | generacion {best['gen']:.0f} GWh")
