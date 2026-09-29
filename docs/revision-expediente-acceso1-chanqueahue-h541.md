# Revisión Técnica — Expediente Solicitud de Acceso N°1, Ruta H-541 Km 2,058

**Proyecto:** Parque Fotovoltaico Chanqueahue 150 MWn
**Titular:** GR Las Chinchillas SpA
**Proyectista:** Barrios Vera Ingenieros SpA
**Documentos revisados:**
- `BVI-741-26-DOC-IN-ACC1-CHA-H541-001-B` — Memoria Proyecto de Ingeniería (Rev. B, 23-07-2026)
- `BVI-741-26-DOC-ET-ACC1-CHA-H541-001-B` — Especificaciones Técnicas (Rev. B, 23-07-2026)

**Fecha de revisión:** 29-09-2026
**Destinatario del expediente:** Dirección Regional de Vialidad, Región del Libertador Bernardo O'Higgins — MOP

---

## 1. Resumen ejecutivo

El expediente está bien estructurado y sigue la lógica esperada por Vialidad (antecedentes → localización → situación actual → tránsito → diseño geométrico → sección transversal → pavimentos → señalización → saneamiento → presupuesto), con Especificaciones Técnicas correctamente referidas al Manual de Carreteras Volumen 5.

**Todos los cálculos numéricos verificables fueron recalculados y son correctos** (ver §7). El problema del expediente no es de cálculo, sino de **consistencia, trazabilidad y completitud de respaldos**.

Se identificaron **3 observaciones críticas** que pueden motivar rechazo o requerimiento de antecedentes adicionales, **8 observaciones mayores** y **un conjunto de observaciones menores y de forma**.

| Severidad | Cantidad | Efecto probable |
|---|---:|---|
| Crítica | 3 | Rechazo o requerimiento formal de antecedentes |
| Mayor | 8 | Observación con plazo de subsanación |
| Menor / forma | 18 | Observación de detalle |

---

## 2. Observaciones CRÍTICAS

### C-1. Contradicción en el tránsito de diseño: 3,4 veh/h vs. 150 camiones/día

Es la observación de mayor riesgo del expediente, porque afecta simultáneamente la **elección del tipo de acceso** y el **diseño de pavimento**.

- El **Capítulo 6 (Tránsito)** declara: *"un flujo promedio de ingreso y salida por el acceso de 3,4 veh/h, asumiendo que el flujo diario de todo el proyecto se da en una jornada de 10 horas"*.
- El **Capítulo 9.1 (Tránsito para pavimentos)** usa `NtotCS = 54.750` camiones simples acumulados. Si ese total corresponde a los 12 meses de construcción, equivale a **150 camiones simples/día** (54.750 / 365), es decir **~15 camiones/h en jornada de 10 h**, sólo camiones simples y sin contar buses ni livianos.

Ambas cifras no pueden ser ciertas a la vez. Las consecuencias son directas:

1. **Elección del acceso tipo.** El Capítulo 7 justifica el uso de la Lámina 4.706.001 del MC-V4 (Acceso Tipo para volúmenes **< 25 veh/h**) sobre la base de los 3,4 veh/h. Si el flujo real de construcción se acerca a los 150 vehículos pesados diarios, en hora punta se superan holgadamente los 25 veh/h y **el acceso tipo aplicado deja de ser el normativamente procedente**, debiendo evaluarse un acceso de mayor estándar con pistas de cambio de velocidad.
2. **Diseño de pavimento.** Si, por el contrario, los 54.750 camiones son el acumulado de los 35 años de operación (54.750 / 35 / 365 ≈ 4,3 camiones/día), entonces **el tránsito de la etapa de construcción —que es el más pesado y el que rige— no estaría incorporado en el cálculo estructural**, y el pavimento estaría subdimensionado.

**Acción requerida:** incorporar en el Capítulo 9.1 la memoria de cálculo explícita del tránsito acumulado, separando **construcción (12 meses)** y **operación (35 años)** y mostrando la suma, con la trazabilidad hacia las Tablas 2 y 3. Verificar en consecuencia si la Lámina 4.706.001 sigue siendo aplicable o si corresponde un acceso de mayor estándar.

