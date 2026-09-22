# LMT de interconexión Chanqueahue Fase I – Fase II
## Ancho de canalización soterrada, franja de servidumbre y emplazamiento en faja fiscal vs. terreno privado

**Versión:** 1.0 · **Fecha:** 22 de septiembre de 2026
**Origen:** respuesta técnica al correo de Marian Catalán (EPC / Análisis EPC) del 22.09.2026, asunto *"RE: CL -PV- Chanqueahue Fase 2: Creación de Layout y circuitos MT"*.
**Alcance:** dimensionamiento preliminar de la zanja de MT soterrada, determinación de la franja de seguridad y de la franja de servidumbre a constituir, y análisis de viabilidad del trazado como paralelismo en faja vial fiscal frente a servidumbre en terreno privado.
**Estado:** documento de factibilidad. Los anchos son de diseño preliminar y deben confirmarse con ensayo de resistividad térmica del suelo y topografía.

---

## 1. Punto de partida: lo que indica el EPC

| Ítem | Valor informado | Observación |
|---|---|---|
| Potencia pico total | 249,88 MWp | A confirmar si es total F1+F2 o sólo F2 |
| Potencia en POI | 208 MWn | Total; brecha sobre F1 (150 MWn) ≈ **58 MWn** a evacuar por la LMT |
| Inversores | "se ha pasado de 22 a 31" (declara 19 adicionales) | **Inconsistencia**: 31 − 22 = 9, no 19. A aclarar |
| Solución MT | **3 circuitos dobles de 400 mm², soterrados** | Estimación sin datos de terreno, según indica el propio EPC |
| Descarte de solución aérea | Sí | El trazado cruza en varias ocasiones la línea y servidumbre de la LAAT 500 kV |

### 1.1 Interpretación adoptada para el dimensionamiento

"3 circuitos dobles de 400 mm²" admite más de una lectura (3 circuitos con doble terna por circuito; 3 trazados de doble circuito; 3 circuitos con 2 conductores por fase). **Las tres convergen en la misma cantidad de conductores de potencia: 6 ternas = 18 cables unipolares de 400 mm².** El dimensionamiento de zanja se construye sobre esa base, y se incluye la variante de 3 ternas (9 cables) por si la lectura correcta fuese otra.

> **A confirmar con el EPC antes de cerrar el ancho:** (i) número real de ternas; (ii) **nivel de tensión de la MT** (no está indicado y condiciona el ingreso al SEIA, ver §6); (iii) criterio de ampacidad y factores de agrupamiento/derating usados; (iv) longitud estimada del trazado.

---

## 2. Ancho de canalización soterrada

### 2.1 Parámetros geométricos

| Parámetro | Valor adoptado | Rango |
|---|---|---|
| Ø exterior cable 1×400 mm² Al XLPE 18/30 kV | 48 mm | 45–52 mm |
| Envolvente horizontal de una terna en tresbolillo (2×Ø) | 0,10 m | 0,09–0,11 m |
| Recubrimiento lateral cable–pared de zanja (cama de arena) | 0,25 m/lado | 0,20–0,30 m |
| Separación libre entre ternas contiguas (*s*) | variable | criterio térmico |

**Fórmula:** `Ancho a nivel de lecho = 2 × 0,25 + n × 0,10 + (n − 1) × s`

### 2.2 Resultados

| Configuración | *s* = 0,30 m | *s* = 0,50 m *(base)* | *s* = 0,70 m |
|---|---|---|---|
| **6 ternas** (18 cables) — caso del EPC | 2,60 m | **3,60 m** | 4,60 m |
| 3 ternas (9 cables) — variante | 1,40 m | 1,80 m | 2,20 m |

**Caso base recomendado para factibilidad: zanja de 3,6–3,8 m de ancho útil a nivel de lecho**, con *s* = 0,50 m entre ternas.

