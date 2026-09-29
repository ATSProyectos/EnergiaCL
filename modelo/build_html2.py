"""Genera docs/escenarios-y-hoja-de-ruta-sqm.html"""
import os
from _style import CSS, tbl
S = os.path.dirname(os.path.abspath(__file__))
fig4 = open(f"{S}/fig4.svg").read()
fig5 = open(f"{S}/fig5.svg").read()

T_BAL = tbl("Reconciliación del balance energético en autoconsumo puro",
 [("Supuesto",0),("Déficit",1),("Vertimiento",1)],
 [["220 GWh · consumo plano 19,0 MW · BESS 320 MWh / <strong>20 MW</strong>","23,8 GWh","68,5 GWh"],
  ["220 GWh · consumo plano 20,0 MW · BESS 320 MWh / <strong>20 MW</strong>","29,0","64,9"],
  ["@hi","220 GWh · consumo plano 19,0 MW · BESS 320 MWh / <strong>70 MW</strong>","<strong>1,4</strong>","43,0"],
  ["@hi","207 GWh · consumo real variable · BESS 320 MWh / <strong>30 MW</strong>","<strong>5,2</strong>","34,3"],
  ["170 GWh (DIA) · consumo real variable · BESS 320 MWh / 20 MW","27,5","22,5"]])

T_DESC = tbl("Descomposición sobre configuración idéntica · 76,5 MWp seguidor + 150 MWh/30 MW, base",
 [("US$ M/año",0),("A · Autoconsumo puro",1),("B · SGC coordinado",1),("C · PPA tradicional",1)],
 [["Costo de capital","8,83","8,83","8,83"],
  ["OPEX","2,97","3,19","3,19"],
  ["Peajes sobre energía servida en sitio","0,00","0,00","<strong>1,85</strong>"],
  ["(−) Margen de mercado","−3,89","+0,09","+0,09"],
  ["(−) Potencia de suficiencia","0,00","<strong>3,66</strong>","<strong>3,66</strong>"],
  ["(−) Servicios complementarios","0,00","<strong>0,60</strong>","<strong>0,60</strong>"],
  ["@hi","<strong>Costo de servir · USD/MWh</strong>","<strong>94,2</strong>","<strong>46,1</strong>","<strong>57,3</strong>"],
  ["Vertimiento","75,1 GWh","0","0"]])

T_COMP = tbl("De autoconsumo puro a SGC coordinado: 48,1 USD/MWh",
 [("Componente",0),("USD/MWh",1)],
 [["Margen de mercado por poder inyectar excedentes en vez de verterlos","23,9"],
  ["Potencia de suficiencia reconocida al BESS","22,0"],
  ["Servicios complementarios","3,6"],
  ["(−) Mayor OPEX por mayor ciclado","−1,4"],
  ["@hi","<strong>Total</strong>","<strong>48,1</strong>"]])

T_MERCH = tbl("El activo valorizado como planta merchant, sin PPA con SQM",
 [("Configuración",0),("CAPEX",1),("EBITDA",1),("Yield",1),("VAN 25 años",1)],
 [["76,5 MWp sin BESS","67,3 M","2,60 M","3,9%","<strong>−37,0 M</strong>"],
  ["@hi","76,5 MWp + 150 MWh / 30 MW","92,7 M","9,57 M","10,3%","<strong>+18,8 M</strong>"],
  ["76,5 MWp + 320 MWh / 20 MW <em>(diseño SQM)</em>","117,0 M","7,33 M","6,3%","<strong>−31,5 M</strong>"],
  ["76,5 MWp + 320 MWh / 30 MW","118,0 M","9,92 M","8,4%","−2,4 M"]])