---

### C-2. El acceso solicitado no coincide con el punto autorizado en la factibilidad

La Introducción señala que la factibilidad fue otorgada por **Ord. N°378 del 16-03-2026** para el **Km 2,0**, y que el acceso se reubicó al **Km 2,058** (58 m de desplazamiento) *"debido a condiciones particulares del sector que impedían la ubicación original"*.

Problemas:

- **No se acompaña respaldo técnico ni gráfico** de por qué el Km 2,0 era inviable (levantamiento topográfico del punto original, registro fotográfico, interferencias, deslinde predial, visibilidad).
- **No consta que se haya solicitado formalmente la modificación de la factibilidad.** Vialidad puede observar que se está solicitando un acceso en un punto distinto al autorizado.
- **Vigencia de la factibilidad:** el Ord. N°378 es de marzo de 2026. Si el expediente se ingresa a fines de septiembre de 2026, debe verificarse que la factibilidad siga vigente (las factibilidades suelen tener plazo de caducidad).

**Acción requerida:** (a) incorporar un acápite específico con el respaldo técnico y gráfico de la reubicación; (b) solicitar formalmente a Vialidad la actualización/ratificación de la factibilidad para el Km 2,058, o bien acompañar el pronunciamiento si ya existe; (c) verificar vigencia del Ord. N°378 antes de ingresar.

---

### C-3. Ausencia de verificación de distancias de visibilidad

El diseño **elimina las cuñas de entrada y salida de 20 m** que la Lámina 4.706.001 del MC-V4 define, conectando directamente el radio de 15 m con la calzada de la ruta. Se justifica por la existencia de postación eléctrica y porque los ingresos se realizarán desde el sur.

Sin embargo, el expediente **no contiene ninguna verificación de distancia de visibilidad**: ni distancia de parada, ni distancia de visibilidad de cruce/entrada, ni el triángulo de visibilidad del acceso. Esta verificación es exigencia normativa y es precisamente lo primero que Vialidad revisa cuando se omiten las cuñas, porque:

- Sin cuña de salida, los vehículos que ingresan al predio **deceleran sobre la calzada de la ruta**, generando un diferencial de velocidad con el tránsito pasante.
- El vehículo de diseño es un **cama baja de 18,08 m** maniobrando a 10 km/h, lo que implica tiempos de despeje largos.
- El tramo es llano y predominantemente recto, por lo que **la velocidad de operación real (V85) puede ser superior a los 50 km/h estimados** (ver M-3).

**Acción requerida:** incorporar un capítulo de verificación de distancias de visibilidad conforme al MC-V3 (3.202) para la velocidad de operación acreditada, incluyendo el triángulo de visibilidad, y evaluar si la eliminación de las cuñas es sostenible o si corresponde al menos conservar la cuña de deceleración/salida, o gestionar el traslado de la postación.

---

## 3. Observaciones MAYORES

### M-1. Contradicción en la geometría existente de la Ruta H-541

| Fuente | Ancho calzada | Bermas |
|---|---|---|
| **Cap. 5** — Caracterización de la situación actual | 5,4 m promedio | **sin bermas** |
| **Cap. 8.1** — Diseño de la sección transversal | 5,5 m promedio | **con bermas a ambos lados** |

Dos contradicciones directas sobre la misma geometría existente, en el mismo documento. Vialidad conoce el estado de sus rutas y esta inconsistencia resta credibilidad al levantamiento. Debe corregirse contra el plano de topografía y dejar una única descripción.

### M-2. Inconsistencia aritmética en la sección transversal del camino de acceso

El Cap. 8.1 declara plataforma de **8,0 m**, con pistas de 3,0 m (calzada 6,0 m), bermas de 0,5 m y SAP de 0,5 m.

```
6,0 (calzada) + 0,5 + 0,5 (bermas) = 7,0 m
7,0 + 0,5 (SAP) = 7,5 m  ≠  8,0 m declarados
```