La separación entre ternas es una decisión **térmica**, no geométrica: con *s* = 0,30 m el derating por agrupamiento de 6 ternas puede llegar a 0,80–0,85, y con *s* ≥ 0,50 m sube a 0,88–0,92. Reducir el ancho de zanja obliga a compensar con sección mayor, con relleno de resistividad térmica controlada (≤ 1,0 K·m/W) o con mayor número de ternas. **Mientras no se mida la resistividad térmica del suelo —precisamente el dato que el EPC advierte que no tiene— el ancho no puede cerrarse por debajo del caso base.**

### 2.3 Profundidad

| Criterio | Exigencia | Fuente |
|---|---|---|
| Cables directamente enterrados (general) | **1,0 m** mínimo desde la superficie del terreno | Pliego Técnico Normativo **RPTD N°13** (remite al pto. 6 del RPTD N°11), DS N°109/2017 MinEnergía |
| Paralelismo soterrado **dentro de faja vial** | **1,20 m** mínimo entre el punto más bajo del terreno y la **clave del ducto** | Instructivo de Paralelismos y Atraviesos, Dirección de Vialidad (Res. DV N°2059) |
| Atravieso bajo calzada | ≥ 1,50 m bajo rasante y ≥ 1,20 m bajo fondo de cuneta/foso, con camisa | Práctica exigida por Vialidad; a confirmar con la Dirección Regional |

**Profundidad total de zanja adoptada: 1,45–1,55 m** (1,20 m de recubrimiento a clave + cama de arena + envolvente de terna). Se adopta el criterio de Vialidad (1,20 m) en todo el trazado, no sólo en faja vial, para no generar dos estándares constructivos.

### 2.4 Sección tipo (caso base, 6 ternas)

```
                    ←————————— 3,60 m (lecho) —————————→
   ════════════════════════════════════════════════════════  terreno natural
   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  relleno compactado
   ──────── cinta de señalización ─────────────────────────      ↑
   ▓▓▓▓▓▓▓▓ placas / ladrillo de protección ▓▓▓▓▓▓▓▓▓▓▓▓▓▓       │ 1,20 m
   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░       │ a clave
   ░ ∴   ∴   ∴   ∴   ∴   ∴  ░  ← 6 ternas en tresbolillo  ░      ↓
   ░0,25│0,10│0,50│ … │0,10│0,25░  + FO + Cu desnudo PAT
   ══════════════════════════════════════════════════════   fondo ≈ 1,50 m
```

---

## 3. Franja de seguridad y franja de servidumbre

### 3.1 La franja de seguridad sí está normada, y es función del ancho de zanja

El **Pliego Técnico Normativo RPTD N°07 "Franja y distancias de seguridad"** (DS N°109/2017 del Ministerio de Energía) establece que, en **líneas subterráneas**, la franja de seguridad queda definida por la zanja que alberga los conductores, **aumentada a cada lado en una distancia de seguridad mínima igual a la mitad del ancho de la canalización**.

> **Franja de seguridad = ancho de zanja + 2 × (½ ancho de zanja) = 2 × ancho de zanja**

| Configuración | Ancho de zanja | **Franja de seguridad (RPTD N°07)** | **Franja de servidumbre recomendada** |
|---|---|---|---|
| 6 ternas, *s* = 0,50 m *(caso base)* | 3,60 m | **7,20 m** | **10 m** |
| 6 ternas, *s* = 0,30 m (compacta) | 2,60 m | 5,20 m | 8 m |
| 3 ternas, *s* = 0,50 m (variante) | 1,80 m | 3,60 m | 6 m |

### 3.2 Por qué la servidumbre debe ser mayor que la franja de seguridad

La franja de seguridad del RPTD N°07 es el **mínimo técnico de seguridad eléctrica**. La franja de servidumbre a escriturar debe además contener:

- **Cámaras y fosos de empalme.** Con largos de bobina de 400 mm² del orden de 500–700 m, se requiere un empalme cada ~500 m. Para 6 ternas el foso es del orden de 2,5 × 10–12 m, y conviene **escalonar los empalmes longitudinalmente** para no concentrar un punto caliente: eso ensancha localmente la franja.
- **Acceso de mantención** (vehículo liviano y, para reparación, retroexcavadora).
- **Derecho a excavar, tender, reparar y reponer**, y prohibición de plantaciones de raíz profunda y de construcciones sobre la traza.
- **Tolerancia de replanteo** entre el trazado de factibilidad y el as-built.