T_MATRIZ = tbl("Matriz de escenarios — costo de servir el bloque 24/7 (166,4 GWh/año)",
 [("",0),("Escenario",0),("Conserv.",1),("Base",1),("Optim.",1),("CAPEX",1),("Autosuf.",1),("Vertido",1)],
 [["<strong>D0</strong>","Diseño SQM tal cual — fija, 320 MWh/20 MW, aislado","111,7","109,7","108,0","111,2 M","74,8%","38,3 GWh"],
  ["<strong>E1</strong>","Autoconsumo puro — SQM propietario, sin inyección · <em>240 MWh/30 MW</em>","90,9","90,1","89,4","106,1 M","92,3%","43,0 GWh"],
  ["<strong>E3</strong>","PPA tradicional — GR propietario, sin beneficio de peaje · <em>150 MWh/30 MW</em>","66,3","57,3","52,0","92,7 M","61,9%","0"],
  ["@hi","<strong>E2</strong>","<strong>SGC coordinado — con inyección y beneficio de peaje · <em>150 MWh/30 MW</em></strong>","<strong>54,7</strong>","<strong>46,1</strong>","<strong>41,3</strong>","92,7 M","61,9%","0"]])

T_PRECIO = tbl("Precio ofertable y margen — anclado en el escenario conservador",
 [("",0),("Piso conservador",1),("PPA sugerido",1),("Ahorro SQM",1),("Margen GR",1),("VAN 15 años",1)],
 [["@dim","<strong>D0</strong>","111,7","—","—","—","—"],
  ["<strong>E1</strong>","90,9","~100","0%","1,65 M","15,0 M"],
  ["<strong>E3</strong>","66,3","<strong>72</strong>","28%","2,45 M","22,4 M"],
  ["@hi","<strong>E2</strong>","<strong>54,7</strong>","<strong>65</strong>","<strong>35%</strong>","<strong>3,14 M</strong>","<strong>28,6 M</strong>"]])

T_LEGAL = tbl("Las preguntas legales que deciden la operación",
 [("#",0),("Pregunta",0),("Qué está en juego",0)],
 [["@hi","<strong>L1</strong>","¿El SGC admite que la generación y el consumo tengan <strong>propietarios distintos</strong>, o exige «generación propia» en sentido estricto?","<strong>Decide la estructura completa.</strong> Si exige mismo propietario, GR no puede ser dueño del activo y conservar el beneficio"],
  ["<strong>L2</strong>","Si exige mismo propietario, ¿el <strong>mandato/contrato</strong> de la minuta es suficiente? ¿Arriendo, usufructo, comodato, mandato de operación?","11 USD/MWh + viabilidad de la compra"],
  ["<strong>L3</strong>","¿La restricción de «consumo existente sin ampliaciones» alcanza al <strong>SGC</strong> o sólo al autoconsumo?","Elegibilidad de E2"],
  ["@hi","<strong>L4</strong>","¿Qué reconocimiento de <strong>potencia de suficiencia</strong> obtiene un BESS dentro de un SGC, y con qué criterio de bloque de punta?","<strong>22,0 USD/MWh</strong> — el componente individual más grande"],
  ["<strong>L5</strong>","¿Puede un SGC participar del mercado de <strong>servicios complementarios</strong>?","3,6 USD/MWh"],
  ["<strong>L6</strong>","¿Qué capacidad de inyección admite el punto de seccionamiento en 66 kV, y qué se requiere para llevarla a ≥ 25 MW?","43,6 USD/MWh (el salto de 0 a inyectar)"]])

T_A = tbl("Etapa A — Cierre técnico y legal (semanas 1–3)",
 [("#",0),("Acción",0),("Responsable",0),("Entregable",0)],
 [["A1","Responder L1–L3 sobre la base del reglamento que compartirá Cata","Cata + J. Vergara","Memo legal de una página"],
  ["A2","Consultar informalmente a CNE/CEN sobre L4 y L5","Regulación","Lectura preliminar del reconocimiento de potencia"],
  ["A3","Cerrar las tres cifras discrepantes: rendimiento, POI, potencia del BESS","N. Machuca / M. Aguilera","Ficha técnica única de referencia"],
  ["A4","Verificar capacidad de inyección real de la LT 66 kV (L6)","Ingeniería / Conexiones","Capacidad máxima y obras requeridas"],
  ["A5","Validar precio de transferencia de GR Power para el bloque de respaldo","J. Friedl / J. Álvarez","Precio interno por bloque horario"],
  ["A6","Contrastar el CAPEX del modelo contra cotizaciones vigentes de EPC y BESS","Ingeniería","Rango de CAPEX validado"]])

