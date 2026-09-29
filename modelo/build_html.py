import io, os
S = os.path.dirname(os.path.abspath(__file__))
fig1 = open(f"{S}/fig1.svg").read()
fig2 = open(f"{S}/fig2.svg").read()
fig3 = open(f"{S}/fig3.svg").read()
from _style import CSS, tbl

BODY = f"""
<header class="masthead">
 <div class="wrap">
  <div class="mast-top">
   <span class="eyebrow">Grenergy · Desarrollo Chile + GR Power · documento de trabajo</span>
   <h1>Adquisición del PFV&nbsp;+&nbsp;BESS de SQM en Nueva Victoria y PPA de suministro</h1>
   <p class="mast-lede">Dos alternativas de estructuración para la contraparte, con el análisis
   de LCOE que las sustenta. La conclusión central: el proyecto tal como está diseñado cuesta
   ≈&nbsp;110&nbsp;USD/MWh y no compite; redimensionado y coordinado con el sistema baja a
   ≈&nbsp;46&nbsp;USD/MWh, y esa diferencia es la que financia la operación.</p>
  </div>
  <dl class="mast-meta">
   <div><dt>Contraparte</dt><dd>SQM — Nitratos Yodo, Nueva Victoria</dd></div>
   <div><dt>Consumo contratable</dt><dd>166.170 MWh/año · 19,0 MW plano 24/7</dd></div>
   <div><dt>Activo</dt><dd>76,5 MWp + 320 MWh · US$ 111 M · RCA est. nov-2026</dd></div>
   <div><dt>Versión</dt><dd>1.0 · septiembre de 2026</dd></div>
  </dl>
 </div>
 <div class="wrap">
  <div class="figures">
   <div class="fig bad"><span class="num">110<small>USD/MWh</small></span>
     <span class="cap">Costo de servir con el diseño actual: estructura fija, BESS de 16&nbsp;h, sin inyección</span></div>
   <div class="fig good"><span class="num">46<small>USD/MWh</small></span>
     <span class="cap">Costo de servir con la configuración optimizada: seguidor, BESS de 5&nbsp;h, coordinado</span></div>
   <div class="fig"><span class="num">62–68<small>USD/MWh</small></span>
     <span class="cap">Precio PPA recomendado para ofertar a SQM (Alternativa&nbsp;2)</span></div>
   <div class="fig good"><span class="num">37<small>M USD</small></span>
     <span class="cap">VAN a 15 años con PPA de 70 USD/MWh: la bolsa para pagar el activo</span></div>
  </div>
 </div>
</header>

<main>

<section id="tesis">
 <div class="wrap">
  <div class="sec-head">
   <span class="eyebrow">01 · La tesis</span>
   <h2>Tres hallazgos que conviene fijar antes de sentarse con SQM</h2>
  </div>
  <ul class="plain">
   <li><span class="n">01</span><span><strong>El proyecto, como está diseñado, destruye valor.</strong>
     Con estructura fija, BESS de 320 MWh/20 MW (16 horas) y operación en autoconsumo puro sin
     inyección, servir el bloque 24/7 de SQM cuesta <strong>≈ 110 USD/MWh</strong> — por encima
     de lo que SQM paga hoy como cliente libre (referencia de mercado 100–107 USD/MWh). Tres fugas
     simultáneas: 38,3 GWh/año vertidos por no tener derecho de inyección, cero ingresos de potencia
     y servicios complementarios por no estar coordinado, y un BESS que cicla 173 veces al año.</span></li>
   <li><span class="n">02</span><span><strong>Tres decisiones de diseño lo transforman.</strong>
     Coordinar con el CEN en lugar de operar aislado vale <strong>−43,6 USD/MWh</strong>; redimensionar
     el almacenamiento de 16 a 4–5 horas vale <strong>−31 USD/MWh</strong>; pasar a seguidor de un eje
     vale <strong>−5 a −6 USD/MWh</strong>. Juntas llevan el costo a ≈ 46 USD/MWh en escenario base
     y ≈ 54 USD/MWh en escenario conservador.</span></li>
   <li><span class="n">03</span><span><strong>La batería de 16 horas es el error de diseño más caro.</strong>
     A partir de la sexta hora, cada hora adicional de almacenamiento <em>añade</em> costo al bloque
     completo. Las horas 11 a 16 destruyen ≈ US$ 3,4 M al año. Y ningún comparable del mercado chileno
     — Sonnedix/Copec, Atlas/COPEC, BHP/Sungrow — supera las 6 horas.</span></li>
  </ul>
  <div class="callout">
   <h3>Recomendación</h3>
   <p>Llevar la <strong>Alternativa 2</strong> (PPA híbrido optimizado, 62–68 USD/MWh) como oferta
   principal y la <strong>Alternativa 1</strong> (PPA 24/7 con BESS de 16 h, 85–92 USD/MWh) como
   opción de contraste, presentada con su sobrecosto explícito para que SQM vea el precio de la
   autonomía física. La Alternativa 2 es la única que genera bolsa suficiente para pagar el activo
   de desarrollo <em>y</em> dejar retorno incremental a GR.</p>
  </div>
 </div>
</section>

<section id="partida">
 <div class="wrap">
  <div class="sec-head">
   <span class="eyebrow">02 · Punto de partida</span>
   <h2>Qué compramos y qué abastecemos</h2>
   <p>El proyecto está en evaluación ante el SEA con PAC cerrada y primera adenda en preparación.
   El consumo a abastecer es un proceso continuo —lixiviación, yodo y yoduro— esencialmente plano,
   el perfil ideal para un PPA de bloque y el peor posible para un solar sin almacenamiento.</p>
  </div>

  {tbl("El proyecto de SQM",
       [("Elemento",0),("Dato",0),("Fuente",0)],
       [["Nombre","«Parque Fotovoltaico y Línea de Transmisión para el abastecimiento de instalaciones SQM en la Región de Tarapacá»","SEIA"],
        ["Ubicación","Pozo Almonte, provincia del Tamarugal, Región de Tarapacá","SEIA"],
        ["Potencia FV","76,5 MWp","DIA / hilo"],
        ["Generación declarada","170 GWh el primer año de operación","DIA / hilo"],
        ["Almacenamiento","320 MWh — «20 MW durante 16 horas continuas»","DIA / hilo"],
        ["Transmisión","LT 66 kV de ≈ 6,6 km + SE seccionadora sobre línea existente","SEIA"],
        ["Inversión declarada","US$ 111 M","SEIA / prensa"],
        ["Estado ambiental","PAC cerrada (6-mar a 6-abr-2026); primera adenda en preparación; RCA estimada para noviembre","Hilo, C. Pavesi 3-jul-2026"]])}

  {tbl("Consumo proyectado — Tap Off Nueva Victoria 110 kV, promedio 2026–2040",
       [("Proceso / planta",0),("MWh/año",1)],
       [["Lixiviación NV","78.289"],["Recursos Hídricos","39.148"],["Yoduro NV","22.848"],
        ["Pozas SV","20.840"],["Yodo NV","5.046"],["Iris / Porteos TEA","0"],
        ["@hi","<strong>Total</strong>","<strong>166.170</strong>"],
        ["@hi","<strong>Potencia horaria 24/7 equivalente</strong>","<strong>19,0 MW</strong>"]])}

  {tbl("Medidores 2026 — TPVITORA_220_J1_SQM, retiro de energía activa horaria",
       [("Mes",0),("Promedio MW",1),("Máximo MW",1),("Mínimo MW",1)],
       [["Enero","12,8","14,3","11,3"],["Febrero","10,7","14,1","0"],["Marzo","12,6","14,6","6,8"],
        ["Abril","13,1","22,2","10,0"],
        ["@hi","<strong>Mayo</strong>","<strong>19,6</strong>","24,9","13,8"],
        ["Junio","20,2","25,6","16,9"],
        ["@hi","Julio","20,9","<strong>31,3</strong>","15,7"],
        ["Agosto","19,7","26,3","15,6"],["Septiembre","20,1","26,9","5,2"]])}

  <div class="callout warn">
   <h3>Dos hechos que condicionan el dimensionamiento</h3>
   <p><strong>Hay un escalón estructural entre abril y mayo de 2026</strong>, de ≈ 13 a ≈ 19,6 MW
   promedio, que se sostiene hasta septiembre y es consistente con la proyección de 19,0 MW plano.
   Y <strong>el máximo horario de 31,3 MW registrado en julio excede la potencia de descarga de
   20 MW del BESS diseñado</strong>: en esas horas el proyecto no puede sostener el consumo aun
   con la batería llena.</p>
  </div>
 </div>
</section>

<section id="recurso">
 <div class="wrap">
  <div class="sec-head">
   <span class="eyebrow">03 · Validación independiente</span>
   <h2>El recurso solar, y la primera cifra que hay que cerrar</h2>
   <p>Se modeló la generación horaria del sitio (lat −20,70 / lon −69,78, ≈ 1.000 msnm) con geometría
   solar y modelo de cielo claro, sin calibrar contra los datos de SQM.</p>
  </div>

  {tbl("Generación modelada · 76,5 MWp",
       [("Configuración",0),("GHI kWh/m²",1),("Generación anual",1),("Rendimiento kWh/kWp",1)],
       [["Estructura fija 20° norte, DC/AC 1,20","2.689","169,9 GWh","2.220"],
        ["@hi","<strong>Seguidor 1 eje N-S, DC/AC 1,30</strong>","2.689","<strong>207,1 GWh</strong>","2.707"]])}

  <div class="body-copy" style="margin-top:22px;">
   <p>El modelo <strong>reproduce con exactitud los 170 GWh declarados en la DIA</strong>, lo que
   confirma que el diseño de SQM asume estructura fija. Pasar a seguidor de un eje entrega
   <strong>+37 GWh/año (+22%)</strong> por un sobrecosto de ≈ US$ 5,4 M en el campo FV — la mejor
   relación costo-beneficio de todo el rediseño.</p>
  </div>

  <div class="callout warn">
   <h3>Discrepancia a resolver antes de fijar precio</h3>
   <p>La simulación interna previa de Grenergy («Generación Estimada PV+BESS – Industria TEA»)
   asume <strong>220 GWh/año</strong>, un 6% por encima de nuestro caso con seguidor y un 29% sobre
   la DIA. También declara <strong>POI de 17 MW</strong> y una «potencia de retiro del BESS de 70 MW»
   que no cuadra con los 20 MW × 16 h de la DIA. Hay que cerrar tres cifras: <strong>rendimiento
   específico, capacidad del punto de inyección y potencia nominal del BESS</strong>. Una diferencia
   de 50 GWh/año equivale a ≈ US$ 3,5 M/año de energía.</p>
  </div>
 </div>
</section>

<section id="estructura">
 <div class="wrap">
  <div class="sec-head">
   <span class="eyebrow">04 · La operación</span>
   <h2>Estructura de la transacción</h2>
  </div>
  <div class="callout warn" style="margin-top:0;">
   <h3>Actualización tras la reunión interna del 29-sep-2026</h3>
   <p>La minuta advierte que la figura de autoconsumo <strong>exige mismo propietario</strong> para la
   generación y el consumo, o bien estructurarse vía mandato/contrato. La estructura descrita aquí
   —GR adquiere el activo y es propietario— conserva el beneficio de peajes sólo si se resuelve esa
   restricción. El análisis de escenarios y la estrategia regulatoria están en
   <a href="escenarios-y-hoja-de-ruta-sqm.html">Escenarios y hoja de ruta</a>, que además muestra que
   el beneficio en juego (11 USD/MWh) es mucho menor que el de coordinar con el CEN (44 USD/MWh).</p>
  </div>
  <div class="flow">
   <div class="flow-step"><span class="ph">Fase 1</span>
     <p><strong>SQM mantiene la titularidad</strong> y lleva la DIA hasta RCA firme (nov-2026).
     GR ejecuta due diligence técnico-legal sobre el expediente.</p></div>
   <div class="flow-step"><span class="ph">Fase 2</span>
     <p><strong>Compraventa del vehículo</strong> — share deal sobre la SPV titular de la RCA,
     servidumbres, terrenos y avance de conexión. Precio = componente fija al cierre + earn-out
     contra hitos.</p></div>
   <div class="flow-step"><span class="ph">Fase 3</span>
     <p><strong>GR rediseña</strong> (seguidores, BESS redimensionado, POI ampliado), tramita la
     modificación de RCA, construye, opera y es propietario del activo.</p></div>
   <div class="flow-step"><span class="ph">Fase 4</span>
     <p><strong>PPA de suministro GR → SQM</strong> en el Tap Off Nueva Victoria 110 kV: bloque 24/7,
     15–20 años, precio fijo en USD indexado. GR Power respalda el déficit desde cartera
     (Oasis de Atacama / Elena).</p></div>
  </div>
  <div class="grid-2" style="margin-top:30px;">
   <div class="body-copy">
    <h3>Por qué le sirve a SQM</h3>
    <p>Libera ≈ US$ 111 M de capital que no es <em>core</em> para una minera no metálica, traslada el
    riesgo de construcción, operación, degradación del BESS y mercado eléctrico a un operador
    especializado, y fija precio de energía por 15–20 años muy por debajo de su costo actual.
    Conserva el beneficio ambiental del proyecto que originó.</p>
   </div>
   <div class="body-copy">
    <h3>Por qué le sirve a GR</h3>
    <p>Entra a un activo con RCA en etapa avanzada —el permiso más lento de la cadena chilena— con
    un offtaker <em>investment grade</em> ya identificado y punto de conexión definido, y suma un nodo
    en Tarapacá que complementa geográficamente la plataforma de Antofagasta.</p>
   </div>
  </div>
 </div>
</section>

<section id="alternativas">
 <div class="wrap">
  <div class="sec-head">
   <span class="eyebrow">05 · Las dos alternativas</span>
   <h2>Autonomía física frente a optimización de sistema</h2>
   <p>La Alternativa 1 es el concepto original de SQM ejecutado por GR. La Alternativa 2 dimensiona
   el almacenamiento por valor en lugar de por autonomía, y cierra el bloque 24/7 con la cartera de
   Grenergy Power.</p>
  </div>

  {tbl("Comparación de las dos alternativas",
       [("",0),("Alternativa 1 — PPA 24/7 con BESS de 16 h",0),("Alternativa 2 — PPA híbrido optimizado",0)],
       [["Configuración","76,5 MWp (seguidor) + 320 MWh / 20 MW","<strong>76,5 MWp (seguidor) + 150 MWh / 30 MW</strong>"],
        ["CAPEX","US$ 117,0 M","<strong>US$ 92,7 M</strong>"],
        ["Generación","207 GWh/año","207 GWh/año"],
        ["Autosuficiencia física","79,9%","61,5%"],
        ["Importación desde GR Power","33,5 GWh/año","64,0 GWh/año a ≈ 54 USD/MWh"],
        ["Exportación de excedentes","64,2 GWh/año","95,1 GWh/año a ≈ 51 USD/MWh"],
        ["Ciclos equivalentes del BESS","242/año","<strong>496/año</strong>"],
        ["Costo de servir · conservador","78,5 USD/MWh","<strong>54,4 USD/MWh</strong>"],
        ["Costo de servir · base","74,1 USD/MWh","<strong>45,6 USD/MWh</strong>"],
        ["@hi","<strong>Precio PPA a ofertar</strong>","<strong>85 – 92 USD/MWh</strong>","<strong>62 – 68 USD/MWh</strong>"],
        ["Ahorro para SQM vs. ≈100 USD/MWh","8 – 15%","<strong>32 – 38%</strong>"],
        ["Margen GR a 70 USD/MWh","−0,7 M USD/año","<strong>+4,1 M USD/año</strong>"],
        ["Tramitación incremental","—","12 – 18 meses (PGP con el CEN)"]])}

  <div class="callout">
   <h3>El punto clave de la Alternativa 2</h3>
   <p>La autosuficiencia <em>física</em> baja de 80% a 62%, pero el suministro sigue siendo
   <strong>100% renovable y 24/7 en términos contractuales</strong>, porque el respaldo viene de la
   cartera renovable de Grenergy Power. SQM no pierde el atributo verde; pierde solo la autonomía
   física — y por esa autonomía estaría pagando ≈ 28 USD/MWh adicionales, unos
   <strong>US$ 4,7 M al año</strong>.</p>
  </div>

  <figure>
   <div class="chartwrap">{fig3}</div>
   <figcaption><b>Costo de servir el bloque 24/7 por configuración.</b> El punto marca el escenario
   base; la línea, el rango entre el escenario conservador y el optimista. La referencia punteada en
   100 USD/MWh es el precio final promedio que paga hoy un cliente libre en Chile. El diseño actual
   queda por encima de esa línea en los tres escenarios. <b>En azul</b>, el diseño actual y la
   Alternativa 1; <b>en naranja</b>, la configuración recomendada; <b>en verde</b>, las demás
   configuraciones evaluadas.</figcaption>
  </figure>
 </div>
</section>

<section id="lcoe">
 <div class="wrap">
  <div class="sec-head">
   <span class="eyebrow">06 · Optimización de LCOE</span>
   <h2>Dónde está el dinero</h2>
  </div>

  {tbl("Descomposición del diseño actual — estructura fija, 320 MWh/20 MW, autoconsumo puro",
       [("Concepto",0),("US$ M/año",1)],
       [["Costo de capital anualizado","10,60"],["OPEX","3,79"],
        ["Compras de energía para cubrir déficit (42,0 GWh)","3,04"],
        ["Ingresos por exportación, potencia y SSCC","0,00"],
        ["@hi","<strong>Total ÷ 166,4 GWh</strong>","<strong>109,7 USD/MWh</strong>"]])}

  {tbl("Las cuatro palancas, cuantificadas",
       [("#",0),("Palanca",0),("Efecto sobre el costo de servir",1)],
       [["1","<strong>Coordinar con el CEN</strong> — de autoconsumo aislado a generación-consumo: habilita inyección, pago por potencia y SSCC","<strong>−43,6</strong>"],
        ["2","<strong>Redimensionar el BESS</strong> de 16 h a 4–5 h","<strong>−31,0</strong>"],
        ["3","<strong>Seguidor de un eje</strong> — +22% de energía por +8% de CAPEX FV","−5 a −6"],
        ["4","<strong>Ampliar el POI</strong> de 17 a 25–30 MW","−4,5"]])}

  <figure>
   <div class="chartwrap">{fig1}</div>
   <figcaption><b>La curva de optimización del almacenamiento.</b> Costo de servir el bloque 24/7
   según la duración del BESS, con FV de 76,5 MWp en seguidor y BESS de 30 MW. El óptimo está en
   4–6 horas en los <b>tres</b> escenarios de mercado, y la configuración recomendada de 5 h queda a
   menos de 0,3 USD/MWh del mínimo en cada uno de ellos. El diseño de SQM
   se sitúa en el extremo derecho de la curva, donde el costo ya volvió a subir.</figcaption>
  </figure>

  {tbl("Costo marginal de cada hora adicional de almacenamiento — escenario base",
       [("Tramo",0),("Efecto USD/MWh",1),("US$/año",1)],
       [["0 → 1 h","−18,3","−3,05 M"],["1 → 2 h","−9,6","−1,60 M"],["2 → 3 h","−7,6","−1,27 M"],
        ["3 → 4 h","−6,3","−1,05 M"],["4 → 5 h","−1,5","−0,25 M"],
        ["@hi","<strong>5 → 6 h</strong>","<strong>+1,5</strong>","<strong>+0,25 M</strong>"],
        ["6 → 8 h","+3,4","+0,57 M"],["8 → 10 h","+5,7","+0,95 M"],["10 → 12 h","+6,8","+1,13 M"],
        ["12 → 14 h","+6,7","+1,12 M"],["14 → 16 h","+6,8","+1,13 M"]])}

  <div class="body-copy" style="margin-top:22px;">
   <p><strong>La razón física:</strong> con 76,5 MWp generando 207 GWh contra un consumo de 166 GWh,
   el balance anual es ajustado. En verano sobra energía y en invierno falta; una batería diaria no
   resuelve un desbalance estacional. Las horas 6 a 16 quedan esperando un excedente que solo aparece
   unos pocos meses al año, y mientras tanto pagan capital.</p>
  </div>

  <figure>
   <div class="chartwrap">{fig2}</div>
   <figcaption><b>Por qué el almacenamiento vale lo que vale.</b> El norte del SEN presenta una
   estructura horaria de costo marginal muy pronunciada: ≈ 13 USD/MWh en horas solares (22% de las
   horas del año bajo 10 USD/MWh) contra ≈ 137 USD/MWh en la rampa vespertina. Un BESS de 30 MW × 5 h
   captura ese diferencial <b>496 veces al año</b>; uno de 20 MW × 16 h lo captura 242 veces. La misma
   inversión en litio rinde el doble cuando se dimensiona para el ciclo diario.</figcaption>
  </figure>

  {tbl("Sensibilidad del costo de servir al punto de inyección — configuración recomendada (150 MWh/30 MW)",
       [("POI",0),("Conservador",1),("Base",1),("Optimista",1),("Exportación",1),("Vertimiento",1)],
       [["0 — aislado","96,1","94,2","92,7","0 GWh","75,1 GWh"],
        ["10 MW","66,7","56,5","49,7","53,5","37,8"],
        ["17 MW — supuesto GR actual","59,6","50,6","45,2","77,4","16,2"],
        ["@hi","<strong>25 MW</strong>","55,1","<strong>46,8</strong>","42,5","93,8","0,5"],
        ["30 MW","54,7","46,1","41,3","94,6","0"],
        ["@dim","40 MW","54,4","45,6","40,4","95,1","0"]])}

  <div class="body-copy" style="margin-top:22px;">
   <p>El salto de 0 a 17 MW vale 43,6 USD/MWh; de 17 a 25–30 MW, otros 4 a 4,5. Por encima de 30 MW
   satura. <strong>El diseño objetivo debe asegurar POI ≥ 25 MW</strong> — algo que hay que verificar
   contra la capacidad real de la LT de 66 kV y del punto de seccionamiento.</p>
  </div>

  {tbl("Sensibilidad al WACC y al CAPEX — escenario base, USD/MWh",
       [("",0),("−15% / 6%",1),("Base / 7%",1),("+15% / 8%",1),("+30% / 9%",1)],
       [["Alternativa 1 · WACC","67,5","74,1","81,0","88,2"],
        ["@hi","<strong>Alternativa 2 · WACC</strong>","<strong>40,4</strong>","<strong>45,6</strong>","<strong>51,1</strong>","<strong>56,8</strong>"],
        ["Alternativa 1 · CAPEX","64,5","74,1","83,7","93,3"],
        ["@hi","<strong>Alternativa 2 · CAPEX</strong>","<strong>38,2</strong>","<strong>45,6</strong>","<strong>53,0</strong>","<strong>60,4</strong>"]])}

  <div class="callout">
   <h3>La Alternativa 2 domina en todo el rango</h3>
   <p>Incluso con CAPEX 30% por encima del supuesto y WACC de 9%, la Alternativa 2 sigue por debajo
   del caso base de la Alternativa 1. La conclusión no depende de la calibración de costos.</p>
  </div>
 </div>
</section>

<section id="benchmark">
 <div class="wrap">
  <div class="sec-head">
   <span class="eyebrow">07 · Mercado</span>
   <h2>Referencias de precio y operaciones comparables</h2>
  </div>

  {tbl("Referencias de precio en Chile",
       [("Indicador",0),("Valor",1),("Período",0)],
       [["Precio Medio de Mercado (PMM), SEN","109,2 USD/MWh","dic-2025"],
        ["@hi","<strong>Precio final promedio a clientes libres</strong>","<strong>US$ 87 → 107/MWh</strong>","2020 → 2024"],
        ["Proyección de precio para nuevos clientes libres","60 – 70 USD/MWh","2026"],
        ["Licitación de suministro regulado (rango de ofertas)","38 – 120 USD/MWh","2026"],
        ["Costo marginal barra Tarapacá","53,5 → 63,6 USD/MWh","dic-25 → may-26"],
        ["Costo marginal barra Crucero","50,6 → 60,7 USD/MWh","dic-25 → may-26"]])}

  {tbl("Operaciones comparables",
       [("Operación",0),("Estructura",0),("Volumen / plazo",0),("Lectura",0)],
       [["<strong>Grenergy – Codelco</strong> (abr-2025)","Primer PPA 24/7 de GR en Chile","0,5 TWh/año · 15 años","Precedente directo del producto 24/7 con respaldo de cartera"],
        ["<strong>Grenergy – offtaker</strong> (jun-2026)","PPA nocturno desde BESS Elena (3,5 GWh, ampliable a 7)","1 TWh/año · 15 años, horario no solar","Demuestra que GR vende el bloque nocturno <em>sin</em> batería dedicada del cliente"],
        ["<strong>Grenergy – Algarrobal</strong> (jun-2026)","PPA híbrido, offtaker <em>investment grade</em>","350 GWh/año · 12 años, desde ene-2028","Estructura híbrida ya validada comercialmente"],
        ["<strong>Atlas – Codelco</strong> (mar-2024)","PPA 24/7 solar + BESS; proyecto 215 MW / 1,6 GWh","375 GWh/año · 15 años","Competidor directo en el mismo producto"],
        ["@hi","<strong>Sonnedix – Copec EMOAC</strong> (abr-2026)","BESS 117 MW / 643,8 MWh ≈ <strong>5,5 h</strong>","COD abr-2027","<span class='chip good'>confirma 4–6 h</span>"],
        ["@hi","<strong>Atlas – COPEC</strong>","BESS 200 MW / 800 MWh = <strong>4 h</strong>","—","<span class='chip good'>confirma 4–6 h</span>"],
        ["<strong>BHP – Sungrow</strong>","195 MW solar + 960 MWh en Escondida y Spence","—","Autoconsumo minero con almacenamiento acotado"],
        ["@hi","Proyecto minero (sep-2026)","10 MWp FV + <strong>40 MWh (4 h)</strong>","−23% de costo energético, 90% renovable","<span class='chip good'>confirma 4–6 h</span>"]])}

  <div class="callout">
   <h3>Hallazgo del benchmark</h3>
   <p>En todas las operaciones comparables de solar + almacenamiento para consumo industrial en Chile,
   <strong>la duración del BESS está entre 4 y 6 horas</strong>. No hay precedente de un almacenamiento
   de 16 horas asociado a un consumo industrial. El diseño de SQM es un <em>outlier</em> de mercado, y
   el análisis explica por qué: la autonomía de 16 horas es una especificación de continuidad
   operacional, no una decisión económica. Es el argumento más potente para la conversación:
   <strong>no proponemos recortar su proyecto, proponemos alinearlo con lo que hace todo el mercado</strong>,
   incluidos sus pares mineros.</p>
  </div>
 </div>
</section>

<section id="precio">
 <div class="wrap">
  <div class="sec-head">
   <span class="eyebrow">08 · Precio</span>
   <h2>Escalera de precios y bolsa de valor</h2>
  </div>

  <div class="grid-2">
   <div>{tbl("Alternativa 1 — PPA 24/7 con BESS de 16 h",
        [("Escenario",0),("Costo",1),("+10%",1),("+20%",1),("+30%",1)],
        [["Conservador","78,5","86,4","94,3","102,1"],
         ["Base","74,1","81,6","89,0","96,4"],
         ["Optimista","73,4","80,7","88,1","95,4"]])}</div>
   <div>{tbl("Alternativa 2 — PPA híbrido optimizado",
        [("Escenario",0),("Costo",1),("+10%",1),("+20%",1),("+30%",1)],
        [["@hi","<strong>Conservador</strong>","<strong>54,4</strong>","59,8","<strong>65,3</strong>","70,7"],
         ["Base","45,6","50,1","54,7","59,3"],
         ["Optimista","40,4","44,4","48,5","52,5"]])}</div>
  </div>

  <div class="body-copy" style="margin-top:26px;">
   <p><strong>Precio recomendado a poner sobre la mesa: 62–68 USD/MWh</strong> para la Alternativa 2,
   anclado en el escenario conservador (54,4) más margen. Deja 8–14 USD/MWh de colchón contra
   compresión de spreads y, aun así, ofrece a SQM un ahorro de un tercio sobre su costo actual.
   Para la Alternativa 1 el precio ofertable honesto es <strong>85–92 USD/MWh</strong> — útil
   precisamente para mostrar el costo de la autonomía.</p>
  </div>

  {tbl("Margen anual de GR y valor presente a 7% real, según el precio PPA acordado",
       [("Precio PPA",1),("Alt. 1 margen",1),("VAN 15 a",1),("VAN 20 a",1),("Alt. 2 margen",1),("VAN 15 a",1),("VAN 20 a",1)],
       [["60","−2,35 M","−21,4 M","−24,9 M","+2,40 M","21,8 M","25,4 M"],
        ["65","−1,52 M","−13,9 M","−16,1 M","+3,23 M","29,4 M","34,2 M"],
        ["@hi","<strong>70</strong>","<strong>−0,69 M</strong>","<strong>−6,3 M</strong>","−7,3 M","<strong>+4,06 M</strong>","<strong>37,0 M</strong>","43,0 M"],
        ["75","+0,14 M","1,3 M","1,5 M","+4,90 M","44,6 M","51,9 M"],
        ["80","+0,97 M","8,9 M","10,3 M","+5,73 M","52,2 M","60,7 M"]])}

  <div class="callout">
   <h3>Lectura para la negociación</h3>
   <p>A 70 USD/MWh la Alternativa 2 genera un VAN de <strong>US$ 37–43 M</strong>. Esa es la bolsa
   desde la cual se paga (i) el activo de desarrollo a SQM y (ii) el retorno incremental de GR.
   <strong>La Alternativa 1 al mismo precio es deficitaria</strong> (−US$ 6,3 M): si SQM insiste en
   las 16 horas, el precio no puede bajar de ≈ 85 USD/MWh. Estructura de pago sugerida:
   componente fija modesta al cierre, reconociendo el gasto de desarrollo y el expediente SEA, más
   <em>earn-out</em> contra RCA firme, contra obtención del POI ≥ 25 MW y contra COD.</p>
  </div>
 </div>
</section>

<section id="regulatorio">
 <div class="wrap">
  <div class="sec-head">
   <span class="eyebrow">09 · Regulatorio</span>
   <h2>El DS 32/2026 cambia el tablero</h2>
   <p>El Decreto Supremo N° 32 del Ministerio de Energía, publicado en junio de 2026, modifica el
   Reglamento de Coordinación y Operación del SEN (DS 125/2017) e incorpora tres figuras directamente
   aplicables a esta operación.</p>
  </div>

  <ul class="plain">
   <li><span class="n">01</span><span><strong>Sistemas de Almacenamiento de Energía (SAE)</strong>
     entre las instalaciones sujetas a coordinación, con reglas para su incorporación a la
     programación de la operación.</span></li>
   <li><span class="n">02</span><span><strong>Sistemas de generación-consumo</strong>, figura pensada
     para complejos productivos que combinan proceso industrial, generación propia y almacenamiento.
     <strong>Es la figura que habilita la Alternativa 2.</strong></span></li>
   <li><span class="n">03</span><span><strong>Cliente con autoconsumo</strong>, definido como aquel
     que, teniendo generación y/o almacenamiento propios, <em>no inyecta excedentes al sistema</em>.
     Es la figura que corresponde a la Alternativa 1 en su versión aislada — y la razón por la que
     esa versión renuncia a 43,6 USD/MWh de valor.</span></li>
  </ul>

  {tbl("Rutas de tramitación — base: análisis de N. Machuca",
       [("",0),("Opción off-grid (autoconsumo)",0),("Opción on-grid (generación-consumo)",0)],
       [["Declaración","SEC — proyecto como autoconsumo (plazos por confirmar)","Fehaciente híbrido: <strong>4–6 meses</strong>"],
        ["Permisos post-RCA","IFC, SEREMI, DOM: 6–9 meses","IFC, SEREMI, DOM: 6–9 meses"],
        ["CNE","—","Declaración en construcción: 2 meses"],
        ["CEN","—","Proceso PGP para operación: <strong>10–12 meses</strong>"],
        ["@hi","<strong>Camino crítico incremental</strong>","—","<strong>≈ 12–18 meses adicionales</strong>"]])}

  <div class="callout warn">
   <h3>Secuencia recomendada</h3>
   <p>Los 12–18 meses adicionales son el costo real de la Alternativa 2. Contra los ≈ 28 USD/MWh de
   diferencia (≈ US$ 4,7 M/año), el retraso se paga en menos de un año de operación — pero hay que
   gestionarlo en paralelo desde el día uno, no en secuencia. <strong>Iniciar el fehaciente híbrido y
   la conversación con el CEN antes del cierre de la compraventa</strong>, en paralelo con la adenda
   ambiental de SQM y al amparo del NDA vigente. El PGP de 10–12 meses es el camino crítico y no
   admite recuperación posterior.</p>
   <p>En paralelo: pedirle a SQM que <strong>introduzca la flexibilidad de diseño en la adenda que
   está preparando ahora</strong> —seguidores, rango de potencia del BESS, POI ampliado—, antes de la
   RCA. Es mucho más barato que una modificación posterior y es una petición concreta, de bajo costo
   para ellos, para la próxima reunión.</p>
  </div>
 </div>
</section>

<section id="riesgos">
 <div class="wrap">
  <div class="sec-head">
   <span class="eyebrow">10 · Riesgos</span>
   <h2>Exposición y mitigantes</h2>
  </div>
  {tbl("Matriz de riesgos",
       [("Riesgo",0),("Exposición",0),("Mitigante",0)],
       [["<strong>Compresión del spread horario.</strong> El almacenamiento instalado en Chile (≈ 1.700 MW a feb-2026) se duplica hacia dic-2026","<span class='chip risk'>alto</span> Es el principal supuesto del caso","Precio anclado en escenario conservador: spread comprimido 45%, captura 70%, sin SSCC. La Alternativa 2 sigue siendo superior en ese escenario"],
        ["<strong>Caída del precio de potencia</strong> por entrada masiva de BESS","<span class='chip'>medio</span> US$ 3,7 M/año en el caso base","El escenario conservador ya asume 6,5 USD/kW-mes"],
        ["<strong>POI limitado a 17 MW</strong> o menos por capacidad de la LT 66 kV","<span class='chip risk'>alto</span> Vale 4,5 USD/MWh; bajo 10 MW el caso se deteriora rápido","Verificar capacidad real antes de fijar precio. Condición suspensiva en el SPA"],
        ["<strong>RCA se retrasa o llega con condiciones</strong>","<span class='chip'>medio</span>","Earn-out contra RCA firme; no adelantar pagos"],
        ["<strong>El rediseño exige nueva evaluación ambiental</strong>","<span class='chip risk'>medio-alto</span>","Introducir flexibilidad en la adenda actual de SQM"],
        ["<strong>Crecimiento del consumo</strong> por sobre los 20,2 MW proyectados","<span class='chip'>bajo-medio</span>","Cláusula de ampliación con precio predefinido; la configuración híbrida escala mejor que la aislada"],
        ["<strong>Máximos horarios de 31,3 MW</strong> superan la descarga del BESS","<span class='chip risk'>cierto en el diseño actual</span>","Los 30 MW de potencia BESS de la Alternativa 2 lo cubren casi por completo; el resto desde la red"],
        ["<strong>Captura merchant imperfecta</strong> — el modelo usa despacho óptimo","<span class='chip'>medio</span>","El escenario conservador castiga la captura a 70%"]])}
 </div>
</section>

<section id="pasos">
 <div class="wrap">
  <div class="sec-head">
   <span class="eyebrow">11 · Siguiente</span>
   <h2>Información a pedir y próximos pasos</h2>
  </div>
  <div class="grid-2">
   <div class="body-copy">
    <h3>Información a solicitar a SQM</h3>
    <ol style="margin:0;padding-left:1.2em;display:flex;flex-direction:column;gap:9px;font-size:.9rem;color:var(--ink-2);">
     <li><strong>Curva horaria de consumo completa</strong> (8.760 h) de al menos dos años, no promedios anuales.</li>
     <li><strong>Detalle del escalón abril-mayo 2026</strong> (13 → 19,6 MW): ¿ampliación permanente, campaña, cambio de proceso?</li>
     <li><strong>Estudio de generación</strong> con el que se calcularon los 170 GWh: software, configuración, pérdidas, P50/P90.</li>
     <li><strong>Capacidad real de inyección</strong> del punto de seccionamiento en 66 kV y estudios eléctricos asociados.</li>
     <li><strong>Contratos de suministro vigentes</strong>: precio, plazo, vencimiento y condiciones de salida.</li>
     <li><strong>Expediente SEA completo</strong>, ICSARA y borrador de adenda.</li>
     <li><strong>Situación de terrenos</strong>: propiedad, CUO, servidumbres de la LT.</li>
     <li><strong>Presupuesto y ofertas de EPC</strong> recibidas, para contrastar el CAPEX de US$ 111 M.</li>
    </ol>
   </div>
   <div>
    {tbl("Próximos pasos",
         [("#",0),("Acción",0),("Responsable",0),("Plazo",0)],
         [["1","Cerrar las tres cifras discrepantes (rendimiento, POI, potencia BESS)","N. Machuca / M. Aguilera","1 sem"],
          ["2","Validar precio de transferencia de GR Power para el bloque de respaldo","J. Friedl / J. Álvarez","1 sem"],
          ["3","Revisión legal de la estructura de adquisición (share vs. asset deal)","J. Vergara","2 sem"],
          ["4","Consulta al equipo ambiental sobre flexibilidad de diseño en la adenda","Equipo ambiental","2 sem"],
          ["5","Reunión con SQM: presentar ambas alternativas y solicitar información","R. Hernández / J. Friedl","3 sem"],
          ["6","Term sheet no vinculante (PPA + opción de compra)","GR Power / Desarrollo","6 sem"]])}
   </div>
  </div>
 </div>
</section>

<section id="metodo">
 <div class="wrap">
  <div class="sec-head">
   <span class="eyebrow">12 · Anexo</span>
   <h2>Metodología, supuestos y limitaciones</h2>
  </div>

  <div class="body-copy">
   <p><strong>Generación FV.</strong> Modelo horario de 8.760 h con geometría solar para
   lat −20,70 / lon −69,78, irradiancia de cielo claro tipo ASHRAE calibrada a alta altitud y aire
   limpio, transposición al plano del arreglo (fija a 20° norte y seguidor de un eje N-S con
   backtracking, GCR 0,33), derrateo térmico con NOCT 45 °C y coeficiente −0,34%/°C, pérdidas de
   sistema 11,5%, disponibilidad y suciedad 96,5%, recorte por inversor según DC/AC.
   <em>Sin calibración a los datos de SQM</em>: el resultado de 169,9 GWh para estructura fija
   coincide de forma independiente con los 170 GWh declarados en la DIA.</p>
   <p><strong>Consumo.</strong> Perfil plano de 19,0 MW con variabilidad autocorrelacionada calibrada
   a la dispersión observada en los medidores 2026 (desviación ≈ 10,5%, rango 13,6–24,9 MW).</p>
   <p><strong>Precio horario.</strong> Perfil de costo marginal de la barra Tarapacá con media anual
   de 60 USD/MWh, forma horaria del norte del SEN (valle solar profundo, rampa vespertina alta) y
   volatilidad log-normal; 22,5% de las horas bajo 10 USD/MWh.</p>
   <p><strong>Despacho.</strong> Optimización por programación lineal con horizonte semanal (168 h) y
   SOC cíclico, minimizando el costo económico de servir el consumo, con todas las variables —carga,
   descarga, importación, exportación, vertimiento— valoradas a costo de oportunidad horario.
   Rendimiento de ida y vuelta 88%, profundidad de descarga 94%.</p>
   <p><strong>Economía.</strong> CAPEX unitarios calibrados contra la inversión declarada de US$ 111 M
   — el modelo reproduce US$ 111,2 M para el diseño de la DIA. WACC real después de impuestos 7,0%,
   vida económica 25 años, impuesto 27% con depreciación lineal a 10 años, degradación FV 0,45%/año.</p>
  </div>

  <div class="grid-2" style="margin-top:8px;">
   <div>{tbl("Supuestos de costo",
        [("Partida",0),("Valor",1)],
        [["FV estructura fija","620 USD/kWp"],["FV seguidor 1 eje","690 USD/kWp"],
         ["BESS — componente de potencia","95 USD/kW"],["BESS — componente de energía","138 USD/kWh"],
         ["Infraestructura común (LT, SE, caminos, conexión)","US$ 9,5 M"],
         ["Desarrollo + owner's cost + contingencia","8% del subtotal"],
         ["OPEX FV","11,5 USD/kWp/año"],["OPEX BESS (O&amp;M + aumentación)","7,5 USD/kWh/año"],
         ["Seguros","0,45% del CAPEX/año"],
         ["Peajes + cargo servicio público + pérdidas","18 USD/MWh"]])}</div>
   <div>{tbl("Escenarios de mercado",
        [("Parámetro",0),("Conserv.",1),("Base",1),("Optim.",1)],
        [["Costo marginal medio","55","60","65"],
         ["Compresión del spread horario","45%","25%","0%"],
         ["Captura del valor merchant","70%","80%","90%"],
         ["Precio de potencia (USD/kW-mes)","6,5","8,5","9,5"],
         ["Ingreso por SSCC (USD/kW-año)","0","20","35"]])}</div>
  </div>

  <div class="callout warn">
   <h3>Limitaciones</h3>
   <p>El despacho por programación lineal supone <strong>previsión perfecta</strong>; el escenario base
   castiga la captura a 80% y el conservador a 70%, pero la captura real depende de la calidad de la
   operación. El perfil de costo marginal es <strong>sintético y calibrado a referencias públicas</strong>,
   no una proyección con modelo de despacho del SEN: antes de una oferta vinculante debe sustituirse por
   la proyección oficial de GR Power. El consumo se modela como un año representativo de 19,0 MW, sin la
   trayectoria 2026–2040 ni la estacionalidad real, que a la fecha no está disponible con detalle horario.
   El reconocimiento de potencia firme del BESS usa el criterio de bloque de punta de 4 horas acotado por
   la capacidad de inyección, y <strong>requiere validación con el CEN</strong>. No se modelan impuestos
   diferidos, estructura de deuda de proyecto, cobertura cambiaria ni el detalle de las garantías del PPA.</p>
  </div>
 </div>
</section>

<section id="fuentes">
 <div class="wrap">
  <div class="sec-head"><span class="eyebrow">13 · Fuentes</span><h2>Referencias</h2></div>
  <div class="refs">
   <div class="refgroup">
    <h3>Documentación interna</h3>
    <ol>
     <li>Hilo de correo «Grenergy – SQM Sinergias de PPAs», nov-2025 a sep-2026: tabla de proyección
     de consumo de SQM, extracción de medidores de N. Machuca, simulación «Generación Estimada
     PV+BESS – Industria TEA» y análisis de rutas de tramitación.</li>
    </ol>
   </div>
   <div class="refgroup">
    <h3>Proyecto y regulación</h3>
    <ol>
     <li><a href="https://www.sea.gob.cl/portal-de-participacion-ciudadana-y-consulta-indigena/proyecto/parque-fotovoltaico-y-linea-de-0">SEA — Ficha del proyecto «Parque Fotovoltaico y Línea de Transmisión … Región de Tarapacá»</a></li>
     <li><a href="https://www.revistaei.cl/minera-sqm-ingresa-al-seia-proyecto-solar-y-de-almacenamiento-por-us111-millones/">Revista Electricidad — «Minera SQM ingresa al SEIA proyecto solar y de almacenamiento por US$111 millones»</a></li>
     <li><a href="https://www.energiaestrategica.com/es/notes/chile-activa-el-decreto-32-las-nuevas-reglas-que-reordenan-almacenamiento-pmgd-y-operacion-electrica">Energía Estratégica — «Chile activa el Decreto 32: las nuevas reglas que reordenan almacenamiento, PMGD y operación eléctrica»</a></li>
     <li><a href="https://www.garrigues.com/es_ES/noticia/chile-gobierno-aprueba-decreto-redefine-operacion-sistema-electrico-reparto-inyecciones">Garrigues — «Chile: El Gobierno aprueba un decreto que redefine la operación del sistema eléctrico y el reparto de inyecciones»</a></li>
    </ol>
   </div>
   <div class="refgroup">
    <h3>Precios y mercado</h3>
    <ol>
     <li><a href="https://www.cne.cl/wp-content/uploads/2026/01/RMensual_v202601.pdf">CNE — Reporte Mensual del Sector Energético, enero 2026</a></li>
     <li><a href="https://www.cne.cl/wp-content/uploads/2026/06/RMensual_v202606.pdf">CNE — Reporte Mensual del Sector Energético, junio 2026</a></li>
     <li><a href="https://electromineria.cl/sistema-electrico-precio-final-promedio-a-clientes-libres-sube-de-us87-a-us107-por-mwh-entre-2020-y-2024/">Electrominería — «Precio final promedio a clientes libres sube de US$87 a US$107 por MWh entre 2020 y 2024»</a></li>
     <li><a href="https://www.energiaestrategica.com/chile-amplia-el-mercado-electrico-acen-proyecta-precios-de-usd-70-por-mwh-para-2026/">Energía Estratégica — «ACEN proyecta precios de USD 70 por MWh para 2026»</a></li>
     <li><a href="https://ember-energy.org/latest-insights/how-cheap-is-battery-storage/">Ember Energy — «How cheap is battery storage?»</a></li>
    </ol>
   </div>
   <div class="refgroup">
    <h3>Operaciones comparables</h3>
    <ol>
     <li><a href="https://www.pv-magazine.es/2026/07/01/grenergy-firma-un-ppa-nocturno-de-1-twh-anual-durante-15-anos-en-chile/">pv magazine — «Grenergy firma un PPA nocturno de 1 TWh anual durante 15 años en Chile»</a></li>
     <li><a href="https://www.pv-magazine-latam.com/2026/06/01/grenergy-firma-en-chile-un-ppa-hibrido-por-350-gwh-anuales-para-la-fase-algarrobal-de-oasis-de-atacama/">pv magazine LatAm — «Grenergy firma un PPA híbrido por 350 GWh anuales para la fase Algarrobal de Oasis de Atacama»</a></li>
     <li><a href="https://www.pv-magazine-latam.com/2026/07/02/grenergy-subasta-en-chile-15-twh-anuales-de-energia-solar-y-almacenada/">pv magazine LatAm — «Grenergy subasta en Chile 1,5 TWh anuales de energía solar y almacenada»</a></li>
     <li><a href="https://www.pv-tech.org/atlas-renewable-energy-signs-375gwh-24-7-ppa-with-codelco/">pv-tech — «Atlas Renewable Energy signs 375GWh 24/7 PPA with Codelco»</a></li>
     <li><a href="https://www.pv-tech.org/atlas-renewable-energy-us510-million-financing-215mw-1-6gwh-solar-plus-storage-chile/">pv-tech — «Atlas Renewable Energy secures US$510 million financing for 215MW/1.6GWh solar-plus-storage in Chile»</a></li>
     <li><a href="https://www.energy-storage.news/atlas-copec-ppa-200mw-800mwh-bess-chile/">Energy-Storage.news — «Atlas and COPEC sign PPA for 200MW/800MWh BESS in Chile»</a></li>
     <li><a href="https://www.pv-magazine-latam.com/2026/04/24/en-chile-sonnedix-firma-tres-ppas-con-copec-emoac-para-un-bess-de-117-mw-6438-mwh/">pv magazine LatAm — «Sonnedix firma tres PPAs con Copec EMOAC para un BESS de 117 MW / 643,8 MWh»</a></li>
     <li><a href="https://www.reporteminero.cl/noticia/noticias/2026/09/proyecto-minero-reduce-costos-energeticos-solar-baterias-descarbonizacion">Reporte Minero — «Proyecto minero reduce 23% costos energéticos con solar y baterías»</a></li>
    </ol>
   </div>
  </div>
 </div>
</section>

</main>

<footer>
 <div class="wrap">
  <p>Documento de trabajo interno de Grenergy. Contiene información de SQM sujeta al NDA suscrito
  entre las partes.</p>
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
<title>PPA SQM Nueva Victoria</title>
<meta name="description" content="Propuesta Grenergy a SQM: adquisición del PFV+BESS de Nueva Victoria y PPA de suministro, con el análisis de LCOE de dos alternativas de estructuración.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<style>{CSS}</style>
</head>
<body>
{BODY}
</body>
</html>"""

out = "/home/user/EnergiaCL/docs/propuesta-sqm-ppa-pfv-bess.html"
open(out,"w").write(HTML)
print("escrito:", out, len(HTML), "bytes")