**Recomendación: constituir servidumbre de 10 m de ancho** para el caso base. El costo marginal de escriturar 10 m en lugar de 8 m, en la negociación que ya está en curso con los propietarios, es despreciable frente al costo de tener que renegociar una ampliación después.

### 3.3 Faja de ocupación temporal en construcción

La construcción necesita más ancho que la operación: zanja (3,6 m) + acopio del material excavado (4–5 m a un lado) + pista de maquinaria y tendido de bobinas (4–5 m al otro).

**Faja de ocupación temporal: 15 m** (mínimo 12 m). Debe quedar explícita en el contrato de servidumbre como ocupación temporal durante obras, distinta de la franja permanente de 10 m.

---

## 4. Faja fiscal vs. terreno privado: ¿es viable el paralelismo?

### 4.1 Respuesta corta

**Es legalmente posible, pero no es recomendable como caso base para la línea principal de evacuación.** La recomendación es un esquema híbrido: **trazado principal por terreno privado en servidumbre voluntaria, y uso de la faja vial sólo para el atravieso de la ruta pública** (que es inevitable, dado que los dos predios están separados por una ruta de Vialidad) y, a lo sumo, para tramos cortos de paralelismo sin alternativa.

### 4.2 El marco: qué autoriza Vialidad y en qué términos

El DFL N°850/1997 del MOP faculta a la Dirección de Vialidad para autorizar la ocupación de la faja de los caminos públicos, en la forma y condiciones que ella determine. El trámite es el **"Permiso de ocupación de faja vial en caminos públicos (paralelismo y/o atraviesos)"**, ante la **Dirección Regional de Vialidad**, y se rige por el Instructivo de Paralelismos y Atraviesos (Res. DV N°2059).

El permiso se otorga sólo si la ocupación: no se opone al uso del camino público, pasos a nivel, obras de arte, túneles o puentes; no afecta la estabilidad de las obras ni la seguridad del tránsito ni el desarrollo vial futuro; no obstruye ni altera el paso de las aguas; y no produce contaminación ni alteración paisajística significativa.

### 4.3 Los cinco factores que desaconsejan el paralelismo como caso base

**1) Precariedad del título — el factor decisivo.**
El permiso de Vialidad es un acto administrativo esencialmente revocable. Y lo determinante: **si Vialidad amplía, mejora o conserva el camino, o por cualquier otra causa se requiere cambiar la ubicación de las instalaciones autorizadas, la relocalización es de cargo exclusivo del propietario de las instalaciones.** Aplicado a la línea de evacuación de ~58 MWn de la Fase II, una relocalización forzada significa CAPEX no presupuestado **más indisponibilidad de la planta**. Un título revocable sobre la única vía de evacuación es difícilmente defendible ante financiamiento y ante due diligence de M&A.

**2) La geometría no cabe cómodamente.**
Una faja vial rural típica no deja, fuera del prisma del camino y de la **zona despejada** (el área lateral donde un vehículo que pierde el control debe poder detenerse sin daño significativo), un corredor libre para una franja de seguridad de 7,2 m más los fosos de empalme. El Instructivo además **prohíbe ubicar cámaras en bermas, bordes de terraplén, cortes, escurrimientos de agua, cunetas, fosos, bahías de detención y sobreanchos de compactación**, y exige que sus tapas no sobresalgan del terreno adyacente. Para 18 cables, con un foso de empalme cada ~500 m, esta restricción es, en la práctica, el obstáculo más duro: los empalmes tendrían que salir de la faja de todos modos.

**3) Concurrencia con otros servicios.**
Las fajas viales rurales suelen tener ya APR, telecomunicaciones y la red de distribución de la concesionaria zonal. Cada concurrencia agrega separaciones mínimas, coordinación con terceros y riesgo de daño por obras ajenas.