La cifra sólo cuadra si el SAP de 0,5 m es **por lado** (7,0 + 1,0 = 8,0 m), pero la redacción actual (*"Se ha definido un SAP de 0,5 m"*) no lo precisa. Debe aclararse explícitamente.

### M-3. Velocidad de operación sin respaldo

El Cap. 5 indica *"La velocidad máxima de operación se estima de 50 km/hr, de acuerdo con las condiciones existentes y el tipo de ruta"*. Es una estimación sin medición ni respaldo.

Dado que el tramo es llano y recto, la V85 real puede ser mayor. La velocidad de operación es el parámetro que gobierna las distancias de visibilidad (C-3), el emplazamiento longitudinal de la señalización y la extensión de la zona de no adelantamiento. **Debe acreditarse** con medición de terreno, con el dato de Vialidad o con la señalización reglamentaria existente en el tramo.

### M-4. Incoherencia entre el supuesto de "sin virajes a la izquierda" y la señalización propuesta

El Cap. 7.1 establece que *"no se proyectan virajes a la izquierda en el acceso (condición restrictiva de acuerdo con diseño de acceso único en calzadas bidireccionales según Lámina 4.706.001)"*.

Sin embargo:

- El Cap. 10 (Señalización y Seguridad Vial) **sólo menciona la señalización "No Adelantar"**. No se indica ninguna señal de prohibición de viraje a la izquierda (RPI), ni demarcación, ni elemento físico que materialice la restricción.
- Las simulaciones AutoTurn (Figuras 6 y 7) cubren únicamente **ingreso desde el sur** y **salida hacia el sur**. No se verifica ni se impide la maniobra desde/hacia el norte, que físicamente sigue siendo posible.

Si la restricción es una condición de diseño, debe materializarse en el plano de seguridad vial y en las ET. De lo contrario, debe verificarse la maniobra desde el norte.

### M-5. Contradicción interna en la ET 404-1 Cape Seal

En **Materiales** se especifica: *"considerando **emulsiones tradicionales no modificadas**"*.

En **Procedimientos de Trabajo** se indica: *"En ninguna circunstancia el Contratista comenzará la aplicación del **cape seal con polímero** antes de obtener la visación del Laboratorio de Vialidad"*.

Contradicción directa (emulsión no modificada vs. con polímero). Es un arrastre de una ET de otro proyecto. Debe corregirse y definir inequívocamente el tipo de emulsión, ya que determina precio y control de recepción.

### M-6. Desalineación entre la Memoria y las Especificaciones Técnicas

Las ET especifican partidas que **la Memoria no describe en ninguna parte**:

| Partida en ET | ¿Descrita en la Memoria? |
|---|---|
| 401-1 Imprimación | **No** — la "Estructuración Propuesta" del Cap. 9 sólo señala Base Granular 200 mm + Cape Seal |
| 607-1 Soleras Tipo A | **No** — no se mencionan soleras en la sección transversal, el diseño geométrico ni el saneamiento |
| 704-7 / 704-8 Demarcación | **No** — el Cap. 10 sólo trata señalización vertical |
| 201-3 Excavación / 205-1 Terraplenes | **No** — el Cap. 7.2 indica que la rasante del acceso coincide con la de la ruta; no se describe movimiento de tierras |

La Memoria y las ET deben ser coherentes entre sí y con el presupuesto. En particular, las **soleras tipo A** son un elemento visible del diseño (confinamiento del cuello de acceso) que debería estar descrito y grafiado.

### M-7. Partidas faltantes en las Especificaciones Técnicas

