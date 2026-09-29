"""Descomposicion del valor de coordinar, sobre configuracion IDENTICA (150 MWh/30 MW)."""
import numpy as np
from escenarios import run, pv_series, load, E_LOAD, TOLLS, H_PUNTA, FR_PV
from final import cmg_for, SCEN
from dispatch_lp import solve
from model import capex, opex, Costs, crf, tax_factor

sc = SCEN["base"]; cmg = cmg_for(sc)
pv = pv_series(76.5)
cx = capex(76.5*1000, 150, 30, tracker=True)

def caso(inj, coord, peaje_local):
    d = solve(pv, load, cmg, 150, 30, tolls=TOLLS, inj_limit=inj, grid_charge=coord)
    ox = opex(76.5*1000, 150, cx["total"], cycles=d["cycles"])
    c_imp=((cmg+TOLLS)*d["imp"]).sum(); r_exp=(cmg*d["exp"]).sum()
    e_local=d["served_local"].sum()
    mg = r_exp-c_imp; mg = mg*sc["cap"] if mg>0 else mg/sc["cap"]
    firm = min(30, 150*0.94/H_PUNTA, load.mean()+inj)
    pot = (firm+pv.max()*FR_PV)*1000*sc["pn"]*12 if coord else 0.0
    ss  = min(30,30.)*1000*sc["sscc"] if coord else 0.0
    cap = cx["total"]*crf(Costs.wacc,Costs.life)*tax_factor()
    pl  = TOLLS*e_local if peaje_local else 0.0
    return dict(cap=cap/1e6, ox=ox/1e6, pl=pl/1e6, mg=mg/1e6, pot=pot/1e6, ss=ss/1e6,
                cts=(cap+ox+pl-mg-pot-ss)/E_LOAD, curt=d["curt"].sum()/1000,
                exp=d["exp"].sum()/1000, autosuf=e_local/E_LOAD)

A = caso(0,  False, False)   # autoconsumo puro
B = caso(30, True,  False)   # SGC coordinado
C = caso(30, True,  True)    # PPA tradicional, GR propietario

print("="*94)
print("DESCOMPOSICIÓN SOBRE CONFIGURACIÓN IDÉNTICA (76,5 MWp seguidor + 150 MWh/30 MW, base)")
print("="*94)
print(f"{'US$ M/año':<40}{'A autoconsumo':>16}{'B SGC':>13}{'C PPA trad.':>14}")
for k,n in (("cap","Costo de capital"),("ox","OPEX"),("pl","Peajes sobre energía en sitio"),
            ("mg","(−) Margen de mercado"),("pot","(−) Potencia de suficiencia"),
            ("ss","(−) Servicios complementarios")):
    print(f"{n:<40}{A[k]:>16.2f}{B[k]:>13.2f}{C[k]:>14.2f}")
print("-"*94)
print(f"{'COSTO DE SERVIR (USD/MWh)':<40}{A['cts']:>16.1f}{B['cts']:>13.1f}{C['cts']:>14.1f}")
print(f"{'Vertimiento (GWh/año)':<40}{A['curt']:>16.1f}{B['curt']:>13.1f}{C['curt']:>14.1f}")
print(f"{'Autosuficiencia':<40}{A['autosuf']:>15.1%}{B['autosuf']:>13.1%}{C['autosuf']:>14.1%}")
print(f"""
De A a B, el diferencial de {A['cts']-B['cts']:.1f} USD/MWh se compone de:
  · margen de mercado por inyectar excedentes  {(B['mg']-A['mg'])*1e6/E_LOAD:6.1f} USD/MWh
  · potencia de suficiencia                    {(B['pot']-A['pot'])*1e6/E_LOAD:6.1f}
  · servicios complementarios                  {(B['ss']-A['ss'])*1e6/E_LOAD:6.1f}
  · (−) mayor OPEX por ciclado                 {-(B['ox']-A['ox'])*1e6/E_LOAD:6.1f}
De B a C, perder la figura de autoconsumo cuesta {C['cts']-B['cts']:+.1f} USD/MWh
(peajes sobre {B['autosuf']*E_LOAD/1000:.0f} GWh servidos en sitio).""")