**4) Carga de tramitación y de obra.**
El permiso exige proyecto aprobado **antes de iniciar la construcción**, con planta a escala 1:1.000 y perfil longitudinal 1:100 coincidente en kilometraje con el eje del camino, indicando cotas de terreno, cota de clave del ducto y borde del pavimento más próximo, con puntos al menos cada 50 m. Súmese pago de derechos, garantías y manejo de tránsito durante las obras. Para varios kilómetros de paralelismo, es un proyecto de ingeniería vial en sí mismo.

**5) No resuelve el problema que originó el soterramiento.**
El motivo por el que el EPC descartó la solución aérea es el cruce reiterado de la servidumbre de la LAAT 500 kV. La faja vial no evita ese conflicto; sólo lo traslada.

### 4.4 El caso base: servidumbre voluntaria en terreno privado

Dado que la LMT de interconexión es una línea particular del proyecto y no se prevé tramitar una **concesión eléctrica definitiva** para ella, no existe la facultad de **imponer** servidumbre: el título es la **servidumbre voluntaria, por escritura pública inscrita en el Conservador de Bienes Raíces**.

Esto convierte el timing en una ventaja y en un riesgo:

> **El proyecto está "en fase de cierre con propietarios". La franja de 10 m de la LMT debe incorporarse ahora, en esa misma negociación y en la misma escritura.** Negociar después una servidumbre aislada sobre un predio que ya cerró condiciones, y sabiendo el propietario que es la única vía de evacuación, es el peor escenario de negociación posible.

**Ventajas frente al paralelismo:** título real, perpetuo, oponible a terceros e inscrito; sin riesgo de relocalización a costo propio; trazado optimizable (por deslindes y caminos internos); y sin permiso sectorial en la ruta crítica.

### 4.5 Si algún tramo cae en terreno fiscal que no es faja vial

Si el trazado debiera pasar por **inmueble fiscal** administrado por el Ministerio de Bienes Nacionales (no por faja vial de Vialidad), el título no es un permiso de Vialidad sino una **Concesión de Uso Oneroso (CUO)** del DL N°1.939/1977. Es una ruta de **13–14 meses P50 y 21–22 meses P80** desde el ingreso (ver `docs/cronograma-cuo-mbn.md`), lo que la pone directamente en la ruta crítica del proyecto. **Debe detectarse en el due diligence territorial, no después.**

---

## 5. Condiciones a considerar en el trazado

### 5.1 Atravieso de la ruta pública entre los dos predios (inevitable)

| Condición | Criterio |
|---|---|
| Ángulo | Perpendicular al eje del camino (90°), o lo más cercano posible |
| Método | **Sin rotura de calzada**: perforación horizontal dirigida (HDD) o hincado con camisa de acero |
| Profundidad | ≥ 1,50 m bajo rasante; ≥ 1,20 m bajo fondo de cuneta/foso |
| Ductos | Camisa de acero + ductos individuales, **más ductos de reserva** (el costo marginal del spare es mínimo y evita un segundo atravieso a futuro) |
| Cámaras | Fuera de la faja vial, a ambos lados |
| Permiso | Dirección Regional de Vialidad, aprobado **antes** de iniciar obras |
| Tránsito | Plan de manejo de tránsito y señalización conforme al Manual de Señalización de Tránsito |

### 5.2 Cruce de la servidumbre de la LAAT 500 kV

Es **viable en soterrado** —de hecho, es la razón técnica que hace preferible el soterramiento— bajo las siguientes condiciones:

- Cruce **perpendicular** y en el menor desarrollo posible dentro de la franja.
- **Autorización del propietario de la línea de 500 kV** (identificar titular; acuerdo de cruce/coexistencia).
- **Ninguna cámara ni foso de empalme dentro de la franja**, y mantención libre de huellas y accesos del propietario de la LAAT.
- **Estudio de interferencia electromagnética**: acoplamiento inductivo en régimen permanente y, sobre todo, **elevación de potencial de tierra (GPR)** ante falla monofásica de la línea de 500 kV. Puede condicionar el tipo de pantalla, su puesta a tierra (single-point / cross-bonding), el uso de contrapesos y la separación mínima a las mallas de tierra de las estructuras.
- La condición eléctrica de cruce no equivale a la condición **legal**: aun siendo técnicamente compatible, la franja está gravada y el cruce debe quedar autorizado y documentado.

