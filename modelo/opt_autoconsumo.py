"""Optimo del BESS bajo AUTOCONSUMO PURO (sin derecho de inyeccion).
La figura de 'cliente con autoconsumo' del DS 32 excluye inyectar excedentes,
de modo que el dimensionamiento optimo NO es el mismo que en SGC."""
from escenarios import run

print("="*100)
print("OPTIMO DEL BESS SIN DERECHO DE INYECCION  (figura de autoconsumo, FV 76,5 MWp seguidor)")
print("="*100)
print(f"{'MWh':>6}{'MW':>5}{'h':>5}{'CAPEX':>8}{'Autosuf':>9}{'Vertido':>9}"
      f"{'conserv':>10}{'base':>8}{'optim':>8}")
best={}
for mwh,mw in [(0,0),(80,20),(120,30),(160,30),(200,30),(240,30),(280,30),(320,30),
               (320,20),(400,30),(480,40)]:
    row=f"{mwh:>6}{mw:>5}{(mwh/mw if mw else 0):>5.0f}"
    vals={}
    for sc in ("conservador","base","optimista"):
        r=run(76.5,mwh,mw,scen=sc,coordinated=False,inj_limit=0,tolls_on_local=False)
        vals[sc]=r["cts"]
        if sc=="base": b=r
    row+=f"{b['capex']:>8.1f}{b['autosuf']:>9.1%}{b['e_curt']:>9.1f}"
    row+=f"{vals['conservador']:>10.1f}{vals['base']:>8.1f}{vals['optimista']:>8.1f}"
    print(row)
    for sc,v in vals.items():
        if sc not in best or v<best[sc][0]: best[sc]=(v,mwh,mw)
print()
for sc,(v,mwh,mw) in best.items():
    print(f"  optimo {sc:<13} {mwh} MWh / {mw} MW ({mwh/mw if mw else 0:.0f} h) -> {v:.1f} USD/MWh")
