CSS = r"""
:root{
  --paper:#F3F4F1; --surface:#FFFFFF; --surface-2:#EAECE7;
  --ink:#131F23; --ink-2:#3A4A4E; --muted:#65767A;
  --line:#D6DAD4; --line-strong:#B9C0B9;
  --accent:#0E6B64; --accent-soft:#DDE9E6; --accent-ink:#0A4F4A;
  --warn:#A2601B; --warn-soft:#F0E4D3;
  --s1:#2a78d6; --s2:#eb6834; --s3:#1baf7a;
  --shadow:0 1px 2px rgba(19,31,35,.06), 0 8px 24px -18px rgba(19,31,35,.35);
  --maxw:1120px;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --paper:#0D1518; --surface:#131E22; --surface-2:#1A272B;
    --ink:#E6EBE7; --ink-2:#B6C3C1; --muted:#8A9B9A;
    --line:#26363A; --line-strong:#3A4E52;
    --accent:#4BAEA4; --accent-soft:#16302F; --accent-ink:#8FD3CA;
    --warn:#D79A4E; --warn-soft:#2E2415;
    --s1:#3987e5; --s2:#d95926; --s3:#199e70;
    --shadow:0 1px 2px rgba(0,0,0,.4), 0 8px 24px -18px rgba(0,0,0,.9);
  }
}
:root[data-theme="dark"]{
  --paper:#0D1518; --surface:#131E22; --surface-2:#1A272B;
  --ink:#E6EBE7; --ink-2:#B6C3C1; --muted:#8A9B9A;
  --line:#26363A; --line-strong:#3A4E52;
  --accent:#4BAEA4; --accent-soft:#16302F; --accent-ink:#8FD3CA;
  --warn:#D79A4E; --warn-soft:#2E2415;
  --s1:#3987e5; --s2:#d95926; --s3:#199e70;
  --shadow:0 1px 2px rgba(0,0,0,.4), 0 8px 24px -18px rgba(0,0,0,.9);
}
body{background:var(--paper);color:var(--ink);
  font-family:"IBM Plex Sans",-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  font-size:16px;line-height:1.6;-webkit-font-smoothing:antialiased;margin:0;}
*,*::before,*::after{box-sizing:border-box;}
.wrap{max-width:var(--maxw);margin:0 auto;padding:0 28px;}
@media (max-width:640px){.wrap{padding:0 16px;}}
h1,h2,h3{font-family:Spectral,Georgia,"Times New Roman",serif;font-weight:500;text-wrap:balance;margin:0;line-height:1.18;}
h1{font-size:clamp(1.9rem,4.4vw,2.9rem);letter-spacing:-.015em;}
h2{font-size:clamp(1.38rem,2.5vw,1.8rem);letter-spacing:-.01em;}
h3{font-size:1.06rem;font-weight:600;letter-spacing:-.005em;}
p{margin:0;}
a{color:var(--accent-ink);text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:2px;}
a:hover{text-decoration-thickness:2px;}
:focus-visible{outline:2px solid var(--accent);outline-offset:3px;border-radius:2px;}
.eyebrow{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:.685rem;font-weight:500;
  letter-spacing:.16em;text-transform:uppercase;color:var(--muted);}
.mono{font-family:"IBM Plex Mono",ui-monospace,monospace;font-variant-numeric:tabular-nums;}

header.masthead{border-bottom:1px solid var(--line);background:var(--surface);padding:clamp(34px,6vw,60px) 0 0;}
.masthead .wrap{display:flex;flex-direction:column;gap:20px;}
.mast-top{display:flex;flex-direction:column;gap:13px;}
.mast-top h1{max-width:20ch;}
.mast-lede{font-size:1.04rem;color:var(--ink-2);max-width:66ch;}
.mast-meta{display:flex;flex-wrap:wrap;gap:0;border-top:1px solid var(--line);margin-top:6px;}
.mast-meta div{flex:1 1 200px;padding:14px 22px 16px 0;display:flex;flex-direction:column;gap:3px;}
.mast-meta dt{font-family:"IBM Plex Mono",monospace;font-size:.66rem;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);}
.mast-meta dd{margin:0;font-size:.88rem;color:var(--ink-2);}

.figures{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--line);margin-top:4px;}
@media (max-width:820px){.figures{grid-template-columns:repeat(2,1fr);}}
.fig{padding:22px 20px 26px;border-right:1px solid var(--line);display:flex;flex-direction:column;gap:5px;}
.fig:last-child{border-right:0;}
@media (max-width:820px){.fig:nth-child(2n){border-right:0;}.fig:nth-child(-n+2){border-bottom:1px solid var(--line);}}
.fig .num{font-family:Spectral,serif;font-size:2.2rem;line-height:1;font-variant-numeric:tabular-nums;letter-spacing:-.02em;}
.fig .num small{font-size:.9rem;font-family:"IBM Plex Sans",sans-serif;color:var(--muted);margin-left:3px;letter-spacing:0;}
.fig .cap{font-size:.82rem;color:var(--muted);line-height:1.4;}
.fig.good .num{color:var(--accent);}
.fig.bad .num{color:var(--warn);}

section{padding:clamp(42px,5.5vw,68px) 0;border-bottom:1px solid var(--line);}
.sec-head{display:flex;flex-direction:column;gap:10px;margin-bottom:28px;max-width:74ch;}
.sec-head p{color:var(--ink-2);}
.grid-2{display:grid;grid-template-columns:1fr 1fr;gap:32px;}
.grid-2 > *{min-width:0;}
@media (max-width:800px){.grid-2{grid-template-columns:1fr;gap:24px;}}
.body-copy{display:flex;flex-direction:column;gap:16px;max-width:74ch;}
.body-copy p{color:var(--ink-2);font-size:.95rem;}
.body-copy strong{color:var(--ink);font-weight:600;}

.callout{background:var(--accent-soft);border-left:3px solid var(--accent);padding:19px 22px;
  display:flex;flex-direction:column;gap:9px;margin-top:26px;}
.callout.warn{background:var(--warn-soft);border-left-color:var(--warn);}
.callout h3{font-family:"IBM Plex Sans",sans-serif;font-size:.8rem;letter-spacing:.08em;
  text-transform:uppercase;color:var(--accent-ink);}
.callout.warn h3{color:var(--warn);}
.callout p{font-size:.9rem;color:var(--ink-2);}

.tablewrap{overflow-x:auto;margin-top:30px;}
table{border-collapse:collapse;width:100%;min-width:560px;font-size:.855rem;}
caption{text-align:left;font-family:"IBM Plex Mono",monospace;font-size:.68rem;letter-spacing:.14em;
  text-transform:uppercase;color:var(--muted);padding-bottom:11px;}
th{text-align:left;font-weight:600;font-size:.71rem;letter-spacing:.06em;text-transform:uppercase;
  color:var(--muted);padding:0 14px 9px 0;border-bottom:1px solid var(--line-strong);vertical-align:bottom;}
td{padding:10px 14px 10px 0;border-bottom:1px solid var(--line);vertical-align:top;color:var(--ink-2);}
td:first-child,th:first-child{padding-left:0;}
td.num,th.num{text-align:right;padding-right:18px;font-variant-numeric:tabular-nums;}
td.num{font-family:"IBM Plex Mono",monospace;color:var(--ink);}
tr.hi td{background:var(--accent-soft);}
tr.hi td:first-child{box-shadow:inset 3px 0 0 var(--accent);padding-left:11px;}
tr.dim td{color:var(--muted);}
.chip{display:inline-block;font-family:"IBM Plex Mono",monospace;font-size:.66rem;padding:2px 7px;
  border:1px solid var(--line-strong);color:var(--muted);white-space:nowrap;}
.chip.good{border-color:var(--accent);color:var(--accent-ink);background:var(--accent-soft);}
.chip.risk{border-color:var(--warn);color:var(--warn);background:var(--warn-soft);}

ul.plain{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:14px;}
ul.plain li{display:grid;grid-template-columns:26px 1fr;gap:12px;font-size:.92rem;color:var(--ink-2);}
ul.plain li .n{font-family:"IBM Plex Mono",monospace;font-size:.72rem;font-weight:600;color:var(--accent);padding-top:3px;}
ul.plain li strong{color:var(--ink);font-weight:600;}

.flow{display:flex;flex-direction:column;gap:0;margin-top:26px;}
.flow-step{border:1px solid var(--line);background:var(--surface);padding:17px 20px;
  display:grid;grid-template-columns:76px 1fr;gap:16px;align-items:start;}
.flow-step + .flow-step{border-top:0;}
.flow-step .ph{font-family:"IBM Plex Mono",monospace;font-size:.68rem;letter-spacing:.1em;
  text-transform:uppercase;color:var(--accent);padding-top:2px;}
.flow-step p{font-size:.9rem;color:var(--ink-2);}
.flow-step strong{color:var(--ink);font-weight:600;}

figure{margin:30px 0 0;border:1px solid var(--line);background:var(--surface);box-shadow:var(--shadow);}
figure .chartwrap{overflow-x:auto;padding:16px 18px 6px;}
figcaption{font-size:.82rem;color:var(--muted);padding:0 18px 16px;line-height:1.5;border-top:1px solid var(--line);padding-top:13px;margin-top:6px;}
figcaption b{color:var(--ink-2);font-weight:600;}
svg.chart{display:block;width:100%;min-width:640px;height:auto;font-family:"IBM Plex Sans",sans-serif;}
svg.chart .grid{stroke:var(--line);stroke-width:1;}
svg.chart .ref{stroke:var(--line-strong);stroke-width:1.5;stroke-dasharray:4 4;}
svg.chart .band{fill:var(--accent-soft);}
svg.chart .tick{font-size:11px;fill:var(--muted);font-variant-numeric:tabular-nums;}
svg.chart .axis{font-size:11.5px;fill:var(--muted);}
svg.chart .rowlbl{font-size:12px;fill:var(--ink-2);}
svg.chart .dlbl{font-size:12px;font-weight:600;font-variant-numeric:tabular-nums;}
svg.chart .lbl-ann{font-size:11px;fill:var(--muted);font-variant-numeric:tabular-nums;}
svg.chart .mid{text-anchor:middle;}
svg.chart .end{text-anchor:end;}
svg.chart .line{fill:none;stroke-width:2;stroke-linejoin:round;stroke-linecap:round;}
svg.chart .fill{fill-opacity:.14;stroke:none;}
svg.chart .bar{stroke:var(--surface);stroke-width:2;}
svg.chart .rng{stroke-width:2.5;stroke-linecap:round;}
svg.chart .dot{stroke:var(--surface);stroke-width:2;}
svg.chart .dot-base{stroke:var(--surface);stroke-width:2.5;}
svg.chart .halo{fill:none;stroke:var(--accent);stroke-width:2;}
svg.chart .hit{fill:transparent;}
svg.chart .neutral{stroke:var(--muted);}
svg.chart circle.neutral{fill:var(--muted);}
svg.chart .s1{stroke:var(--s1);}   svg.chart text.s1{fill:var(--s1);stroke:none;}
svg.chart .s2{stroke:var(--s2);}   svg.chart text.s2{fill:var(--s2);stroke:none;}
svg.chart .s3{stroke:var(--s3);}   svg.chart text.s3{fill:var(--s3);stroke:none;}
svg.chart circle.s1,svg.chart rect.s1,svg.chart polygon.s1{fill:var(--s1);}
svg.chart circle.s2,svg.chart rect.s2,svg.chart polygon.s2{fill:var(--s2);}
svg.chart circle.s3,svg.chart rect.s3,svg.chart polygon.s3{fill:var(--s3);}
svg.chart polygon.fill.s1{fill:var(--s1);stroke:none;}

.refs{display:flex;flex-direction:column;}
.refgroup{border-top:1px solid var(--line);padding:18px 0 20px;}
.refgroup h3{font-family:"IBM Plex Sans",sans-serif;font-size:.72rem;letter-spacing:.14em;
  text-transform:uppercase;color:var(--muted);margin-bottom:12px;font-weight:600;}
.refgroup ol{margin:0;padding-left:1.15em;display:flex;flex-direction:column;gap:9px;}
.refgroup li{font-size:.84rem;color:var(--ink-2);line-height:1.5;}
footer{padding:32px 0 50px;font-size:.8rem;color:var(--muted);}
footer .wrap{display:flex;flex-direction:column;gap:9px;}
.themebtn{position:fixed;right:16px;bottom:16px;z-index:9;background:var(--surface);
  border:1px solid var(--line-strong);color:var(--ink-2);font-family:"IBM Plex Mono",monospace;
  font-size:.7rem;letter-spacing:.08em;text-transform:uppercase;padding:9px 13px;cursor:pointer;
  box-shadow:var(--shadow);}
.themebtn:hover{background:var(--surface-2);}
@media print{.themebtn{display:none;}section{break-inside:avoid;}}
@media (prefers-reduced-motion: reduce){*{transition:none !important;animation:none !important;}}

svg.chart .connector{stroke:var(--line-strong);stroke-width:1;stroke-dasharray:3 3;}
"""

def tbl(caption, head, rows, cls=""):
    o = [f'<div class="tablewrap"><table class="{cls}">',
         f'<caption>{caption}</caption>', "<thead><tr>"]
    for h, num in head:
        o.append(f'<th class="num">{h}</th>' if num else f"<th>{h}</th>")
    o.append("</tr></thead><tbody>")
    for r in rows:
        rc = ""
        cells = list(r)
        if cells and isinstance(cells[0], str) and cells[0].startswith("@"):
            rc = cells.pop(0)[1:]
        o.append(f'<tr class="{rc}">' if rc else "<tr>")
        for i, c in enumerate(cells):
            o.append(f'<td class="num">{c}</td>' if head[i][1] else f"<td>{c}</td>")
        o.append("</tr>")
    o.append("</tbody></table></div>")
    return "\n".join(o)

