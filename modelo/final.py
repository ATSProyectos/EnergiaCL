"""Analisis final: configuraciones, escenarios de mercado y precio PPA ofertable."""
import numpy as np, json
from solar import generate
from model import load_profile, capex, opex, levelized, Costs, crf, tax_factor
from market import cmg_profile
from dispatch_lp import solve

LOAD_MW=19.0; TOLLS=18.0; CMG=60.0; H_PUNTA=4.0; FR_PV=0.10
load = load_profile(LOAD_MW); E_LOAD = load.sum()
cmg_raw = cmg_profile(CMG)

SCEN = {
    # nombre        compresion_spread  captura  precio_potencia  sscc
    "conservador": dict(comp=0.45, cap=0.70, pn=6.5, sscc=0.0,  cmg=55.0),
    "base":        dict(comp=0.25, cap=0.80, pn=8.5, sscc=20.0, cmg=60.0),
    "optimista":   dict(comp=0.00, cap=0.90, pn=9.5, sscc=35.0, cmg=65.0),
}

def cmg_for(sc):
    c = cmg_raw * sc["cmg"]/CMG
    m = c.mean()
    return np.clip(m + (c-m)*(1-sc["comp"]), 0, None)

_pv={}
def pv_series(mwp, tracker=True, dcac=1.30):
    k=(round(mwp,2),tracker,dcac)
    if k not in _pv:
        _pv[k]=generate(mwp*1000, config="tracker" if tracker else "fixed", dc_ac_ratio=dcac)["ac_mw"]
    return _pv[k]

def evaluate(pv_mwp, bess_mwh, bess_mw, scen="base", tracker=True, dcac=1.30,
             inj_limit=40.0, coordinated=True, label=""):
    sc = SCEN[scen]; cmg = cmg_for(sc)
    pv = pv_series(pv_mwp, tracker, dcac)
    d = solve(pv, load, cmg, bess_mwh, bess_mw, tolls=TOLLS,
              inj_limit=inj_limit if coordinated else 0.0, grid_charge=coordinated)
    cx = capex(pv_mwp*1000, bess_mwh, bess_mw, tracker=tracker)
    ox = opex(pv_mwp*1000, bess_mwh, cx["total"], cycles=d["cycles"])

    e_imp=d["imp"].sum(); e_exp=d["exp"].sum(); e_local=d["served_local"].sum()
    c_imp=((cmg+TOLLS)*d["imp"]).sum(); r_exp=(cmg*d["exp"]).sum()

    # El margen merchant (export - import) se castiga por la captura imperfecta
    merch_gross = r_exp - c_imp
    merch = merch_gross*sc["cap"] if merch_gross > 0 else merch_gross/max(sc["cap"],0.5)

    firm = min(bess_mw, bess_mwh*0.94/H_PUNTA, load.mean()+inj_limit) if bess_mwh else 0.0
    r_pot = (firm + pv.max()*FR_PV)*1000*sc["pn"]*12 if coordinated else 0.0
    r_sscc = min(bess_mw,30.0)*1000*sc["sscc"] if (coordinated and bess_mwh) else 0.0

    capital = cx["total"]*crf(Costs.wacc, Costs.life)*tax_factor()
    cts = (capital + ox - merch - r_pot - r_sscc)/E_LOAD
    return dict(label=label, scen=scen, pv=pv_mwp, mwh=bess_mwh, mw=bess_mw,
                gen=pv.sum()/1000, capex=cx["total"]/1e6, opex=ox/1e6, capital=capital/1e6,
                e_local=e_local/1000, e_imp=e_imp/1000, e_exp=e_exp/1000,
                e_curt=d["curt"].sum()/1000, autosuf=e_local/E_LOAD, cycles=d["cycles"],
                merch=merch/1e6, r_pot=r_pot/1e6, r_sscc=r_sscc/1e6, firm=firm,
                cts=cts, lcoe=levelized(cx["total"],ox,e_local+e_exp),
                p_imp=(cmg*d["imp"]).sum()/max(e_imp,1e-9), p_exp=r_exp/max(e_exp,1e-9))

