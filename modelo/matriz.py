"""Matriz final de escenarios para la decision interna."""
from escenarios import run, E_LOAD
from model import Costs, crf

E_GWH = E_LOAD/1000
REF_CLIENTE_LIBRE = 100.0   # precio final promedio que paga hoy un cliente libre

ESC = [
 ("E1", "Autoconsumo puro · SQM propietario · sin inyección",
  dict(pv_mwp=76.5, mwh=240, mw=30, coordinated=False, inj_limit=0, tolls_on_local=False)),
 ("E2", "SGC coordinado · con inyección · beneficio de peaje",
  dict(pv_mwp=76.5, mwh=150, mw=30, coordinated=True,  inj_limit=30, tolls_on_local=False)),
 ("E3", "PPA tradicional · GR propietario · sin beneficio de peaje",
  dict(pv_mwp=76.5, mwh=150, mw=30, coordinated=True,  inj_limit=30, tolls_on_local=True)),
 ("D0", "Diseño SQM tal cual · fija, 320 MWh/20 MW, aislado",
  dict(pv_mwp=76.5, mwh=320, mw=20, coordinated=False, inj_limit=0, tolls_on_local=False,
       tracker=False, dcac=1.20)),
]

print("="*108)
print("MATRIZ DE ESCENARIOS — costo de servir el bloque 24/7 de SQM (166,4 GWh/año)")
print("="*108)
print(f"{'':<4}{'Escenario':<52}{'conserv':>9}{'base':>8}{'optim':>8}{'CAPEX':>8}{'Autosuf':>9}{'Vert':>7}")
R={}
for cod,lbl,kw in ESC:
    vals={}
    for sc in ("conservador","base","optimista"):
        r=run(scen=sc,label=lbl,**kw); vals[sc]=r
    R[cod]=vals; b=vals["base"]
    print(f"{cod:<4}{lbl:<52}{vals['conservador']['cts']:>9.1f}{b['cts']:>8.1f}"
          f"{vals['optimista']['cts']:>8.1f}{b['capex']:>8.1f}{b['autosuf']:>9.1%}{b['e_curt']:>7.1f}")

print("\n" + "="*108)
print("DESCOMPOSICIÓN DEL VALOR (escenario base)")
print("="*108)
a,b2,c = R["E1"]["base"]["cts"], R["E2"]["base"]["cts"], R["E3"]["base"]["cts"]
print(f"  Autoconsumo puro (E1)                                  {a:6.1f} USD/MWh")
print(f"  → valor de COORDINAR: inyección + potencia + SSCC      {b2-a:+6.1f}   (E1 → E2)")
print(f"  SGC coordinado (E2)                                    {b2:6.1f} USD/MWh")
print(f"  → costo de PERDER el beneficio de peaje del autoconsumo {c-b2:+6.1f}   (E2 → E3)")
print(f"  PPA tradicional con GR propietario (E3)                {c:6.1f} USD/MWh")
print(f"\n  El derecho a inyectar y coordinar vale {abs(b2-a):.0f} USD/MWh.")
print(f"  La figura de autoconsumo vale {abs(c-b2):.0f} USD/MWh.")
print(f"  Incluso SIN autoconsumo (E3), coordinar supera a la figura de autoconsumo por {a-c:.0f} USD/MWh.")

print("\n" + "="*108)
print("PRECIO OFERTABLE Y MARGEN GR  (ancla: escenario conservador + margen)")
print("="*108)
print(f"{'':<4}{'Escenario':<46}{'piso':>7}{'PPA sugerido':>14}{'ahorro SQM':>12}"
      f"{'margen/año':>12}{'VAN 15a':>10}")
SUG = {"E1": 100, "E2": 65, "E3": 72, "D0": 118}
for cod,lbl,kw in ESC:
    piso = R[cod]["conservador"]["cts"]; p = SUG[cod]
    m = (p - R[cod]["base"]["cts"])*E_GWH*1000/1e6
    van = m/crf(0.07,15)
    ah = (REF_CLIENTE_LIBRE-p)/REF_CLIENTE_LIBRE
    print(f"{cod:<4}{lbl[:44]:<46}{piso:>7.1f}{p:>11}{'':>3}{ah:>11.0%}{m:>11.2f}M{van:>9.1f}M")
print("\n  E1 no deja margen ofertable: su piso conservador (90,9) roza la tarifa actual del cliente.")