T_SEC = tbl("La secuencia recomendada para la reunión con SQM",
 [("Paso",0),("Mensaje",0),("Por qué en esta posición",0)],
 [["<strong>1 · Validación</strong>","«Modelamos su proyecto de forma independiente y nos da 169,9 GWh contra sus 170, y US$ 111,2 M contra sus US$ 111 M»","Construye credibilidad técnica antes de cualquier crítica. No cuesta nada y cambia el tono"],
  ["@hi","<strong>2 · El hallazgo técnico</strong>","«El limitante no es la energía almacenada, es la potencia de descarga. Con 30 MW en vez de 20, el déficit cae de 24 a 5 GWh por US$ 0,95 M»","Es un regalo: barato, verificable, y mejora <em>su</em> proyecto sea quien sea el dueño"],
  ["@hi","<strong>3 · El problema compartido</strong>","«El derecho a inyectar y coordinar vale unos 44 USD/MWh. Sin él, ningún dimensionamiento hace competitivo el proyecto»","Alinea intereses: ambos quieren que el activo valga más. Aquí se propone la estrategia regulatoria conjunta"],
  ["<strong>4 · La oferta</strong>","«Con esos dos ajustes podemos ofrecerles un PPA 24/7 a X USD/MWh, un tercio bajo lo que pagan hoy»","Llega después de haber demostrado competencia y aportado valor"],
  ["<strong>5 · La estructura</strong>","Las opciones de propiedad y las condiciones","Es lo único puramente distributivo. Va al final"]])

T_RIESGO = tbl("Riesgos añadidos a la matriz del documento anterior",
 [("Riesgo",0),("Exposición",0),("Mitigante",0)],
 [["<strong>El SGC exige mismo propietario y el mandato no resiste el escrutinio regulatorio</strong>","<span class='chip risk'>existencial</span> para la compra del activo","Plan B: no comprar; competir por el PPA desde cartera. Resolver L1–L2 antes de cualquier oferta"],
  ["<strong>El reconocimiento de potencia del BESS en un SGC es menor al supuesto</strong>","<span class='chip risk'>alto</span> 22,0 USD/MWh","El escenario conservador ya asume 6,5 USD/kW-mes. Consulta informal al CEN antes de ofertar"],
  ["<strong>El reglamento de autoconsumo bloquea también al SGC</strong>","<span class='chip'>medio</span> elimina E1 y E2","E3 sigue siendo ofertable a 72 con 28% de ahorro"],
  ["<strong>SQM no acepta rediseñar y exige el proyecto tal como está</strong>","<span class='chip risk'>alto</span> D0 no es ofertable","Presentar el benchmark de mercado y el hallazgo de potencia. Si aun así no cede, retirarse de la compra"],
  ["<strong>La adenda se presenta sin flexibilidad de diseño</strong>","<span class='chip'>medio</span> obliga a modificar la RCA después","Pedido explícito en la próxima reunión, por escrito"]])

T_CAMBIA = tbl("Qué aporta la minuta del 29-sep-2026",
 [("Aporte",0),("Consecuencia sobre el análisis",0)],
 [["La figura de autoconsumo <strong>exige mismo propietario</strong>, o estructurarse vía mandato/contrato","Invalida la estructura propuesta en §3 del documento anterior (GR compra y es propietario) si se quiere conservar el beneficio de autoconsumo"],
  ["El reglamento <strong>busca impedir que grandes clientes usen la figura para alimentar consumo existente</strong>; las proyecciones de SQM 2026–2027 no muestran crecimiento","El riesgo no es de precio, es de <strong>elegibilidad</strong>. Rodrigo ya fue advertido"],
  ["El caso Data Center evalúa <strong>tres</strong> alternativas: SGC, PPA tradicional y autoconsumo","Da el marco correcto: son tres vehículos distintos, no dos configuraciones"]])