- **Señalización transitoria de obras / manejo de tránsito durante la construcción.** El Anexo lista un "Plano Seguridad Vial de Obras", pero no existe la partida ni un capítulo en la Memoria que describa el desvío y control de tránsito conforme al MC-V6, Capítulo 6.3. Vialidad lo exige siempre que se interviene la calzada de una ruta pública.
- **Mejoramiento de subrasante.** El diseño de pavimento asume un CBR de 20% señalando que el suelo *"se mejorará de tal manera de alcanzar un CBR de 20%"*, pero las ET sólo incluyen 209-1 Preparación de la Subrasante. No hay partida de mejoramiento ni de subbase granular.
- **Escarpe / remoción de capa vegetal**, habitual en terreno agrícola.
- **Replanteo y topografía**.
- **Traslado o protección de la postación eléctrica**, que es precisamente la interferencia que condiciona el diseño (eliminación de cuñas). Si hay intervención, debe declararse la coordinación con la empresa distribuidora; si no la hay, debe declararse expresamente.

### M-8. El CBR de subrasante de 20% no está respaldado

El espesor mínimo `e_min = 592 − 308·log(CBR) = 191,3 mm` depende enteramente del CBR de subrasante adoptado (20%). El expediente **no acompaña ensayos de mecánica de suelos** ni prospecciones que acrediten el CBR natural, ni cuantifica el mejoramiento necesario para alcanzar el 20%. Sin ese respaldo, el diseño de pavimento no es verificable por el revisor.

---

## 4. Observaciones sobre el saneamiento

El Cap. 11 despacha el saneamiento en un párrafo, concluyendo que no se proyectan obras porque *"la pendiente del camino interno escurre hacia el interior del predio"* y el canal está en el lado izquierdo (opuesto al acceso).

El razonamiento es defendible, pero **no está verificado**. Se recomienda incorporar:

- Verificación de que el acceso **no aporta caudal ni sedimentos a la calzada** de la Ruta H-541.
- Verificación de que **no se altera el escurrimiento longitudinal** de la plataforma de la ruta en el sector del cuello (continuidad del bombeo y de la evacuación existente).
- Confirmación explícita de que **no se intercepta ni afecta el canal** del costado izquierdo, con referencia al plano de topografía.
- Definición del tratamiento del empalme para que las aguas de la ruta no ingresen al predio ni viceversa.

---

## 5. Observaciones MENORES y de forma

### 5.1 Memoria

| # | Observación |
|---|---|
| m-1 | **EIA vs. DIA.** La Introducción y la Figura 1 citan *"Estudio de Impacto Ambiental"*; la Figura 2 cita *"Declaración de Impacto Ambiental"*. Unificar (según el texto, corresponde EIA en calificación). |
| m-2 | **Nombre del proyecto.** Portada y títulos: *"Parque Fotovoltaico Chanqueahue 150 MWn"*; Introducción: *"Parque Fotovoltaico y Sistema BESS Chanqueahue 150 MWn"*. Unificar. |
| m-3 | **Razón social.** Portada: *"GR Las Chinchillas SpA"*; Cap. 2: *"la empresa Las Chinchillas SpA"*. Unificar. |
| m-4 | **Correo del representante legal.** Se individualiza a Antonio Ros Mesa con el correo `vvera@grenergy.eu`, que no corresponde al titular indicado. Corregir o aclarar. |
| m-5 | **Cuadro de revisiones.** Las tres filas tienen Preparó/Revisó completos, pero la columna **"Aprobó" está vacía en todas** y sólo la Rev. B tiene letra y fecha. Completar antes de presentar. |
| m-6 | **Numeración de capítulos.** El cuerpo del documento presenta los títulos sin numerar (INTRODUCCIÓN, GENERALIDADES, …) y al final aparecen *"1. SANEAMIENTO"* y *"1. PRESUPUESTO ESTIMATIVO"* en lugar de 11 y 12. Error de numeración automática; el índice sí está correcto. |
| m-7 | **Vehículo de diseño — redacción contradictoria.** Se declara un cama baja de 18,08 m y a la vez *"no se considera el uso de camiones de más de dos ejes de largo mayor a 20 m"*. Un cama baja de 18 m tiene más de dos ejes. Reformular. |
| m-8 | **Transporte del transformador de potencia.** Para una S/E elevadora de un parque de 150 MWn con BESS, el transformador suele requerir transporte especial de mayor longitud/peso que el cama baja de 18,08 m. Verificar y, si aplica, declarar por qué acceso ingresa. |
| m-9 | **Referencia normativa de accesos.** Se menciona genéricamente *"las Normas sobre Accesos a Caminos Públicos"*. Conviene citar el decreto vigente y los artículos aplicables. |
| m-10 | **Zona de no adelantamiento.** Se propone señalización "No Adelantar" a 200 m a ambos lados, sin justificación de cálculo de esa distancia y sin mencionar la demarcación de eje (línea continua) asociada. Las ET incluyen 704-7 (línea lateral continua) y 704-8, pero no se explicita la línea de eje. |
| m-11 | **Superficies del proyecto.** El desglose suma 222,67 ha (188,39 + 0,42 + 1,44 + 15,27 + 17,15) frente a las 278,73 ha declaradas: quedan 56,06 ha (20%) en *"entre otras"*. Conviene detallar. |
| m-12 | **Localización.** Se indica *"10 km aproximadamente al sur poniente del centro de la ciudad de Rengo"*. Verificar contra las coordenadas declaradas (334.910,047 E / 6.195.129,339 N, WGS84 19S) con SIG, y ajustar distancia y rumbo si corresponde. |
| m-13 | **Precisión de coordenadas.** Se entregan con milímetro de precisión (3 decimales), heredado de CAD. Basta el centímetro o el metro. |
| m-14 | **Alcance del expediente.** La Introducción menciona los Accesos N°2 y N°3 en la Ruta S/R-H-543 Km 1,259. Confirmar que cuentan con expediente propio y que el Ord. N°378 los cubre. |
| m-15 | **Falta capítulo de plazo de ejecución y compromiso de mantención** del acceso por parte del titular, habitualmente requerido. |
| m-16 | **Registro del proyectista.** No se indica el N° de inscripción del ingeniero en el Registro de Consultores del MOP. |

