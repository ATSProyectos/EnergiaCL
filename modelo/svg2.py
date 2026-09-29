E = lambda s: s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

# ---------------------------------------------------------- FIG 4: puente de valor
STEPS = [
    ("Autoconsumo puro\nsin inyección", None, 94.2, "total"),
    ("Inyectar\nexcedentes", -23.9, None, "down"),
    ("Potencia de\nsuficiencia", -22.0, None, "down"),
    ("Servicios\ncomplementarios", -3.6, None, "down"),
    ("Mayor OPEX\npor ciclado", +1.4, None, "up"),
    ("SGC\ncoordinado", None, 46.1, "total"),
    ("Pérdida del\nautoconsumo", +11.1, None, "up"),
    ("PPA tradicional\nGR prop.", None, 57.3, "total"),
]
def fig_puente():
    W,H = 760, 430
    ml,mr,mt,mb = 52, 26, 34, 76
    pw,ph = W-ml-mr, H-mt-mb
    ymin,ymax = 0, 105
    n = len(STEPS)
    slot = pw/n
    bw = slot*0.56
    Y = lambda v: mt + (ymax-v)/(ymax-ymin)*ph
    s=[f'<svg viewBox="0 0 {W} {H}" role="img" class="chart" aria-label="Puente de valor entre vehículos regulatorios">']
    s.append('<title>De autoconsumo puro a SGC coordinado y a PPA tradicional: origen de cada diferencia</title>')
    for v in (0,25,50,75,100):
        s.append(f'<line x1="{ml}" y1="{Y(v):.1f}" x2="{ml+pw}" y2="{Y(v):.1f}" class="grid"/>')
        s.append(f'<text x="{ml-9}" y="{Y(v)+4:.1f}" class="tick end">{v}</text>')
    s.append(f'<text x="{ml-40}" y="{mt+ph/2:.1f}" class="axis mid" transform="rotate(-90 {ml-40} {mt+ph/2:.1f})">USD/MWh</text>')
    run = 0.0
    for i,(lbl,delta,total,kind) in enumerate(STEPS):
        cx = ml + slot*i + slot/2
        if kind == "total":
            top, bot, val = total, 0.0, total
            cls = "s1"
            s.append(f'<rect x="{cx-bw/2:.1f}" y="{Y(top):.1f}" width="{bw:.1f}" '
                     f'height="{Y(bot)-Y(top):.1f}" rx="3" class="bar {cls}">'
                     f'<title>{E(lbl.replace(chr(10)," "))}: {total} USD/MWh</title></rect>')
            s.append(f'<text x="{cx:.1f}" y="{Y(top)-9:.1f}" class="dlbl {cls} mid">{total:.1f}</text>')
            run = total
        else:
            new = run + delta
            top, bot = max(run,new), min(run,new)
            cls = "s3" if delta<0 else "s2"
            s.append(f'<rect x="{cx-bw/2:.1f}" y="{Y(top):.1f}" width="{bw:.1f}" '
                     f'height="{max(Y(bot)-Y(top),2):.1f}" rx="3" class="bar {cls}" opacity="0.62">'
                     f'<title>{E(lbl.replace(chr(10)," "))}: {delta:+.1f} USD/MWh</title></rect>')
            s.append(f'<text x="{cx:.1f}" y="{Y(top)-9:.1f}" class="dlbl {cls} mid">{delta:+.1f}</text>')
            run = new
        if i < n-1:
            nx = ml + slot*(i+1) + slot/2
            s.append(f'<line x1="{cx+bw/2:.1f}" y1="{Y(run):.1f}" x2="{nx-bw/2:.1f}" '
                     f'y2="{Y(run):.1f}" class="connector"/>')
        for j,part in enumerate(lbl.split("\n")):
            s.append(f'<text x="{cx:.1f}" y="{mt+ph+20+j*13:.1f}" class="tick mid">{E(part)}</text>')
    s.append('</svg>')
    return "\n".join(s)

# ---------------------------------------------------------- FIG 5: matriz de escenarios
ESC = [
  ("D0 · Diseño SQM tal cual, aislado",              111.7, 109.7, 108.0, "s1"),
  ("E1 · Autoconsumo puro, sin inyección",            90.9,  90.1,  89.4, "s1"),
  ("E3 · PPA tradicional, GR propietario",            66.3,  57.3,  52.0, "s3"),
  ("E2 · SGC coordinado  (recomendado)",              54.7,  46.1,  41.3, "s2"),
]
def fig_matriz():
    W=760; rowh=46; mt=76; ml=286; mr=74
    H = mt + len(ESC)*rowh + 26
    pw = W-ml-mr
    xmin,xmax = 30,122
    X = lambda v: ml+(v-xmin)/(xmax-xmin)*pw
    ytop, ybot = mt-16, mt+len(ESC)*rowh-16
    s=[f'<svg viewBox="0 0 {W} {H}" role="img" class="chart" aria-label="Costo de servir por escenario regulatorio">']
    s.append('<title>Costo de servir el bloque 24/7 por vehículo regulatorio</title>')
    lg=16
    s.append(f'<circle cx="{ml+5}" cy="{lg-4}" r="5" class="dot-base neutral"/>')
    s.append(f'<text x="{ml+16}" y="{lg}" class="lbl-ann">escenario base</text>')
    s.append(f'<line x1="{ml+118}" y1="{lg-4}" x2="{ml+142}" y2="{lg-4}" class="rng neutral"/>')
    s.append(f'<text x="{ml+150}" y="{lg}" class="lbl-ann">rango conservador–optimista</text>')
    for v in (40,60,80,100,120):
        s.append(f'<line x1="{X(v):.1f}" y1="{ytop}" x2="{X(v):.1f}" y2="{ybot}" class="grid"/>')
        s.append(f'<text x="{X(v):.1f}" y="{ytop-8}" class="tick mid">{v}</text>')
    s.append(f'<text x="{ml}" y="{ytop-26}" class="axis">costo de servir el bloque 24/7 · USD/MWh</text>')
    s.append(f'<line x1="{X(100):.1f}" y1="{ytop}" x2="{X(100):.1f}" y2="{ybot}" class="ref"/>')
    s.append(f'<text x="{X(100):.1f}" y="{ybot+18}" class="lbl-ann mid">≈100 · tarifa actual del cliente</text>')
    for i,(name,c,b,o,cls) in enumerate(ESC):
        y = mt + i*rowh + 8
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

open("fig4.svg","w").write(fig_puente())
open("fig5.svg","w").write(fig_matriz())
print("fig4, fig5 generadas")
