"""Precio PPA ofertable, sensibilidades y valorizacion de la compra del proyecto."""
import numpy as np
from final import evaluate, E_LOAD, SCEN, load
from model import Costs, crf, tax_factor, capex, opex

E_GWH = E_LOAD/1000

# Configuraciones cabeza de serie
A1 = dict(pv_mwp=76.5, bess_mwh=320, bess_mw=20, inj_limit=25)
A2 = dict(pv_mwp=76.5, bess_mwh=150, bess_mw=30, inj_limit=40)

def ppa_ladder(cfg, name):
    print(f"\n{'='*92}\n{name}\n{'='*92}")
    print(f"{'Escenario':<14}{'Costo servir':>14}{'+10% margen':>13}{'+20%':>9}{'+30%':>9}"
          f"{'Ahorro vs 100':>15}")
    out={}
    for sc in ("conservador","base","optimista"):
        r = evaluate(scen=sc, **cfg); c = r["cts"]; out[sc]=r
        print(f"{sc:<14}{c:>14.1f}{c*1.10:>13.1f}{c*1.20:>9.1f}{c*1.30:>9.1f}"
              f"{(100-c*1.20)/100:>14.0%}")
    return out

rA1 = ppa_ladder(A1, "ALTERNATIVA 1 - PPA 24/7 firme con BESS de 16 h en sitio (diseno SQM)")
rA2 = ppa_ladder(A2, "ALTERNATIVA 2 - PPA hibrido optimizado: BESS 150 MWh / 30 MW (5 h)")

print(f"\n{'='*92}\nSENSIBILIDAD AL WACC Y AL CAPEX (escenario base, USD/MWh)\n{'='*92}")
print(f"{'':>16}" + "".join(f"{f'WACC {w:.0%}':>12}" for w in (0.06,0.07,0.08,0.09)))
for name,cfg in (("Alternativa 1",A1),("Alternativa 2",A2)):
    row=f"{name:>16}"
    for w in (0.06,0.07,0.08,0.09):
        old=Costs.wacc; Costs.wacc=w
        row+=f"{evaluate(scen='base',**cfg)['cts']:>12.1f}"; Costs.wacc=old
    print(row)
print()
print(f"{'':>16}" + "".join(f"{f'CAPEX {d:+.0%}':>12}" for d in (-0.15,0,0.15,0.30)))
for name,cfg in (("Alternativa 1",A1),("Alternativa 2",A2)):
    row=f"{name:>16}"
    for d in (-0.15,0,0.15,0.30):
        o_pv,o_bp,o_be = Costs.pv_tracker, Costs.bess_power, Costs.bess_energy
        Costs.pv_tracker*=(1+d); Costs.bess_power*=(1+d); Costs.bess_energy*=(1+d)
        row+=f"{evaluate(scen='base',**cfg)['cts']:>12.1f}"
        Costs.pv_tracker,Costs.bess_power,Costs.bess_energy = o_pv,o_bp,o_be
    print(row)

print(f"\n{'='*92}\nVALORIZACION DE LA COMPRA DEL PROYECTO A SQM\n{'='*92}")
print("Margen anual de GR = (precio PPA - costo de servir) x 166,4 GWh; VAN a 7% real.\n")
print(f"{'Precio PPA':>11}{'Alt.1 margen':>14}{'VAN 15a':>10}{'VAN 20a':>10}"
      f"{'Alt.2 margen':>14}{'VAN 15a':>10}{'VAN 20a':>10}")
for p in (60, 65, 70, 75, 80, 85):
    c1 = rA1["base"]["cts"]; c2 = rA2["base"]["cts"]
    m1 = (p-c1)*E_GWH*1000/1e6; m2 = (p-c2)*E_GWH*1000/1e6
    v = lambda m,n: m/crf(0.07,n)
    print(f"{p:>11}{m1:>13.2f}M{v(m1,15):>9.1f}M{v(m1,20):>9.1f}M"
          f"{m2:>13.2f}M{v(m2,15):>9.1f}M{v(m2,20):>9.1f}M")

print(f"""
Lectura: a un precio PPA de 70 USD/MWh (30% bajo la referencia de ~100 USD/MWh que hoy
paga un cliente libre), la Alternativa 2 genera un margen de US$ {(70-rA2['base']['cts'])*E_GWH*1000/1e6:.1f} M/ano,
equivalente a un VAN de US$ {((70-rA2['base']['cts'])*E_GWH*1000/1e6)/crf(0.07,15):.0f} M a 15 anos. Ese VAN es la bolsa desde la cual
se paga (i) el activo de desarrollo a SQM y (ii) el retorno incremental de GR.
La Alternativa 1 al mismo precio deja US$ {(70-rA1['base']['cts'])*E_GWH*1000/1e6:.1f} M/ano.""")