### 5.3 Ancho de la servidumbre de la LAAT 500 kV — respuesta a la consulta del EPC

**En Chile no existe un ancho normado genérico por nivel de tensión.** La **franja de seguridad se calcula vano a vano** conforme al RPTD N°07 (Tabla N°3, distancia de seguridad en función de la tensión máxima de la línea), integrando tensión, propiedades del conductor, flecha máxima en condición térmica extrema y topografía; esa memoria de cálculo es uno de los documentos que exige la SEC al tramitar la concesión eléctrica definitiva.

En consecuencia:

- El buffer de **40 m a cada lado (80 m total) que asumió el EPC es un supuesto razonable de orden de magnitud para una línea de 500 kV, pero no es un dato normativo y no debe consolidarse en el layout.**
- **El dato vinculante es la franja efectivamente constituida**: la del **decreto de concesión definitiva** de esa línea y sus **planos especiales de servidumbre inscritos en el CBR**.
- **Acción:** solicitar al titular de la LAAT (y/o revisar el decreto de concesión y la inscripción en el CBR) la franja real. Hasta entonces, mantener los 40 m/lado como hipótesis conservadora explícita.

**Sobre las instalaciones auxiliares permanentes de la Fase I bajo la franja de 500 kV: no corresponde.** Dentro de la franja de seguridad no se admiten edificaciones ni construcciones permanentes. Deben relocalizarse fuera de la franja; es un ajuste de layout, no una gestión de autorización.

### 5.4 Retranqueo del estero — respuesta a la consulta del EPC

**Los 10 m a cada lado tampoco son una cifra normativa.** El criterio vinculante es la definición de **cauce** del Código de Aguas (bienes nacionales de uso público) y la exigencia de **autorización de la DGA para obras en cauces naturales** (arts. 41 y 171).

Criterio recomendado hasta contar con estudio hidráulico:

1. Determinar la **línea de crecida de diseño T = 100 años** y adoptar el retranqueo desde ella, no desde el eje del estero.
2. Buffer provisional de trabajo: **el mayor entre (i) línea de crecida T=100 + 10 m y (ii) 20–25 m desde el eje**. Los 10 m asumidos por el EPC son probablemente insuficientes.
3. Para el **cruce** de la MT: HDD con recubrimiento **bajo la cota de socavación** calculada, nunca zanja abierta en el cauce.
4. Verificar además vegetación ribereña (Ley N°20.283) y restricciones del instrumento de planificación territorial aplicable.

### 5.5 Cruce de la faja considerada para Engie

Es una cuestión **contractual y de terceros, no normativa**. Verificar si esa faja está constituida como servidumbre inscrita, su ancho, su exclusividad y si admite cruces. Si está inscrita, el cruce requiere acuerdo con el titular. Recomendación: resolverlo antes de consolidar el trazado, porque un "no" de Engie obliga a rediseñar la llegada a la S/E.

### 5.6 Accesos a las parcelas

Los accesos desde camino público requieren también autorización de Vialidad. Conviene tramitarlos **en el mismo expediente** que el atravieso de MT, para no abrir dos frentes ante la misma Dirección Regional.

---

## 6. Ingreso al SEIA: el nivel de tensión y la longitud importan

Conforme al art. 3 letra b) del DS N°40/2012 (Reglamento del SEIA), son líneas de transmisión eléctrica de alto voltaje las que conducen energía con tensión **mayor a 23 kV** y —tras la modificación reglamentaria vigente desde enero de 2026— **cuyo trazado presente una longitud superior a 2 km**.

Esto abre tres escenarios para la LMT de interconexión:

