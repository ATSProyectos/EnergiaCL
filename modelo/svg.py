import json
d = json.load(open("charts.json"))
E = lambda s: (s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;"))

# ---------------------------------------------------------------- CHART 1
def chart_optimizacion():
    W,H = 760, 420
    ml,mr,mt,mb = 52, 118, 28, 46
    pw,ph = W-ml-mr, H-mt-mb
    curve = d["curve"]
    xs = [r["h"] for r in curve]
    xmax = 16
    ymin,ymax = 30, 105
    X = lambda h: ml + h/xmax*pw
    Y = lambda v: mt + (ymax-v)/(ymax-ymin)*ph
    s=[]
    s.append(f'<svg viewBox="0 0 {W} {H}" role="img" class="chart" aria-label="Costo de servir el bloque 24/7 segun la duracion del almacenamiento">')
    s.append('<title>Costo de servir el bloque 24/7 segun la duracion del BESS</title>')
    # banda optimo
    s.append(f'<rect x="{X(4):.1f}" y="{mt}" width="{X(6)-X(4):.1f}" height="{ph}" class="band"/>')
    s.append(f'<text x="{(X(4)+X(6))/2:.1f}" y="{mt-9}" class="lbl-ann mid">banda óptima 4–6 h</text>')
    # grilla
    for v in range(30,106,15):
        s.append(f'<line x1="{ml}" y1="{Y(v):.1f}" x2="{ml+pw}" y2="{Y(v):.1f}" class="grid"/>')
        s.append(f'<text x="{ml-9}" y="{Y(v)+4:.1f}" class="tick end">{v}</text>')
    for h in [0,2,4,6,8,10,12,14,16]:
        s.append(f'<text x="{X(h):.1f}" y="{mt+ph+20}" class="tick mid">{h}</text>')
    s.append(f'<text x="{ml+pw/2:.1f}" y="{mt+ph+40}" class="axis mid">horas de almacenamiento (BESS de 30 MW)</text>')
    s.append(f'<text x="{ml-40}" y="{mt+ph/2:.1f}" class="axis mid" transform="rotate(-90 {ml-40} {mt+ph/2:.1f})">USD/MWh</text>')
    # marcador diseno SQM
    s.append(f'<line x1="{X(16):.1f}" y1="{mt}" x2="{X(16):.1f}" y2="{mt+ph}" class="ref"/>')
    series = [("conservador","s1"),("base","s2"),("optimista","s3")]
    for name,cls in series:
        pts = " ".join(f"{X(r['h']):.1f},{Y(r[name]):.1f}" for r in curve)
        s.append(f'<polyline points="{pts}" class="line {cls}"/>')
        for r in curve:
            s.append(f'<circle cx="{X(r["h"]):.1f}" cy="{Y(r[name]):.1f}" r="4" class="dot {cls}">'
                     f'<title>{name} · {r["h"]} h ({r["mwh"]} MWh): {r[name]} USD/MWh</title></circle>')
        last = curve[-1]
        s.append(f'<text x="{X(16)+12:.1f}" y="{Y(last[name])+4:.1f}" class="dlbl {cls}">{name} {last[name]:.0f}</text>')
    # anotacion diseno SQM y optimo
    opt = min(curve, key=lambda r: r["base"])
    s.append(f'<circle cx="{X(opt["h"]):.1f}" cy="{Y(opt["base"]):.1f}" r="7.5" class="halo"/>')
    s.append(f'<text x="{X(opt["h"]):.1f}" y="{Y(opt["base"])-18:.1f}" class="lbl-ann mid">mínimo {opt["base"]:.1f}</text>')
    d16 = curve[-1]
    s.append(f'<text x="{X(16)-8:.1f}" y="{mt+14}" class="lbl-ann end">diseño SQM</text>')
    s.append('</svg>')
    return "\n".join(s)

# ---------------------------------------------------------------- CHART 2
def chart_perfil():
    W,H = 760, 430
    ml,mr = 54, 20
    pw = W-ml-mr
    top_h, gap, bot_h = 150, 54, 120
    mt1 = 26; mt2 = mt1+top_h+gap
    X = lambda h: ml + (h+0.5)/24*pw
    pv,ld,cm = d["pv_h"], d["load_h"], d["cmg_h"]
    s=[f'<svg viewBox="0 0 {W} {H}" role="img" class="chart" aria-label="Perfil horario medio de generacion, consumo y costo marginal">']
    s.append('<title>Perfil horario medio: generacion FV, consumo de SQM y costo marginal de la barra</title>')
    # --- panel superior: MW
    ymax1 = 60
    Y1 = lambda v: mt1 + (ymax1-v)/ymax1*top_h
    for v in (0,20,40,60):
        s.append(f'<line x1="{ml}" y1="{Y1(v):.1f}" x2="{ml+pw}" y2="{Y1(v):.1f}" class="grid"/>')
        s.append(f'<text x="{ml-9}" y="{Y1(v)+4:.1f}" class="tick end">{v}</text>')
    s.append(f'<text x="{ml}" y="{mt1-10}" class="axis">Generación FV y consumo · MW</text>')
    area = " ".join(f"{X(i):.1f},{Y1(v):.1f}" for i,v in enumerate(pv))
    s.append(f'<polygon points="{ml},{Y1(0):.1f} {area} {ml+pw},{Y1(0):.1f}" class="fill s1"/>')
    s.append(f'<polyline points="{area}" class="line s1"/>')
    lp = " ".join(f"{X(i):.1f},{Y1(v):.1f}" for i,v in enumerate(ld))
    s.append(f'<polyline points="{lp}" class="line s2"/>')
    for i in range(24):
        s.append(f'<rect x="{X(i)-pw/48:.1f}" y="{mt1}" width="{pw/24:.1f}" height="{top_h}" class="hit">'
                 f'<title>{i:02d}:00 — FV {pv[i]:.1f} MW · consumo {ld[i]:.1f} MW</title></rect>')
    s.append(f'<text x="{X(12):.1f}" y="{Y1(pv[12])-10:.1f}" class="dlbl s1 mid">FV 76,5 MWp</text>')
    s.append(f'<text x="{X(2):.1f}" y="{Y1(ld[2])-10:.1f}" class="dlbl s2">consumo SQM 19 MW</text>')
    # --- panel inferior: USD/MWh
    ymax2 = 160
    Y2 = lambda v: mt2 + (ymax2-v)/ymax2*bot_h
    for v in (0,50,100,150):
        s.append(f'<line x1="{ml}" y1="{Y2(v):.1f}" x2="{ml+pw}" y2="{Y2(v):.1f}" class="grid"/>')
        s.append(f'<text x="{ml-9}" y="{Y2(v)+4:.1f}" class="tick end">{v}</text>')
    s.append(f'<text x="{ml}" y="{mt2-10}" class="axis">Costo marginal barra Tarapacá · USD/MWh</text>')
    bw = pw/24*0.72
    for i,v in enumerate(cm):
        h = Y2(0)-Y2(v)
        s.append(f'<rect x="{X(i)-bw/2:.1f}" y="{Y2(v):.1f}" width="{bw:.1f}" height="{max(h,0.6):.1f}" '
                 f'rx="3" class="bar s3"><title>{i:02d}:00 — {v} USD/MWh</title></rect>')
    for i in (12,19):
        s.append(f'<text x="{X(i):.1f}" y="{Y2(cm[i])-8:.1f}" class="dlbl s3 mid">{cm[i]:.0f}</text>')
    for i in range(0,24,3):
        s.append(f'<text x="{X(i):.1f}" y="{mt2+bot_h+20}" class="tick mid">{i:02d}</text>')
    s.append(f'<text x="{ml+pw/2:.1f}" y="{mt2+bot_h+40}" class="axis mid">hora del día</text>')
    s.append('</svg>')
    return "\n".join(s)

# ---------------------------------------------------------------- CHART 3
CONF = [
    ("Diseño SQM · fija, 320 MWh/20 MW, aislado", 111.7, 109.7, 108.0),
    ("Alt. 1 · seguidor, 320 MWh/20 MW (16 h)",    78.5,  74.1,  73.4),
    ("Alt. 2 · seguidor, 240 MWh/20 MW (8 h)",     61.6,  50.5,  41.4),
    ("Alt. 2 · seguidor, 180 MWh/30 MW (6 h)",     56.6,  47.1,  40.2),
    ("Alt. 2 · seguidor, 150 MWh/30 MW (5 h)",     54.4,  45.6,  40.4),
    ("Alt. 2 · seguidor, 120 MWh/30 MW (4 h)",     54.1,  47.1,  43.8),
    ("Sólo FV, sin almacenamiento",                78.9,  88.9, 102.1),
]
def chart_configs():
    W = 760; rowh = 40; mt = 78; ml = 296; mr = 74
    H = mt + len(CONF)*rowh + 26
    pw = W-ml-mr
    xmin,xmax = 30, 122
    X = lambda v: ml + (v-xmin)/(xmax-xmin)*pw
    ytop, ybot = mt-16, mt+len(CONF)*rowh-12
    s=[f'<svg viewBox="0 0 {W} {H}" role="img" class="chart" aria-label="Costo de servir por configuracion y escenario">']
    s.append('<title>Costo de servir el bloque 24/7 por configuración, rango entre escenario conservador y optimista</title>')
    # leyenda en su propia linea
    lg = 16
    s.append(f'<circle cx="{ml+5}" cy="{lg-4}" r="5" class="dot-base neutral"/>')
    s.append(f'<text x="{ml+16}" y="{lg}" class="lbl-ann">escenario base</text>')
    s.append(f'<line x1="{ml+118}" y1="{lg-4}" x2="{ml+142}" y2="{lg-4}" class="rng neutral"/>')
    s.append(f'<text x="{ml+150}" y="{lg}" class="lbl-ann">rango conservador–optimista</text>')
    # eje
    for v in (40,60,80,100,120):
        s.append(f'<line x1="{X(v):.1f}" y1="{ytop}" x2="{X(v):.1f}" y2="{ybot}" class="grid"/>')
        s.append(f'<text x="{X(v):.1f}" y="{ytop-8}" class="tick mid">{v}</text>')
    s.append(f'<text x="{ml}" y="{ytop-26}" class="axis">costo de servir el bloque 24/7 · USD/MWh</text>')
    s.append(f'<line x1="{X(100):.1f}" y1="{ytop}" x2="{X(100):.1f}" y2="{ybot}" class="ref"/>')
    s.append(f'<text x="{X(100):.1f}" y="{ybot+18}" class="lbl-ann mid">≈100 · cliente libre</text>')
    for i,(name,c,b,o) in enumerate(CONF):
        y = mt + i*rowh + 10
        cls = "s2" if "5 h" in name else ("s1" if ("16 h" in name or "aislado" in name) else "s3")
        s.append(f'<text x="{ml-16}" y="{y+4:.1f}" class="rowlbl end">{E(name)}</text>')
        lo,hi = min(c,o), max(c,o)
        s.append(f'<line x1="{X(lo):.1f}" y1="{y:.1f}" x2="{X(hi):.1f}" y2="{y:.1f}" class="rng {cls}">'
                 f'<title>{E(name)} — conservador {c} · base {b} · optimista {o} USD/MWh</title></line>')
        for v in (lo,hi):
            s.append(f'<circle cx="{X(v):.1f}" cy="{y:.1f}" r="3.5" class="dot {cls}"/>')
        s.append(f'<circle cx="{X(b):.1f}" cy="{y:.1f}" r="6.5" class="dot-base {cls}">'
                 f'<title>{E(name)} — base {b} USD/MWh</title></circle>')
        s.append(f'<text x="{X(hi)+13:.1f}" y="{y+4:.1f}" class="dlbl {cls}">{b:.1f}</text>')
    s.append('</svg>')
    return "\n".join(s)

open("fig1.svg","w").write(chart_optimizacion())
open("fig2.svg","w").write(chart_perfil())
open("fig3.svg","w").write(chart_configs())
print("figuras generadas:", [len(open(f'fig{i}.svg').read()) for i in (1,2,3)])