BODY = f"""
<header class="masthead">
 <div class="wrap">
  <div class="mast-top">
   <span class="eyebrow">Grenergy · documento de trabajo · complementa la propuesta SQM</span>
   <h1>Escenarios y hoja de ruta — PPA SQM Nueva Victoria</h1>
   <p class="mast-lede">Incorpora la reunión interna del 29 de septiembre. El hallazgo que reordena
   la discusión: <strong>el derecho a inyectar y coordinar vale cuatro veces más que la figura de
   autoconsumo</strong>, y la preocupación regulatoria de la reunión apunta al vehículo menos
   valioso de los tres.</p>
  </div>
  <dl class="mast-meta">
   <div><dt>Minuta</dt><dd>29-sep-2026 · Cata, Nico, Rodrigo, Juan</dd></div>
   <div><dt>Vehículo recomendado</dt><dd>SGC · plan B: PPA tradicional coordinado</dd></div>
   <div><dt>Camino crítico</dt><dd>Memo legal L1–L6 (Cata + J. Vergara)</dd></div>
   <div><dt>Versión</dt><dd>1.0 · septiembre de 2026</dd></div>
  </dl>
 </div>
 <div class="wrap">
  <div class="figures">
   <div class="fig good"><span class="num">44<small>USD/MWh</small></span>
     <span class="cap">Vale el derecho a inyectar y coordinar con el CEN</span></div>
   <div class="fig"><span class="num">11<small>USD/MWh</small></span>
     <span class="cap">Vale la figura de autoconsumo: cuatro veces menos</span></div>
   <div class="fig bad"><span class="num">−31<small>M USD</small></span>
     <span class="cap">VAN del activo como planta merchant sin PPA: el vehículo es el negocio</span></div>
   <div class="fig good"><span class="num">0,95<small>M USD</small></span>
     <span class="cap">Cuesta subir el BESS de 20 a 30 MW. Ahorra US$ 2,6 M al año</span></div>
  </div>
 </div>
</header>

<main>

<section id="cambia">
 <div class="wrap">
  <div class="sec-head">
   <span class="eyebrow">01 · Qué cambia</span>
   <h2>El vehículo regulatorio no es un detalle de implementación</h2>
   <p>La minuta introduce un eje que el análisis previo no tenía. Es la variable que más mueve el
   precio — más que el dimensionamiento del BESS, más que el CAPEX, más que el WACC.</p>
  </div>
  {T_CAMBIA}
  <div class="callout">
   <h3>Estado de los acuerdos de la minuta</h3>
   <p>El acuerdo n.° 3 —calcular CAPEX y OPEX para determinar el LCOE y definir la tarifa de PPA
   competitiva— es exactamente lo que entrega el documento anterior. Este documento cierra el
   acuerdo n.° 2: integrar el análisis legal y decidir el vehículo. Queda pendiente el n.° 1,
   el envío de la sección del reglamento por parte de Cata, que está en el camino crítico.</p>
  </div>
 </div>
</section>

<section id="hallazgo1">
 <div class="wrap">
  <div class="sec-head">
   <span class="eyebrow">02 · Hallazgo</span>
   <h2>El déficit de 9 GWh no se sostiene con un BESS de 20 MW</h2>
   <p>La minuta registra un déficit estimado de 9 GWh/año. Al reproducir ese balance en el modelo
   horario, ese número sólo aparece si la batería descarga muy por encima de los 20 MW de la DIA.</p>
  </div>
  {T_BAL}
  <div class="callout warn">
   <h3>El diagnóstico correcto</h3>
   <p>El déficit bajo de la simulación previa es consistente con la nota «Potencia de Retiro del BESS
   (70 MW)» de la lámina <em>Generación Estimada PV+BESS – Industria TEA</em>, <strong>no</strong> con
   los «20 MW durante 16 horas continuas» que declara la DIA.</p>
   <p><strong>El problema del diseño de SQM no es que sobre energía almacenada: es que falta potencia
   de descarga.</strong> El proyecto es rico en energía y pobre en potencia, exactamente al revés de
   lo que conviene.</p>
  </div>
  <div class="body-copy" style="margin-top:22px;">
   <p>Y la corrección es barata. Subir el BESS de 20 a 30 MW manteniendo los 320 MWh cuesta
   ≈ <strong>US$ 0,95 M</strong> adicionales de conversión y reduce el costo de servir de 74,1 a
   58,5 USD/MWh — unos <strong>US$ 2,6 M al año</strong>. Payback inferior a cinco meses. Es la
   mejora de mejor relación costo-beneficio de todo el rediseño y, a diferencia del resto,
   no exige discutir el tamaño de la batería con SQM.</p>
  </div>
 </div>
</section>

<section id="hallazgo2">
 <div class="wrap">
  <div class="sec-head">
   <span class="eyebrow">03 · Hallazgo</span>
   <h2>Coordinar vale cuatro veces más que el autoconsumo</h2>
  </div>
  {T_DESC}
  <figure>
   <div class="chartwrap">{fig4}</div>
   <figcaption><b>De dónde viene cada diferencia.</b> Sobre configuración idéntica (76,5 MWp con
   seguidor + 150 MWh/30 MW, escenario base). Las barras claras son los componentes; las sólidas,
   los tres vehículos. <b>En verde</b> lo que reduce el costo, <b>en naranja</b> lo que lo
   aumenta.</figcaption>
  </figure>
  {T_COMP}
  <div class="callout">
   <h3>Esto invierte la prioridad regulatoria de la reunión</h3>
   <p>La preocupación de la minuta fue si la figura de autoconsumo es elegible. Los números dicen que
   el autoconsumo es el vehículo <strong>menos</strong> valioso de los tres: un PPA tradicional con
   GR propietario, sin ningún beneficio de autoconsumo pero coordinado con el CEN, es
   <strong>33 USD/MWh más barato</strong> que un autoconsumo puro perfectamente elegible.
   <strong>Lo que hay que pelear es el derecho a inyectar y coordinar</strong>, no la figura de
   autoconsumo.</p>
   <p>La conclusión resiste el escenario conservador, que castiga justamente los dos componentes
   mayores —compresión de spreads y caída del precio de potencia—: E1 queda en 90,9 y E2 en 54,7,
   una brecha que sigue siendo de 36 USD/MWh.</p>
  </div>
 </div>
</section>

<section id="hallazgo3">
 <div class="wrap">
  <div class="sec-head">
   <span class="eyebrow">04 · Hallazgo</span>
   <h2>El activo no se sostiene solo: el vehículo <em>es</em> el negocio</h2>
   <p>Valorizado como planta merchant, sin PPA con SQM, con toda la energía al sistema.</p>
  </div>
  {T_MERCH}
  <div class="body-copy" style="margin-top:22px;">
   <p>Por escenario, para la configuración optimizada: VAN de <strong>−15,0 M</strong> (conservador),
   <strong>+18,8 M</strong> (base), <strong>+47,9 M</strong> (optimista).</p>
  </div>
  <div class="callout warn">
   <h3>Corolario para la negociación</h3>
   <p><strong>Comprar Nueva Victoria como activo merchant no se sostiene.</strong> Sólo el caso base
   da VAN positivo y el conservador lo destruye. El valor del activo para GR está en el PPA con SQM,
   no en el mercado spot. Por lo tanto la pregunta del vehículo no es una condición de borde del
   negocio: <strong>es el negocio</strong>.</p>
   <p>De ahí que la opción de <strong>desacoplar</strong> —comprar el activo como planta de cartera y
   venderle a SQM un PPA desde el portafolio de GR Power— no sea una alternativa de repliegue
   atractiva. Si el vehículo falla, lo razonable es <strong>no comprar el activo</strong> y competir
   por el PPA de SQM desde la cartera existente (Oasis de Atacama / Elena), donde GR ya tiene costo
   marginal.</p>
  </div>
 </div>
</section>

<section id="matriz">
 <div class="wrap">
  <div class="sec-head">
   <span class="eyebrow">05 · Escenarios</span>
   <h2>La matriz de decisión</h2>
   <p>Cada escenario con su configuración óptima, porque <strong>el óptimo del BESS depende del
   vehículo</strong>.</p>
  </div>
  {T_MATRIZ}
  <figure>
   <div class="chartwrap">{fig5}</div>
   <figcaption><b>Costo de servir por vehículo regulatorio.</b> El punto marca el escenario base;
   la línea, el rango entre conservador y optimista. La referencia punteada en 100 USD/MWh es lo que
   SQM paga hoy. <b>D0 y E1 quedan sobre o junto a esa línea: no son ofertables.</b> El rango casi
   nulo de E1 no es un error: al no participar del mercado, es el único escenario indiferente a
   cómo evolucionen los precios.</figcaption>
  </figure>
  <div class="callout">
   <h3>El óptimo del almacenamiento cambia con el vehículo</h3>
   <p>Con derecho de inyección el óptimo son <strong>4–6 horas</strong> (150 MWh/30 MW); sin derecho
   de inyección se desplaza a <strong>8 horas</strong> (240 MWh/30 MW), porque el excedente que no se
   puede vender conviene almacenarlo. En ningún vehículo el óptimo se acerca a las 16 horas del
   diseño actual.</p>
  </div>
  {T_PRECIO}
  <div class="callout warn">
   <h3>D0 y E1 no son ofertables</h3>
   <p>D0 cuesta más que la tarifa actual del cliente. E1 tiene un piso conservador de 90,9: cualquier
   margen razonable lo deja en el entorno de lo que SQM ya paga, con lo cual la operación pierde su
   razón de ser para ambas partes.</p>
  </div>
 </div>
</section>

<section id="estrategia">
 <div class="wrap">
  <div class="sec-head">
   <span class="eyebrow">06 · Estrategia</span>
   <h2>Perseguir el SGC, no el autoconsumo</h2>
  </div>
  <div class="body-copy">
   <p><strong>Vehículo primario: SGC (sistema de generación-consumo). Plan B: PPA tradicional
   coordinado. Tratar el autoconsumo como lo que es —un beneficio marginal de 11 USD/MWh— y no
   condicionar la estructura de la operación a conseguirlo.</strong></p>
  </div>
  <ul class="plain" style="margin-top:20px;">
   <li><span class="n">01</span><span>El DS 32/2026 crea expresamente la figura de sistemas de
     generación-consumo para «complejos productivos que combinan proceso industrial, generación
     propia y almacenamiento». <strong>Es la figura diseñada para este caso.</strong></span></li>
   <li><span class="n">02</span><span>La restricción que preocupa a la reunión —impedir alimentar
     consumo existente sin ampliaciones reales— es una restricción del reglamento de
     <strong>autoconsumo</strong>. Hay que verificar si alcanza también al SGC; si no alcanza, el
     problema de elegibilidad desaparece.</span></li>
   <li><span class="n">03</span><span>Aun en el peor caso —ningún beneficio de peaje, GR propietario,
     PPA tradicional— el proyecto coordinado sirve a 57,3 USD/MWh y es ofertable a 72 con
     28% de ahorro para SQM.</span></li>
  </ul>
  {T_LEGAL}
  <div class="callout warn">
   <h3>L1 y L4 concentran el riesgo</h3>
   <p>Hasta que <strong>L1</strong> esté respondida no se puede definir la estructura de la
   operación, y hasta que <strong>L4</strong> esté respondida el precio ofertable tiene una
   incertidumbre de ±22 USD/MWh. Ninguna de las dos se resuelve con más modelación.</p>
  </div>
 </div>
</section>

<section id="interna">
 <div class="wrap">
  <div class="sec-head">
   <span class="eyebrow">07 · Hoja de ruta interna</span>
   <h2>Del memo legal al mandato de negociación</h2>
  </div>
  {T_A}
  <h3 style="margin-top:34px;">Etapa B — Decisión interna (semana 4)</h3>
  <div class="body-copy" style="margin-top:12px;">
   <p>Comité con Rodrigo, Juan, Cata y el equipo de desarrollo. Tres decisiones, en este orden:</p>
  </div>
  <div class="flow">
   <div class="flow-step"><span class="ph">Uno</span>
     <p><strong>Vehículo.</strong> SGC, PPA tradicional, o no avanzar. Determinado por A1–A2.</p></div>
   <div class="flow-step"><span class="ph">Dos</span>
     <p><strong>Estructura de propiedad.</strong> Compra del activo, mandato, o sólo PPA desde
     cartera. Determinada por la anterior.</p></div>
   <div class="flow-step"><span class="ph">Tres</span>
     <p><strong>Mandato de negociación.</strong> Precio piso, precio objetivo, y hasta dónde se puede
     ceder en configuración técnica.</p></div>
  </div>
  <div class="callout">
   <h3>Regla de decisión sugerida</h3>
   <p>Si <strong>L1 permite propiedad de terceros bajo SGC</strong> → comprar el activo y estructurar
   E2. Si <strong>L1 exige mismo propietario y L2 no ofrece un vehículo contractual sólido</strong> →
   no comprar el activo; ofrecer a SQM el rol de desarrollador, EPC y O&amp;M más un PPA desde
   cartera, y competir por el suministro sin inmovilizar capital.</p>
  </div>
  <h3 style="margin-top:34px;">Etapa C — Preparación del material (semana 5)</h3>
  <div class="body-copy" style="margin-top:12px;">
   <p>Cinco láminas, una por paso de la conversación: validación, hallazgo de potencia, valor de
   inyectar, oferta, estructura.</p>
  </div>
 </div>
</section>

<section id="sqm">
 <div class="wrap">
  <div class="sec-head">
   <span class="eyebrow">08 · Hoja de ruta con SQM</span>
   <h2>El orden de la conversación importa</h2>
   <p>La secuencia natural —«compramos su proyecto, pero antes hay que rediseñarlo»— pone tres
   pedidos sobre la mesa al mismo tiempo y activa la defensa del proyecto. Esta secuencia separa lo
   que es de interés común de lo que es negociación.</p>
  </div>
  {T_SEC}

  <div class="grid-2" style="margin-top:34px;">
   <div class="body-copy">
    <h3>Mostrar</h3>
    <ul style="margin:8px 0 0;padding-left:1.2em;display:flex;flex-direction:column;gap:8px;font-size:.9rem;color:var(--ink-2);">
     <li>La validación de generación y CAPEX</li>
     <li>El benchmark de duración de almacenamiento (Sonnedix/Copec 5,5 h, Atlas/COPEC 4 h, el caso
     minero de 4 h). <strong>Es el argumento más fuerte y no es nuestro: es el mercado</strong></li>
     <li>La curva de optimización del BESS, sin los costos de GR</li>
     <li>El precio ofertable y el ahorro para SQM</li>
    </ul>
   </div>
   <div class="body-copy">
    <h3>No mostrar</h3>
    <ul style="margin:8px 0 0;padding-left:1.2em;display:flex;flex-direction:column;gap:8px;font-size:.9rem;color:var(--ink-2);">
     <li>El costo de servir de GR ni el margen</li>
     <li>El VAN de la operación ni la valorización del activo</li>
     <li>La descomposición de dónde viene el valor de coordinar — se comunica el resultado
     (44 USD/MWh), no el desglose entre potencia, SSCC y arbitraje, que es información comercial
     de GR</li>
    </ul>
   </div>
  </div>

  <div class="callout">
   <h3>Qué pedirle a SQM en esta reunión</h3>
   <p>Además de la información del §10 del documento anterior, <strong>dos pedidos concretos y de
   bajo costo para ellos</strong>: (i) <strong>introducir flexibilidad de diseño en la adenda que
   están preparando ahora</strong> —rango de potencia del BESS, estructura con seguidores, capacidad
   de inyección ampliada—, antes de la RCA; y (ii) <strong>abordar conjuntamente la estrategia
   regulatoria del vehículo</strong> ante CNE y CEN. GR aporta el equipo de regulación; SQM aporta la
   titularidad y el consumo.</p>
  </div>

  <div class="callout warn">
   <h3>El punto de quiebre a anticipar</h3>
   <p>SQM presentó su proyecto al SEA como abastecimiento de sus instalaciones, y sus proyecciones
   2026–2027 no muestran crecimiento. Si el reglamento de autoconsumo efectivamente les impide usar
   la figura sobre consumo existente, <strong>SQM tiene un problema con o sin Grenergy</strong>, y su
   proyecto pierde buena parte de su justificación económica.</p>
   <p>Ese es el momento en que la conversación cambia de «nos quieren comprar el proyecto» a «nos
   traen la salida». Conviene llegar con la respuesta preparada —la ruta SGC, el rediseño y el PPA—
   y <strong>reservarla para cuando ellos planteen la dificultad, no antes</strong>.</p>
  </div>
 </div>
</section>

<section id="riesgos">
 <div class="wrap">
  <div class="sec-head">
   <span class="eyebrow">09 · Riesgos</span>
   <h2>Lo que se añade a la matriz anterior</h2>
  </div>
  {T_RIESGO}
 </div>
</section>

<section id="metodo">
 <div class="wrap">
  <div class="sec-head">
   <span class="eyebrow">10 · Anexo</span>
   <h2>Cómo se implementan los escenarios</h2>
  </div>
  <div class="body-copy">
   <p>Los escenarios E1, E2 y E3 se calculan con el mismo modelo horario del documento anterior. Las
   diferencias se implementan así:</p>
   <p><strong>E1 · autoconsumo puro:</strong> sin capacidad de inyección, sin participación en el
   mercado de potencia ni en servicios complementarios, sin carga del BESS desde la red. El excedente
   se vierte. Es la lectura literal de la definición de «cliente con autoconsumo» del DS 32, que
   excluye inyectar excedentes al sistema.</p>
   <p><strong>E2 · SGC coordinado:</strong> inyección hasta el límite del POI, participación en
   potencia y SSCC, peajes sólo sobre la energía importada.</p>
   <p><strong>E3 · PPA tradicional:</strong> idéntico a E2, salvo que la energía servida en sitio
   <em>también</em> paga peajes (18 USD/MWh), porque no existe figura que permita netear.</p>
  </div>
  <div class="callout warn">
   <h3>El supuesto que más pesa</h3>
   <p>La atribución de ingresos por potencia y SSCC a E2 y E3, y su exclusión de E1, explica
   <strong>25,6 de los 48,1 USD/MWh</strong> de diferencia entre E1 y E2. Ese supuesto es
   precisamente la pregunta <strong>L4–L5</strong> para Cata, y es la razón por la que el memo legal
   está en el camino crítico y <strong>no puede resolverse con más modelación</strong>.</p>
  </div>
 </div>
</section>

</main>

<footer>
 <div class="wrap">
  <p>Documento de trabajo interno de Grenergy. Complementa
  <a href="propuesta-sqm-ppa-pfv-bess.html">la propuesta SQM Nueva Victoria</a>.
  Contiene información de SQM sujeta al NDA suscrito entre las partes.</p>
  <p class="mono">Versión 1.0 · septiembre de 2026 · cifras indicativas de modelación propia, no
  constituyen oferta vinculante</p>
 </div>
</footer>

<button class="themebtn" id="themebtn" type="button" aria-label="Cambiar tema">tema</button>
<script>
(function(){{
  var b=document.getElementById("themebtn"), r=document.documentElement;
  try{{ var s=localStorage.getItem("sqm-theme"); if(s) r.setAttribute("data-theme",s); }}catch(e){{}}
  b.addEventListener("click",function(){{
    var cur=r.getAttribute("data-theme");
    var next = cur==="dark" ? "light" : (cur==="light" ? "dark"
      : (matchMedia("(prefers-color-scheme: dark)").matches ? "light" : "dark"));
    r.setAttribute("data-theme",next);
    try{{ localStorage.setItem("sqm-theme",next); }}catch(e){{}}
  }});
}})();
</script>
"""

HTML = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Escenarios PPA SQM</title>
<meta name="description" content="Escenarios de estructuración y hoja de ruta para el PPA SQM Nueva Victoria, incorporando la reunión interna del 29 de septiembre de 2026.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<style>{CSS}</style>
</head>
<body>
{BODY}
</body>
</html>"""

out = "/home/user/EnergiaCL/docs/escenarios-y-hoja-de-ruta-sqm.html"
open(out,"w").write(HTML)
print("escrito:", out, len(HTML), "bytes")
