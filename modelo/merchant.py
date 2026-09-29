"""Valor del activo Nueva Victoria como planta merchant/cartera, sin PPA con SQM."""
import numpy as np
from solar import generate
from model import capex, opex, Costs, crf, tax_factor
from final import cmg_for, SCEN
from dispatch_lp import solve

TOLLS=18.0; H_PUNTA=4.0; FR_PV=0.10

def merchant(pv_mwp, mwh, mw, scen="base", inj_limit=40.0):
    sc=SCEN[scen]; cmg=cmg_for(sc)
    pv = generate(pv_mwp*1000, config="tracker", dc_ac_ratio=1.30)["ac_mw"]
    cero = np.zeros(8760)                      # sin consumo local: 100% al sistema
    d = solve(pv, cero, cmg, mwh, mw, tolls=TOLLS, inj_limit=inj_limit, grid_charge=True)
    cx = capex(pv_mwp*1000, mwh, mw, tracker=True)
    ox = opex(pv_mwp*1000, mwh, cx["total"], cycles=d["cycles"])
    ing = (cmg*d["exp"]).sum() - ((cmg+TOLLS)*d["imp"]).sum()
    ing *= sc["cap"]
    firm = min(mw, mwh*0.94/H_PUNTA, inj_limit) if mwh else 0.0
    ing += (firm + pv.max()*FR_PV)*1000*sc["pn"]*12 + min(mw,30.)*1000*sc["sscc"]
    ebitda = ing - ox
    van = ebitda/crf(Costs.wacc, Costs.life) - cx["total"]
    return dict(capex=cx["total"]/1e6, ebitda=ebitda/1e6, van=van/1e6,
                exp=d["exp"].sum()/1000, imp=d["imp"].sum()/1000, cycles=d["cycles"],
                yield_pct=ebitda/cx["total"])

print("="*96)
print("EL ACTIVO COMO PLANTA MERCHANT / DE CARTERA (sin PPA con SQM, 100% al sistema)")
print("="*96)
print(f"{'Configuración':<34}{'CAPEX':>9}{'EBITDA':>9}{'yield':>8}{'VAN 25a':>10}{'export':>9}{'ciclos':>8}")
for lbl,p,e,w in [("76,5 MWp sin BESS",76.5,0,0),
                  ("76,5 MWp + 150 MWh/30 MW",76.5,150,30),
                  ("76,5 MWp + 320 MWh/20 MW",76.5,320,20),
                  ("76,5 MWp + 320 MWh/30 MW",76.5,320,30)]:
    for sc in ["base"]:
        r=merchant(p,e,w,scen=sc)
        print(f"{lbl:<34}{r['capex']:>9.1f}{r['ebitda']:>9.2f}{r['yield_pct']:>8.1%}"
              f"{r['van']:>10.1f}{r['exp']:>9.1f}{r['cycles']:>8.0f}")
print("\nPor escenario, configuración 150 MWh/30 MW:")
for sc in ("conservador","base","optimista"):
    r=merchant(76.5,150,30,scen=sc)
    print(f"  {sc:<13} EBITDA US$ {r['ebitda']:5.2f} M/a | yield {r['yield_pct']:5.1%} | VAN US$ {r['van']:6.1f} M")