| Escenario | Consecuencia |
|---|---|
| MT ≤ 23 kV | No gatilla por este literal, cualquiera sea la longitud |
| MT > 23 kV y trazado ≤ 2 km | No gatilla por este literal (criterio nuevo desde enero 2026) |
| MT > 23 kV y trazado > 2 km | **Ingresa al SEIA** |

De las coordenadas recuperables del DWG adjunto por el EPC, la extensión del conjunto de áreas es del orden de **1,8 km × 1,75 km (diagonal ≈ 2,5 km)** —muestra parcial, sólo referencial—, por lo que **es probable que el trazado supere los 2 km** y que, si la MT es de 33 kV, el tercer escenario aplique.

**Acción:** pedir al EPC la tensión nominal de MT y la longitud del trazado, y evaluar pertinencia ante el SEA. Sea cual sea el resultado, el trazado y la estrategia de servidumbres deben quedar consistentes con lo que se declare ambientalmente para la Fase II.

---

## 7. Resumen ejecutivo de respuestas

| Pregunta | Respuesta |
|---|---|
| **¿Qué ancho de canalización soterrada?** | **3,6–3,8 m** a nivel de lecho para las 6 ternas (18 cables de 400 mm²) con separación de 0,50 m entre ternas; **1,45–1,55 m** de profundidad. Comprimible a 2,6 m con *s* = 0,30 m, a costa de derating térmico |
| **¿Qué franja de servidumbre?** | Franja de seguridad normativa (RPTD N°07) = **2 × ancho de zanja ≈ 7,2 m**. Franja de servidumbre a escriturar: **10 m**. Ocupación temporal en obra: **15 m** |
| **¿Es viable el paralelismo en faja fiscal?** | Legalmente sí, pero **no como caso base**: permiso precario, relocalización a costo propio, y los fosos de empalme no caben en la faja. Usar la faja vial para el **atravieso** de la ruta pública y tramos cortos inevitables |
| **¿Obligatoriamente por terrenos privados?** | No es obligatorio, pero **sí es lo recomendable**: servidumbre voluntaria de 10 m por escritura pública inscrita en el CBR, **incorporada ahora a la negociación en curso con los propietarios** |

---

## 8. Acciones inmediatas

| # | Acción | Responsable | Prioridad |
|---|---|---|---|
| 1 | Incorporar la franja de 10 m de la LMT a las escrituras de servidumbre en negociación con propietarios | Desarrollo / Legal | **Crítica — ventana abierta** |
| 2 | Confirmar al EPC: n° de ternas, tensión nominal MT, longitud de trazado, criterio de derating | PM / EPC | Alta |
| 3 | Aclarar la inconsistencia 22→31 inversores vs. "19 adicionales" y si 249,88 MWp / 208 MWn son totales F1+F2 | PM / EPC | Alta |
| 4 | Solicitar al titular de la LAAT 500 kV el decreto de concesión y los planos de servidumbre inscritos | Legal / Desarrollo | Alta |
| 5 | Ensayo de resistividad térmica del suelo en la traza (condiciona el ancho final) | EPC | Alta |
| 6 | Estudio hidráulico del estero (crecida T=100 y socavación) | EPC | Media |
| 7 | Consulta previa a la Dirección Regional de Vialidad de O'Higgins por el atravieso | Permisos | Media |
| 8 | Definir con Engie la condición de cruce de su faja | Desarrollo | Media |
| 9 | Evaluar pertinencia SEIA de la LMT según §6 | Medio Ambiente | Media |
| 10 | Relocalizar las instalaciones auxiliares permanentes de Fase I fuera de la franja de 500 kV | EPC | Media |

---

## 9. Referencias