CONFIGS = [
  ("C0  Diseno SQM off-grid (fija, 320 MWh/20 MW, sin coordinar)", 76.5,320,20, dict(tracker=False,dcac=1.20,coordinated=False,inj_limit=0)),
  ("A1  24/7 firme: seguidor + 320 MWh/20 MW coordinado",          76.5,320,20, dict(inj_limit=25)),
  ("A2a Hibrido 8 h: seguidor + 160 MWh/20 MW",                    76.5,160,20, dict(inj_limit=40)),
  ("A2b Hibrido 6 h: seguidor + 150 MWh/25 MW",                    76.5,150,25, dict(inj_limit=40)),
  ("A2c Hibrido 5 h: seguidor + 150 MWh/30 MW  (RECOMENDADO)",     76.5,150,30, dict(inj_limit=40)),
  ("A2d Hibrido 4 h: seguidor + 120 MWh/30 MW",                    76.5,120,30, dict(inj_limit=40)),
  ("A2e Solo FV, sin BESS (referencia)",                           76.5,  0, 0, dict(inj_limit=40)),
]

print(f"Consumo SQM {E_LOAD/1000:.1f} GWh/ano | referencia spot+peajes "
      f"{((cmg_raw+TOLLS)*load).sum()/E_LOAD:.1f} USD/MWh\n")
print("="*112)
print("COSTO DE SERVIR EL BLOQUE 24/7 (USD/MWh) POR ESCENARIO DE MERCADO")
print("="*112)
print(f"{'Configuracion':<56}{'conserv.':>11}{'base':>9}{'optim.':>9}{'CAPEX':>9}{'Autosuf':>9}")
results={}
for lbl,p,e,w,kw in CONFIGS:
    row=f"{lbl:<56}"
    for sc in ("conservador","base","optimista"):
        r=evaluate(p,e,w,scen=sc,label=lbl,**kw); results[(lbl,sc)]=r
        row+=f"{r['cts']:>11.1f}" if sc=="conservador" else f"{r['cts']:>9.1f}"
    b=results[(lbl,"base")]
    row+=f"{b['capex']:>9.1f}{b['autosuf']:>9.1%}"
    print(row)

print("\n"+"="*112)
print("DETALLE - ESCENARIO BASE")
print("="*112)
for lbl,p,e,w,kw in CONFIGS:
    r=results[(lbl,"base")]
    dur=r['mwh']/r['mw'] if r['mw'] else 0
    print(f"\n{lbl}")
    print(f"  FV {r['pv']:.1f} MWp -> {r['gen']:.0f} GWh | BESS {r['mwh']:.0f} MWh/{r['mw']:.0f} MW ({dur:.0f} h) "
          f"| CAPEX US$ {r['capex']:.1f} M | {r['cycles']:.0f} ciclos/a")
    print(f"  Autosuf. {r['autosuf']:.1%} | importa {r['e_imp']:.1f} GWh @ {r['p_imp']:.0f} USD/MWh "
          f"| exporta {r['e_exp']:.1f} GWh @ {r['p_exp']:.0f} | vertido {r['e_curt']:.1f} GWh")
    print(f"  US$M/a: capital {r['capital']:.2f} + opex {r['opex']:.2f} "
          f"- merchant {r['merch']:.2f} - potencia {r['r_pot']:.2f} ({r['firm']:.0f} MW firmes) - SSCC {r['r_sscc']:.2f}")
    print(f"  >> costo de servir {r['cts']:.1f} USD/MWh | LCOE del activo {r['lcoe']:.1f}")

json.dump({f"{k[0]}|{k[1]}": {kk:vv for kk,vv in v.items() if not isinstance(vv,np.ndarray)}
           for k,v in results.items()}, open("results.json","w"), indent=1, default=float)
