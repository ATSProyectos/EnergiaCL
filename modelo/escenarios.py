"""
Matriz de escenarios: vehiculo regulatorio x configuracion tecnica.

El eje nuevo lo introduce la minuta del 29-sep-2026: la figura de autoconsumo
exige mismo propietario (o mandato) y el reglamento busca impedir que grandes
clientes la usen para alimentar consumo EXISTENTE sin ampliaciones reales.
Si la figura no aplica, la energia autoconsumida deja de ahorrar peajes.
"""
import numpy as np
from solar import generate
from model import load_profile, capex, opex, levelized, Costs, crf, tax_factor
from final import cmg_for, SCEN
from dispatch_lp import solve

TOLLS = 18.0; H_PUNTA = 4.0; FR_PV = 0.10
LOAD_MW = 19.0
load = load_profile(LOAD_MW); E_LOAD = load.sum()

_pv = {}
def pv_series(mwp, tracker=True, dcac=1.30):
    k = (round(mwp,2), tracker, dcac)
    if k not in _pv:
        _pv[k] = generate(mwp*1000, config="tracker" if tracker else "fixed", dc_ac_ratio=dcac)["ac_mw"]
    return _pv[k]

def run(pv_mwp, mwh, mw, scen="base", tracker=True, dcac=1.30, inj_limit=30.0,
        coordinated=True, tolls_on_local=False, label=""):
    """tolls_on_local=True  -> la energia servida en sitio TAMBIEN paga peajes
                               (no hay figura de autoconsumo: GR propietario, PPA tradicional)"""
    sc = SCEN[scen]; cmg = cmg_for(sc)
    pv = pv_series(pv_mwp, tracker, dcac)
    d = solve(pv, load, cmg, mwh, mw, tolls=TOLLS,
              inj_limit=inj_limit if coordinated else 0.0, grid_charge=coordinated)
    cx = capex(pv_mwp*1000, mwh, mw, tracker=tracker)
    ox = opex(pv_mwp*1000, mwh, cx["total"], cycles=d["cycles"])

    e_imp = d["imp"].sum(); e_exp = d["exp"].sum(); e_local = d["served_local"].sum()
    c_imp = ((cmg + TOLLS)*d["imp"]).sum(); r_exp = (cmg*d["exp"]).sum()
    peaje_local = TOLLS*e_local if tolls_on_local else 0.0

    merch_gross = r_exp - c_imp
    merch = merch_gross*sc["cap"] if merch_gross > 0 else merch_gross/max(sc["cap"],0.5)
    firm = min(mw, mwh*0.94/H_PUNTA, load.mean()+inj_limit) if mwh else 0.0
    r_pot = (firm + pv.max()*FR_PV)*1000*sc["pn"]*12 if coordinated else 0.0
    r_sscc = min(mw,30.0)*1000*sc["sscc"] if (coordinated and mwh) else 0.0

    capital = cx["total"]*crf(Costs.wacc, Costs.life)*tax_factor()
    cts = (capital + ox + peaje_local - merch - r_pot - r_sscc)/E_LOAD
    return dict(label=label, pv=pv_mwp, mwh=mwh, mw=mw, capex=cx["total"]/1e6,
                gen=pv.sum()/1000, e_local=e_local/1000, e_imp=e_imp/1000, e_exp=e_exp/1000,
                e_curt=d["curt"].sum()/1000, autosuf=e_local/E_LOAD, cycles=d["cycles"],
                peaje_local=peaje_local/1e6, cts=cts)

if __name__ == "__main__":
    print("="*104)
    print("COSTO DE LA PERDIDA DE LA FIGURA DE AUTOCONSUMO")
    print("(peajes sobre la energia servida en sitio: 18 USD/MWh)")
    print("="*104)
    print(f"{'Configuración':<44}{'con autoconsumo':>17}{'sin autoconsumo':>17}{'Δ':>9}{'Autosuf':>9}")
    CFG = [
        ("Diseño SQM · fija, 320 MWh/20 MW, aislado", 76.5,320,20,
         dict(tracker=False,dcac=1.20,coordinated=False,inj_limit=0)),
        ("Alt. 1 · seguidor, 320 MWh/20 MW (16 h)",   76.5,320,20, dict(inj_limit=25)),
        ("Alt. 1b · seguidor, 320 MWh/30 MW (11 h)",  76.5,320,30, dict(inj_limit=30)),
        ("Alt. 2 · seguidor, 150 MWh/30 MW (5 h)",    76.5,150,30, dict(inj_limit=30)),
        ("Sólo FV, sin almacenamiento",               76.5,  0, 0, dict(inj_limit=30)),
    ]
    for lbl,p,e,w,kw in CFG:
        a = run(p,e,w,tolls_on_local=False,label=lbl,**kw)
        b = run(p,e,w,tolls_on_local=True, label=lbl,**kw)
        print(f"{lbl:<44}{a['cts']:>17.1f}{b['cts']:>17.1f}{b['cts']-a['cts']:>+9.1f}{a['autosuf']:>9.1%}")
    print("\nLectura: cuanto MAS autosuficiente es la configuracion, MAS pierde si la figura")
    print("de autoconsumo no se materializa. La Alternativa 2 es la menos expuesta.")
