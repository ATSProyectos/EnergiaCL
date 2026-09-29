import json, numpy as np
from final import evaluate, load, cmg_raw, SCEN, cmg_for, E_LOAD
from solar import generate
from dispatch_lp import solve

# ---- 1) Curva de optimizacion: costo de servir vs duracion del BESS -----------
print("CURVA DE OPTIMIZACION (FV 76,5 MWp seguidor, BESS 30 MW, POI 40 MW)")
print(f"{'h':>4}{'MWh':>7}{'conserv':>10}{'base':>9}{'optim':>9}{'ciclos':>8}{'autosuf':>9}")
curve=[]
for h in [0,1,2,3,4,5,6,8,10,12,14,16]:
    mwh = 30*h
    row={"h":h,"mwh":mwh}
    for sc in ("conservador","base","optimista"):
        r=evaluate(76.5, mwh, 30 if mwh else 0, scen=sc, inj_limit=40)
        row[sc]=round(r["cts"],1)
        if sc=="base": row["cycles"]=round(r["cycles"]); row["autosuf"]=round(r["autosuf"],3)
    curve.append(row)
    print(f"{h:>4}{mwh:>7}{row['conservador']:>10.1f}{row['base']:>9.1f}"
          f"{row['optimista']:>9.1f}{row['cycles']:>8}{row['autosuf']:>9.1%}")

# ---- 2) Costo marginal de cada bloque adicional de almacenamiento ------------
print("\nCOSTO MARGINAL DE CADA HORA ADICIONAL DE ALMACENAMIENTO (escenario base)")
prev=None
for row in curve:
    if prev is not None:
        d=(row["base"]-prev["base"])
        print(f"  hora {prev['h']}->{row['h']}: {d:+6.1f} USD/MWh sobre el bloque total "
              f"({(d*E_LOAD/1000):+7.0f} kUSD/ano)")
    prev=row

# ---- 3) Perfiles diarios de despacho (A1 vs A2), dia tipo de verano e invierno
cmg = cmg_for(SCEN["base"])
pv = generate(76_500, config="tracker", dc_ac_ratio=1.30)["ac_mw"]
profiles={}
for name,(mwh,mw,inj) in {"A1":(320,20,25), "A2":(150,30,40)}.items():
    d = solve(pv, load, cmg, mwh, mw, inj_limit=inj, grid_charge=True)
    for season,d0 in (("verano", 15), ("invierno", 180)):
        s=d0*24
        profiles[f"{name}_{season}"]={
            "pv":[round(x,2) for x in pv[s:s+24]],
            "load":[round(x,2) for x in load[s:s+24]],
            "ch":[round(x,2) for x in d["ch"][s:s+24]],
            "dis":[round(x,2) for x in d["dis"][s:s+24]],
            "imp":[round(x,2) for x in d["imp"][s:s+24]],
            "exp":[round(x,2) for x in d["exp"][s:s+24]],
            "cmg":[round(x,1) for x in cmg[s:s+24]],
        }

# ---- 4) Perfil medio horario de cmg y de generacion --------------------------
hod=np.arange(8760)%24
cmg_h=[round(float(cmg[hod==i].mean()),1) for i in range(24)]
pv_h=[round(float(pv[hod==i].mean()),2) for i in range(24)]
load_h=[round(float(load[hod==i].mean()),2) for i in range(24)]

json.dump({"curve":curve,"profiles":profiles,"cmg_h":cmg_h,"pv_h":pv_h,"load_h":load_h},
          open("charts.json","w"), indent=1)
print("\ncharts.json escrito")
print("\nPerfil medio horario  (h: cmg USD/MWh | FV MW | consumo MW)")
for i in range(24):
    print(f"  {i:02d}  {cmg_h[i]:7.1f}  {pv_h[i]:6.1f}  {load_h[i]:6.1f}")