### 5.2 Especificaciones Técnicas

| # | Observación |
|---|---|
| e-1 | **Numeración de ítems.** En todas las partidas los cuatro acápites (Descripción, Materiales, Procedimientos, Unidad de Medida y Pago) aparecen numerados como "1." Error de numeración automática en todo el documento. |
| e-2 | **Error de codificación en 302-1.** Aparece *"CBR ³ 80%"* en lugar de *"CBR ≥ 80%"* (fuente Symbol mal convertida). Aparece en el cuerpo de la partida, aunque el título sí usa "≥". |
| e-3 | **302-1 — referencia dudosa.** Se citan *"las Especificaciones 8.101.1, punto 4, y 5.302.2"*. Verificar la cita al Volumen 8; los requisitos de calidad y graduación de bases granulares corresponden a 5.302.2 del MC-V5. |
| e-4 | **401-1 — errata:** *"PROCEDIMIENTOSDE TRABAJO"* (falta espacio). |
| e-5 | **702 — referencia desactualizada.** Se remite al *"Manual de Señalización de Tránsito 'Señales Verticales' del MTT, Año 2012"*, mientras la Memoria declara haber usado el Manual vigente. Actualizar a la versión vigente del Capítulo 2. |
| e-6 | **Edición del Manual de Carreteras.** La Memoria cita expresamente el MC año 2025; las ET citan secciones sin indicar edición. Agregar la edición en las ET para evitar ambigüedad en la recepción. |
| e-7 | **607-1 Soleras Tipo A.** Verificar que el tipo A esté grafiado en los planos y que su extensión esté cuantificada en el presupuesto, dado que la Memoria no las menciona (ver M-6). |

---

## 6. Antecedentes no verificables en el archivo entregado

En la versión revisada (conversión a texto), **la totalidad de las tablas con datos y de las figuras están vacías**:

| Elemento | Contenido esperado | Estado |
|---|---|---|
| Tabla 2 | Flujo de vehículos — etapa de construcción | Vacía |
| Tabla 3 | Flujo de vehículos — etapa de operación | Vacía |
| Tabla 4 | Coeficientes estructurales Morin-Todor | Vacía |
| Tabla 5 | Estructura propuesta e IE resistente | Vacía |
| Tabla 6 | Presupuesto estimativo | Vacía |
| Figuras 1 a 9 | Localización, acceso tipo, diseño, simulaciones, seguridad vial | Sólo pies de figura |
| Fórmulas | `e_min = f(CBR)` y `IE = f(EE, CV)` | Sólo aplicación numérica |

