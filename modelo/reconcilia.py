"""Reconcilia el balance energetico de la minuta (deficit 9 GWh) con el modelo."""
import numpy as np
from solar import generate
from model import load_profile
from market import cmg_profile
from dispatch_lp import solve
from final import cmg_for, SCEN

cmg = cmg_for(SCEN["base"])

def bal(gen_gwh, load_mw, flat, mwh, mw, label):
    pv = generate(76_500, config="tracker", dc_ac_ratio=1.30)["ac_mw"]
    pv = pv * (gen_gwh*1000/pv.sum())
    load = np.full(8760, load_mw) if flat else load_profile(load_mw)
    d = solve(pv, load, cmg, mwh, mw, inj_limit=0.0, grid_charge=False)
    print(f"{label:<52} gen {pv.sum()/1000:6.1f} | consumo {load.sum()/1000:6.1f} | "
          f"deficit {d['imp'].sum()/1000:5.1f} | vertido {d['curt'].sum()/1000:5.1f} | "
          f"autosuf {1-d['imp'].sum()/load.sum():5.1%}")

print("BALANCE ENERGETICO EN AUTOCONSUMO PURO (sin inyeccion), GWh/ano\n")
print("Supuestos de la simulacion previa de GR (minuta: deficit 9 GWh):")
bal(220, 19.0, True,  320, 20, "  220 GWh · consumo plano 19,0 MW · BESS 320/20")
bal(220, 20.0, True,  320, 20, "  220 GWh · consumo plano 20,0 MW · BESS 320/20")
bal(220, 19.0, True,  320, 70, "  220 GWh · plano 19,0 MW · BESS 320 MWh/70 MW (retiro 70 MW)")
print("\nCon el recurso que valida la DIA (170 GWh, estructura fija):")
bal(170, 19.0, True,  320, 20, "  170 GWh · consumo plano 19,0 MW · BESS 320/20")
bal(170, 19.0, False, 320, 20, "  170 GWh · consumo real variable · BESS 320/20")
print("\nCon seguidor de un eje (207 GWh, nuestro caso):")
bal(207, 19.0, True,  320, 20, "  207 GWh · consumo plano 19,0 MW · BESS 320/20")
bal(207, 19.0, False, 320, 20, "  207 GWh · consumo real variable · BESS 320/20")
bal(207, 19.0, False, 320, 30, "  207 GWh · consumo real variable · BESS 320 MWh/30 MW")