**Normativa eléctrica**
- DFL N°4/20.018, de 2006 — Ley General de Servicios Eléctricos (texto refundido del DFL N°1/1982, Minería)
- DS N°109, de 2017, Ministerio de Energía — Reglamento de Seguridad de las Instalaciones Eléctricas
- Pliego Técnico Normativo **RPTD N°07**, "Franja y distancias de seguridad", SEC — https://www.sec.cl/sitio-web/wp-content/uploads/2020/09/Pliego-T%C3%A9cnico-Normativo-RPTD-N%C2%B007-Franja-y-distancia-seguridad.pdf
- Pliego Técnico Normativo **RPTD N°11**, "Líneas de alta tensión", SEC — https://www.sec.cl/sitio-web/wp-content/uploads/2020/09/Pliego-T%C3%A9cnico-Normativo-RPTD-N%C2%B011-L%C3%ADneas-de-alta-tensi%C3%B3n.pdf
- Pliego Técnico Normativo **RPTD N°13**, "Líneas eléctricas de media y baja tensión", SEC — https://www.sec.cl/sitio-web/wp-content/uploads/2020/09/Pliego-T%C3%A9cnico-Normativo-RPTD-N%C2%B013-L%C3%ADneas-el%C3%A9ctricas-de-media-y-baja-tensi%C3%B3n.pdf
- ChileAtiende, Concesión eléctrica definitiva — https://www.chileatiende.gob.cl/fichas/2680-concesion-electrica-definitiva

**Faja vial y caminos públicos**
- DFL N°850, de 1997, MOP — Ley de Caminos (texto refundido de la Ley N°15.840 y del DFL N°206/1960)
- Dirección de Vialidad — Permiso de ocupación de faja vial (paralelismo y/o atraviesos) — https://vialidad.mop.gob.cl/gestion-vial/permiso-de-ocupacion-de-faja-vial-paralelismo-y-o-atraviesos/
- ChileAtiende, ficha N°56612 — Permiso de ocupación de faja vial en caminos públicos — https://www.chileatiende.gob.cl/fichas/56612-permiso-de-ocupacion-de-faja-vial-en-caminos-publicos-paralelismo-y-o-atraviesos
- Dirección de Vialidad, Res. DV N°2059 — Instructivo sobre Paralelismos y Atraviesos en Caminos Públicos
- Ministerio de Energía — Revisión y análisis de proyectos de paralelismo y solicitud de uso de faja fiscal — https://energia.gob.cl/sites/default/files/3_solicitud_de_uso_de_faja_fiscal_-_modo_de_compatibilidad.pdf

**Ambiental y aguas**
- DS N°40, de 2012, MMA — Reglamento del SEIA, art. 3 letra b) — https://www.bcn.cl/leychile/navegar?idNorma=1053563
- Texto refundido DS N°40 (SEA, 2024) — https://www.sea.gob.cl/en/sites/default/files/imce/archivos/2024/05/30/DS40_Refundido2024_SEA.pdf
- Modernización del Reglamento del SEIA (vigente enero 2026): umbral adicional de 2 km de trazado — https://www.reporteminero.cl/noticia/noticias/2026/01/modificacion-reglamento-seia-nuevos-umbrales-excepciones
- Código de Aguas, arts. 30 y ss., 41 y 171 — obras en cauces naturales

**Terreno fiscal**
- `docs/cronograma-cuo-mbn.md` — Cronograma de adjudicación de CUO del Ministerio de Bienes Nacionales (DL N°1.939/1977)

---

## 10. Limitaciones

- Los anchos de zanja son **dimensionamiento geométrico preliminar**. El ancho final es resultado de un cálculo térmico (IEC 60287) que requiere resistividad térmica del suelo, temperatura ambiente del terreno y factor de carga: datos que hoy no existen, como advierte el propio EPC.
- El Ø exterior del cable (48 mm) es un valor típico de catálogo para 400 mm² Al XLPE 18/30 kV; debe reemplazarse por el del cable efectivamente especificado.
- Los valores de la Tabla N°3 del RPTD N°07 para 500 kV no se transcriben aquí por no haberse podido verificar el documento fuente en esta revisión; se cita el método, no el número.
- Las exigencias específicas de la Dirección Regional de Vialidad de O'Higgins pueden ser más estrictas que el Instructivo general. Validar en consulta previa antes de comprometer trazado o plazos.
- La extensión inferida del DWG proviene de una muestra parcial de coordenadas recuperables del archivo comprimido; es referencial y no sustituye la medición sobre el layout.