Esto puede deberse exclusivamente a la conversión del archivo. **Debe verificarse en el PDF/Word final** que todas las tablas, figuras y ecuaciones estén presentes y legibles antes de ingresar el expediente: sin ellas, el revisor de Vialidad no puede verificar el tránsito de diseño, los coeficientes estructurales, la estructura propuesta ni el presupuesto.

Como consecuencia de lo anterior, **el valor `IE_resistente = 412,8 mm` no pudo ser verificado**, porque depende de la Tabla 5 (estructura propuesta) y la Tabla 4 (coeficientes). Se hace notar además que el método Morin-Todor asume 900 mm de estructura (0–250 base, 250–500 subbase, 500–900 subrasante) y la estructuración propuesta sólo define **200 mm de base granular**; la definición de los 700 mm restantes debe quedar explícita en la Tabla 5.

---

## 7. Verificación de cálculos

Se recalcularon todos los valores numéricos presentados. **Todos verifican correctamente.**

| Cálculo | Valor en el documento | Recalculado | ✓ |
|---|---|---|:---:|
| `e_min = 592 − 308·log(20)` | 191,3 mm | 191,28 mm | ✓ |
| `EE = 54.750×0,71 + 1.460×2,01 + 5.110×1,90` | 51.516 | 51.516,1 | ✓ |
| `IE_EE = 1024·(0,25)^0,354·[(9,56/(11,49−log EE))−1]` | 257,28 mm | 257,28 mm | ✓ |
| Verificación `IE_EE < IE_resistente` | 257,28 < 412,8 | consistente con los valores dados | ✓ (*) |
| Espesor base 200 mm ≥ e_min 191,3 mm | OK | OK | ✓ |
| Potencia: 271.040 paneles × 665 W | 180,24 MWp | 180,24 MWp | ✓ |

(*) La comparación es aritméticamente correcta, pero `IE_resistente` no es verificable de forma independiente (ver §6).

**Observación de método:** el cálculo no incorpora factor de crecimiento del tránsito durante los 35 años de operación. El método Morin-Todor trabaja con ejes equivalentes en ambas direcciones, por lo que no requiere factor de distribución por pista; sin embargo, conviene declarar explícitamente ese supuesto. Adicionalmente, la zona del radio de 15 m invade la calzada de la Ruta H-541 y por tanto recibe también el tránsito pasante de la ruta, el cual no está considerado en el cálculo: debe aclararse el alcance del diseño estructural en esa superficie.

---

## 8. Plan de subsanación sugerido

**Antes de ingresar a Vialidad:**

1. Resolver **C-1**: rehacer y explicitar la memoria de cálculo del tránsito (construcción + operación), y confirmar la aplicabilidad de la Lámina 4.706.001.
2. Resolver **C-2**: respaldo técnico de la reubicación al Km 2,058 y gestión formal ante Vialidad; verificar vigencia del Ord. N°378.
3. Resolver **C-3**: incorporar capítulo de verificación de distancias de visibilidad.
4. Corregir **M-1** y **M-2** (inconsistencias de geometría y aritmética de la sección transversal).
5. Acreditar **M-3** (velocidad de operación) y **M-8** (CBR de subrasante).
6. Alinear Memoria ↔ ET ↔ Presupuesto (**M-6**) e incorporar las partidas faltantes (**M-7**).
7. Corregir la contradicción de la ET de Cape Seal (**M-5**) y materializar la restricción de viraje izquierdo (**M-4**).
8. Ampliar el capítulo de saneamiento (§4).
9. Verificar que el PDF final contenga todas las tablas, figuras y ecuaciones (§6).
10. Corregir observaciones de forma (§5) y completar el cuadro de revisiones (emitir Rev. C).
