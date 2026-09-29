from final import evaluate
print("SENSIBILIDAD A LA CAPACIDAD DEL PUNTO DE INYECCION (POI)")
print("Configuracion recomendada A2: FV 76,5 MWp seguidor + BESS 150 MWh / 30 MW\n")
print(f"{'POI MW':>8}{'conserv':>10}{'base':>9}{'optim':>9}{'export GWh':>12}{'vertido':>9}{'autosuf':>9}")
for poi in (0, 10, 17, 25, 30, 40, 55):
    row=f"{poi:>8}"
    for sc in ("conservador","base","optimista"):
        r=evaluate(76.5,150,30,scen=sc,inj_limit=poi,coordinated=(poi>0))
        row+=f"{r['cts']:>10.1f}" if sc=="conservador" else f"{r['cts']:>9.1f}"
        if sc=="base": b=r
    print(row+f"{b['e_exp']:>12.1f}{b['e_curt']:>9.1f}{b['autosuf']:>9.1%}")
print("\nIdem para A1 (BESS 320 MWh / 20 MW):")
print(f"{'POI MW':>8}{'conserv':>10}{'base':>9}{'optim':>9}{'export GWh':>12}{'vertido':>9}{'autosuf':>9}")
for poi in (0, 10, 17, 25, 40):
    row=f"{poi:>8}"
    for sc in ("conservador","base","optimista"):
        r=evaluate(76.5,320,20,scen=sc,inj_limit=poi,coordinated=(poi>0))
        row+=f"{r['cts']:>10.1f}" if sc=="conservador" else f"{r['cts']:>9.1f}"
        if sc=="base": b=r
    print(row+f"{b['e_exp']:>12.1f}{b['e_curt']:>9.1f}{b['autosuf']:>9.1%}")
