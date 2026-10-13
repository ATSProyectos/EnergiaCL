# Estrategia de tramitación — Chanqueahue Fase 1 (150 MW) y Fase 2 (~100 MW)

**Objeto:** confirmar la estrategia de tramitación para desarrollar la Fase 2 de Chanqueahue como ampliación que utiliza la misma conexión al SEN, y definir secuencia de hitos, titularidad y vía regulatoria.
**Fecha:** 13 de octubre de 2026 · **Versión:** 3.0

> **Documento complementario.** La arquitectura de SPV, la asignación de activos y permisos entre vehículos, y la estrategia para que las dos tramitaciones ante el SEA sean independientes están en **`estructura-spv-chanqueahue-fase2.md`**. Ese documento es posterior y, donde haya diferencia, prevalece: incorpora los antecedentes del hilo *RE: Chanqueahue FASE II* (hasta el 13.10.2026), entre ellos la decisión de usar una SPV separada para la Fase 2, lo que **cierra la vía del fehaciente** para ella (§3, vía B) y la reemplaza por contrato de transporte más SUCTD.

> **Advertencia de verificación.** Los hosts `coordinador.cl`, `sea.gob.cl`, `cne.cl`, `sec.cl` y `bcn.cl` están bloqueados por la política de red del entorno en que se elaboró este documento, de modo que los documentos primarios no pudieron abrirse directamente. El análisis se construyó sobre fuentes secundarias y citas indirectas (§9). Los puntos marcados **[V]** deben verificarse contra el texto vigente antes de accionarse.

---

## 0. Síntesis para decisión

| # | Conclusión | Consecuencia |
|---|---|---|
| 1 | **La conexión tiene dos capas, no una.** La capacidad en el punto de conexión al SEN la da la SAC/IAC por 250 MW. El uso de la SET elevadora y la LAT —instalaciones **dedicadas** propias— se gobierna por un régimen distinto: proyecto fehaciente, SUCTD o capacidad contratada. | La pregunta de Cristian ("¿habría que meter otra SAC?") y la respuesta de Mario ("solicitamos un fehaciente") responden a **capas distintas**: ambas son correctas en la suya. Con la SET y la LAT dimensionadas para 250 MW, **no se requiere una segunda SAC**. |
| 2 | **El riesgo dominante es la ventana de acceso abierto, no la caducidad.** El IAC por 250 MW se publica (ene-2027) mientras solo 150 MW están declarados: eso señaliza al mercado una SET con holgura. El art. 79 inc. 2º LGSE solo protege la capacidad contratada y los proyectos propios declarados fehacientemente **"al momento de la solicitud"** de un tercero. | Desde ene-2027 y hasta que exista fehaciente o contrato, los 100 MW son contestables por SUCTD de un tercero. **Esta es la ventana que hay que cerrar primero.** |
| 3 | **La intuición de Mario sobre el "mismo titular" es correcta, y ahora se sabe por qué.** El criterio de aplicación del Coordinador es que solo califican como fehacientes los proyectos **del mismo propietario** cuyas instalaciones dedicadas se usarán; los de terceros van por SUCTD. | Mantener una sola SPV hasta cerrar el IAC es lo que deja disponible la vía más rápida y barata. Su secuencia —consolidar, cerrar, separar antes del instrumento de Capa 2— es la correcta. |
| 4 | **Con las fechas confirmadas, la caducidad pasa a ser un riesgo administrable.** IAC ene-2027 → DEC ene-2029 → prórroga única hasta ene-2031. Inicio de construcción Fase 1 objetivo ene-2028. | La Fase 2 tiene entre 2 y 4 años para llegar a su propia DEC. Condición operativa: **ingresar la DIA de la Fase 2 durante 2027**, porque la prórroga es discrecional y se concede sobre avance acreditado, no por el solo transcurso del plazo. |
| 5 | **La separación de ≥2 km entre predios es una buena noticia y cambia el análisis ambiental.** Debilita de forma significativa la lectura de unidad de proyecto y hace defendible una DIA independiente para la Fase 2. | El vínculo funcional que queda —SET elevadora y BESS compartidos— es lo único sobre lo que podría construirse un reproche. Es gestionable documentalmente. |
| 6 | **Aparece una palanca de diseño con consecuencia de permisos: el nivel de tensión de la línea MT.** El DS 17/2025 subió el umbral de la tipología b.1 a **>23 kV *y* trazado de 2 km**. El trazado de la Fase 2 ya supera los 2 km, de modo que **la tensión decide** si la línea es tipología por sí sola. | A ≤23 kV la línea queda fuera de la tipología b.1; sobre 23 kV, dentro. Pero mover ~100 MW en MT sobre 2 km es exigente eléctricamente (§4.3): hay que decidir el *trade-off* conscientemente, no por defecto. |
| 7 | **Existe una cuarta vía que no se discutió: la capacidad contratada.** El art. 79 inc. 2º exceptúa del acceso abierto tanto los proyectos propios declarados fehacientemente *como* la **capacidad contratada**. | Es el plan B si el criterio de identidad de titular resulta restrictivo, y la única vía que protege la capacidad **con SPV distintas**. |

---

## 1. Punto de partida

### 1.1 Datos confirmados

| Elemento | Dato |
|---|---|
| Capacidad solicitada en la SAC | 250 MW |
| Etapa del proceso de conexión | En elaboración del Informe de Autorización de Conexión **Preliminar** |
| Fase 1 | 150 MW solar + BESS propio colindante; es la que obtendrá RCA y concesión eléctrica, y sobre la cual se hará la DEC |
| Fase 2 | El delta (~100 MW), **solo solar** |
| Dimensionamiento de SET elevadora y LAT | **250 MW** (holgura de 100 MW disponible) |
| Punto de conexión al SEN | **S/E Totihue**, vía LAT desde la SET elevadora de la Fase 1 |
| Conexión y emplazamiento de la Fase 2 | **Dos sectores**: ~30 ha cercanas en MT directo a la SET elevadora, y 120–150 ha lejanas agrupadas en **AT con línea de ~3,3 km**. Dato a reconciliar: con posterioridad se manejó MT para el sector lejano |
| Superficie con acuerdos en avance | **148,7 ha**; rango en definición 120–180 ha |
| Concesión eléctrica SEC | **Ya dimensionada a 250 MW**; sin cambios por la nueva fase |
| SPV de la Fase 2 | **GR Laguna San Rafael SpA**, RUT 77.134.068-7 (ex proyecto Charquecillo) |
| Fecha estimada de IAC | **enero 2027** |
| Plazo a DEC | enero 2029, más prórroga de hasta 2 años (enero 2031) |
| Inicio de construcción Fase 1 (objetivo interno) | enero 2028 |
| Propiedad de la infraestructura compartida | SPV de la Fase 1: SET elevadora, LAT a Totihue y BESS |
| Compromisos comerciales con fecha dura | Ninguno por ahora |
| Apetito de riesgo en acceso abierto | Mitigar el riesgo, evaluando el *trade-off* velocidad vs. exposición |

### 1.2 Supuestos pendientes

| # | Supuesto | Por qué importa |
|---|---|---|
| S1 | El punto de conexión al SEN es una S/E de transmisión **nacional o zonal** (servicio público) | Confirma que la vía de la Capa 1 es SAC y no SUCTD sobre instalación ajena |
| S2 | ~~"IFC" = Informe Favorable para la Construcción~~ **Resuelto:** se trata de la **concesión eléctrica ante la SEC**, ya dimensionada a 250 MW | Confirmar si cubre las obras de la Fase 2 o si su línea AT requiere concesión propia |
| S3 | La RCA de la Fase 1 **aún no está aprobada** y no declara etapas | Si ya lo está, la vía ambiental de la Fase 2 cambia (§5) |
| S4 | El BESS colindante es de la Fase 1 y la Fase 2 lo **usaría**, no construiría uno propio | Es un segundo activo compartido: el principal vínculo funcional remanente (§5.2) |

---

## 2. Marco normativo aplicable

| Capa | Norma / instrumento | Contenido relevante |
|---|---|---|
| Conexión al SEN (servicio público) | **DS N° 37/2019**, Minenergía — Reglamento de los sistemas de transmisión | Procedimiento de SAC; contenidos mínimos del IAC Preliminar (art. 21); régimen de acceso abierto **[V]** |
| Conexión — procedimiento | Coordinador: *Procedimiento Interno de Interconexión de Proyectos* (dic-2024) y *Criterios para la Aplicación del Régimen de Acceso Abierto* (DAA-PIC v2, abr-2023) | Etapas y plazos; **una sola oportunidad de modificar la solicitud**; plazo de 24 meses a DEC; prórroga única |
| Instalaciones dedicadas | **Art. 79 inc. 2º LGSE** | El titular no puede negar el servicio habiendo capacidad técnica disponible, *sin perjuicio de la capacidad contratada y de los proyectos propios declarados fehacientemente al momento de la solicitud* |
| Instalaciones dedicadas | **Art. 80 inc. 2º LGSE** | El Coordinador determina fundadamente la CTD, oyendo a las partes; los titulares deben informarle contratos de transporte vigentes y proyectos que usen esa capacidad |
| Proyectos fehacientes | Coordinador, *Consideración y Gestión de Proyectos Fehacientes* | Definición; criterio de aplicación (mismo propietario); consigna de fehaciencia; IACPF |
| Declaración en construcción | **Art. 72°-17 LGSE** y **DS N° 125/2017** (Reglamento de Coordinación y Operación del SEN, D.O. 20.12.2019), Título II Cap. 1 | La CNE declara en construcción solo instalaciones que acrediten, al menos, permisos sectoriales, órdenes de compra y cronograma de obras; seguimiento y revocación por incumplimiento de hitos o cambios significativos |
| Caducidad de capacidad | **Ley N° 20.936** | Transcurrido el plazo sin declaración en construcción, la aprobación caduca y la capacidad vuelve a considerarse disponible **[V]** |
| Ambiental | **Ley N° 19.300, art. 11 bis** | Prohíbe fraccionar *a sabiendas* para variar el instrumento o eludir el SEIA; **excepciona expresamente** los proyectos cuya ejecución se acredite **por etapas** |
| Ambiental | **DS N° 40/2012** (RSEIA), art. 2 g) y art. 3 | Modificación de proyecto; tipologías de ingreso (c) generación, b.1) transmisión |
| Ambiental — reforma vigente | **DS N° 17/2025**, MMA (Contraloría 31.12.2025; D.O. **21.01.2026**) | Ajusta el art. 2 g.1: si la intervención corresponde a la **misma tipología** por la que el proyecto fue calificado, se aplican los criterios generales en lugar de exigir automáticamente nuevo ingreso. Sube el umbral de transmisión a **>23 kV *y* trazado de 2 km** (art. 3 b.1) |

---

## 3. La arquitectura de conexión: dos capas

**Capa 1 — punto de conexión al SEN (transmisión de servicio público).** La da la SAC. Con el IAC emitido por 250 MW y la SET y LAT dimensionadas para esa capacidad, la inyección de la Fase 2 **ya queda autorizada**: no se requiere una segunda SAC, salvo que la Fase 2 modifique el punto de conexión o agregue obras sobre instalaciones de servicio público. Lo único que hay que administrar es la caducidad (§4.2).

**Capa 2 — uso de la SET elevadora, la LAT y el BESS (instalaciones dedicadas propias).** Cuatro caminos:

| Vía | Cómo opera | Requisito de titularidad | Lectura para Chanqueahue |
|---|---|---|---|
| **A. Nueva SAC independiente** | La Fase 2 tramita su propio proceso completo | Indiferente | **Descartable.** Solo aplicaría si la Fase 2 se conectara directo a servicio público con obras propias. Nueva cola, nuevos estudios, compite por capacidad |
| **B. Proyecto fehaciente** | El titular de la instalación dedicada declara su propio proyecto; obtiene consigna de fehaciencia e IACPF | **Mismo propietario** de las instalaciones dedicadas (criterio de aplicación). La definición admite además arrendatario, usufructuario o quien explote a cualquier título **[V]** | **Vía recomendada.** La más rápida y barata, y la que cierra antes la ventana de acceso abierto — siempre que se mantenga identidad de titular hasta declararlo |
| **C. SUCTD de la Fase 2** | La SPV 2, como tercero, solicita uso de la capacidad técnica disponible | Indiferente — es la vía de terceros | Funciona con SPV distintas, pero la CTD se determina y publica, quedando contestable. Es la vía que **obliga** a usar si se separa la titularidad antes de tiempo |
| **D. Capacidad contratada** | Contrato firme de transporte entre el dueño de la SET y la SPV 2; esa capacidad queda excluida de la CTD por art. 79 inc. 2º | **Indiferente** | **Plan B.** Protege la capacidad sin identidad de titular. A validar: el Coordinador revisa los contratos vigentes (art. 80 inc. 2º) y puede escrutar un contrato con relacionada para un proyecto sin RCA **[V]** |

---

## 4. Riesgos, en orden de severidad

### 4.1 Riesgo 1 — La ventana de acceso abierto (ene-2027 en adelante)

El IAC se publica en la plataforma de Acceso Abierto del Coordinador. Desde ene-2027, cualquier tercero puede ver una SET elevadora y una LAT dimensionadas para 250 MW con solo 150 MW declarados en construcción. Esa holgura es exactamente lo que una SUCTD de tercero busca.

La defensa del art. 79 inc. 2º es de **dos puertas y se mide en el momento de la solicitud del tercero**: capacidad contratada, o proyecto propio declarado fehacientemente. Mientras no exista una de las dos, no hay defensa.

> **Esto corrige la secuencia de la conversación.** El plan era "DEC de la Fase 1 primero, fehaciente después". La reserva de capacidad no existe hasta que se declara, de modo que el fehaciente debe presentarse **en cuanto esté el IAC Definitivo**, en paralelo con la DEC de la Fase 1 y no después de ella.

**Pregunta crítica que esto abre:** ¿qué antecedentes exige el Coordinador para consignar un proyecto como fehaciente, y puede la Fase 2 calificar en 2027 **sin RCA**? Si la consigna exige RCA, la ventana de exposición no se puede cerrar con la vía B y hay que recurrir a la vía D (capacidad contratada), que no depende del estado de permisos del proyecto beneficiario. **[V]** — es la verificación de mayor valor de todo el plan.

### 4.2 Riesgo 2 — Caducidad del remanente de 100 MW (administrable)

| Hito | Fecha |
|---|---|
| IAC estimado | ene-2027 |
| Plazo máximo a DEC (24 meses) | ene-2029 |
| Prórroga única, hasta por el plazo original | ene-2031 |
| Inicio de construcción Fase 1 (objetivo) | ene-2028 |

La Fase 1 llega a su DEC con holgura. La Fase 2 dispone de 2 años ciertos y hasta 4 con prórroga, lo que es suficiente para DIA, RCA, IFC, permisos sectoriales y órdenes de compra — **si la DIA entra durante 2027**.

Dos cautelas:
1. **La prórroga no es automática.** Se concede por una única vez y sobre avance acreditado; la SEC ya confirmó el techo del plazo original más 24 meses. Un remanente sin RCA en ene-2029 es una solicitud de prórroga débil. El plazo de planificación real es **ene-2029**, con ene-2031 como colchón, no como fecha objetivo.
2. **Sigue abierto si la caducidad es parcial o total.** ¿Una DEC por 150 MW de un IAC por 250 MW conserva el remanente hasta el vencimiento, o gatilla caducidad parcial de los 100 MW? **[V]**

> Hay antecedente favorable: el Coordinador ha emitido autorizaciones cuya validez se ancla a la vigencia de la SUCTD de una fase posterior ("permanecerá válida mientras la SUCTD del Atacama Solar-BESS Fase III se encuentre vigente"). El desarrollo por fases con instrumento propio por fase es práctica aceptada.

### 4.3 Riesgo 3 — Coherencia eléctrica de la conexión en MT

Conectar ~100 MW en media tensión sobre un trazado de al menos 2 km es exigente. A 33 kV, 100 MW equivalen del orden de **1.750 A**; a 23 kV, cerca de **2.500 A**. Eso implica varios circuitos en paralelo o conductores de sección muy alta, con pérdidas y costo relevantes sobre 2 km.

Esto interactúa directamente con los permisos:

| Decisión de diseño | Consecuencia de permisos | Consecuencia eléctrica |
|---|---|---|
| Línea **≤23 kV** | Queda **fuera** de la tipología b.1 del art. 3 RSEIA, cualquiera sea el largo | Corriente muy alta; múltiples circuitos; pérdidas sobre 2 km |
| Línea **>23 kV** con trazado ≥2 km | **Dentro** de la tipología b.1: constituye tipología por sí sola | Solución eléctrica razonable; posible SET elevadora propia en la Fase 2 |

La solución técnicamente natural para ~100 MW a 2+ km es elevar en el predio de la Fase 2 y transmitir en alta tensión — lo que cruza el umbral y convierte la línea en tipología propia. **Conviene tomar esta decisión conscientemente, con ingeniería y permisos en la misma mesa**, y no heredarla del diseño preliminar. Nótese que caer en la tipología b.1 no es necesariamente malo: la Fase 2 ingresará al SEIA de todos modos (§5.2), y una SET propia reduce la dependencia funcional respecto de la Fase 1, lo que ayuda en la separabilidad comercial.

### 4.4 Riesgo 4 — Costo de separar la Fase 2 más adelante

Si la Fase 2 termina cubierta por una RCA conjunta, extraerla exige dividir o refundir esa RCA más un cambio de titularidad ante el SEA — trámite que en la práctica se ha visto lento cuando ambos se piden juntos. Se mitiga eligiendo el envase ambiental correcto desde el inicio (§5.3), no al momento de vender.

---

## 5. Encuadre ambiental

### 5.1 El art. 11 bis no es el obstáculo que parece

La norma prohíbe fraccionar **"a sabiendas"** y con el objeto de **variar el instrumento de evaluación o eludir el SEIA**, y **excepciona expresamente** los proyectos cuya ejecución por etapas se acredite. Si el proyecto conjunto de 250 MW seguiría siendo evaluable por DIA, no hay variación de instrumento y el reproche se debilita sustancialmente.

La pregunta operativa no es si el SEA *obliga* a verlo por etapas, sino **qué encuadre conviene declarar** — porque declararlo por etapas es precisamente lo que activa la excepción legal.

### 5.2 Qué cambia con los predios separados por ≥2 km

Este dato mejora la posición de forma significativa. El criterio de unidad de proyecto se construye sobre contigüidad geográfica y dependencia funcional:

| Factor | Situación en Chanqueahue | Efecto |
|---|---|---|
| Contigüidad geográfica | **Predios alejados ≥2 km** | **Favorable.** Debilita la lectura de proyecto único |
| Misma tecnología y tipología | Solar en ambas fases | Neutro a favorable: habilita la excepción del art. 2 g.1 del DS 17/2025 si se va por modificación |
| SET elevadora compartida | Sí | Vínculo funcional |
| **BESS compartido** | Sí, el de la Fase 1 | **Vínculo funcional, el más fuerte** |
| Instrumento de evaluación | DIA en ambos casos | **Favorable.** Sin variación de instrumento, el núcleo del art. 11 bis no se configura |

El BESS compartido es el punto a trabajar. Además del ángulo ambiental, tiene un ángulo regulatorio propio: si energía de la Fase 2 se almacena en un BESS de la Fase 1, ese BESS presta un servicio a un tercero y hay que resolver cómo se estructura (contrato, medida y asignación de inyecciones ante el Coordinador). **Conviene definirlo explícitamente antes de que quede implícito en el diseño.**

De todas formas, la Fase 2 **sí ingresará al SEIA**: ~100 MW solares sobre superficie nueva constituyen por sí solos una central generadora de la tipología c) del art. 3. Lo que está en juego es el envase. El precedente *Crucero Este* (de 127,87 a 213,12 MW tratado como modificación) no es trasladable, porque allí el aumento se logró con los mismos paneles en la misma área, sin obra nueva en terreno nuevo.

### 5.3 Comparación de envases

| Envase | Ventaja | Costo | Encaje con Chanqueahue |
|---|---|---|---|
| RCA única por 250 MW, declarada por etapas | Activa la excepción del art. 11 bis; justifica DEC parcial; alinea con la SAC | Separación posterior exige dividir/refundir RCA + cambio de titularidad | Solo si la Fase 2 **no** se vende |
| RCA Fase 1 + DIA de modificación para la Fase 2 | Evalúa solo el delta; aprovecha el art. 2 g.1 del DS 17/2025 | Sigue siendo un proyecto y una RCA: mismo problema de separabilidad | Poco atractivo: paga el costo de separabilidad sin ganar la limpieza |
| **RCA Fase 1 + DIA nueva e independiente para la Fase 2** | Separabilidad limpia: RCA propia, titular propio, DEC propia, vendible | Expuesto al criterio de unidad de proyecto; la DIA debe describir SET y BESS como infraestructura existente y resolver impactos acumulativos | **Recomendado.** Los ≥2 km de separación y el ingreso por DIA en ambos casos hacen esta exposición manejable |

---

## 6. Propiedad de la infraestructura compartida

Punto que quedó explícitamente abierto. La regulación aplicable es la de instalaciones dedicadas (arts. 79 y 80 LGSE), y las consecuencias de cada estructura son estas:

### Opción I — La SET, la LAT y el BESS quedan en la SPV de la Fase 1

| | |
|---|---|
| **Capa 2 disponible** | Vía B (fehaciente) mientras la Fase 2 sea de la misma SPV; vía C o D si se separa |
| **Obligaciones que asume la SPV 1** | Pasa a ser titular de instalaciones dedicadas: acceso abierto sobre su capacidad disponible, e informar al Coordinador los contratos de transporte vigentes y los proyectos que usen esa capacidad (art. 80 inc. 2º) |
| **Ventaja** | Es la estructura que **no toca** la SAC en curso. Deja la vía B disponible de inmediato |
| **Costo** | Al vender la Fase 2, el comprador queda dependiendo de activos del vendedor. Es un punto de *due diligence* y de negociación de contratos de servidumbre, transporte y uso del BESS |

### Opción II — SET, LAT y BESS en una SPV de transmisión separada

| | |
|---|---|
| **Capa 2 disponible** | **Ambos** generadores pasan a ser terceros respecto de la infraestructura: vía C o D para la Fase 1 **y** para la Fase 2 |
| **Ventaja** | Separabilidad simétrica: cualquiera de las dos fases se vende sin que el comprador dependa del otro generador. Es la estructura más limpia para una cartera |
| **Costo** | Implementarla **ahora** exige reestructurar la titularidad de la SAC en curso, consumiendo la única ventana de modificación (§7). Y hace perder la vía B también para la Fase 1 |

### Opción III — Opción I ahora, segregación posterior

| | |
|---|---|
| **Cómo** | La infraestructura queda en la SPV 1 hasta el IAC Definitivo y la DEC; después se segrega, por ejemplo mediante división de sociedad |
| **Ventaja** | **Preserva la vía B hoy y la opción de llegar a la Opción II mañana.** No consume la ventana de modificación |
| **Costo** | La segregación posterior obliga a informar al Coordinador el cambio de propiedad de instalaciones dedicadas y a mapear la transferencia del IAC y de la DEC. Es trabajo acotado, pero hay que planificarlo, no improvisarlo |

**Recomendación:** **Opción III.** Dado que no hay compromisos comerciales con fecha dura y que el calendario tiene holgura, el valor de preservar optatividad es alto y el costo de decidir ahora —consumir la ventana de modificación— es inmediato y no recuperable.

---

## 7. La restricción de calendario que condiciona todo

Según los criterios del Coordinador, **la solicitud no puede modificarse más de una vez**, en un plazo de **15 días**, entregando una nueva versión como parte de las respuestas a las observaciones al IAC Preliminar. Hay además una discrepancia entre fuentes sobre si el plazo de observaciones es de 15 o 30 días hábiles **[V]**.

Chanqueahue está justo antes de esa ventana: **es la última oportunidad barata de ajustar la arquitectura de conexión.** Después, la estructura cristaliza en el IAC Final y Definitivo.

Duración de referencia, proyecto *PFV BESS El Peral* (2025): Preliminar 04.08 → observaciones 25.08 → Final 25.09 → Definitivo 23.10. Del Preliminar al Definitivo, unos 2,5 meses.

---

## 8. Recomendación y plan de avance

### 8.1 Recomendación

**El plan de la conversación es el correcto. Las respuestas lo refuerzan, con tres correcciones.**

1. **Mantener una sola SPV hasta el IAC Definitivo**, con la infraestructura en la SPV de la Fase 1 (Opción III). No introducir la SPV 2 en el proceso de conexión en curso: consumiría la ventana de modificación sin beneficio, porque no hay compromisos comerciales que lo exijan. La secuencia de Mario —consolidar, cerrar, separar antes del instrumento de Capa 2— es la correcta.

2. **Corrección 1 — No esperar la DEC para proteger la capacidad.** La protección del art. 79 inc. 2º se mide al momento de la solicitud de un tercero. El fehaciente de la Fase 2 debe presentarse en cuanto esté el IAC Definitivo, **en paralelo** con la DEC de la Fase 1.

3. **Corrección 2 — Declarar el proyecto por etapas, explícitamente, en ambos frentes.** Activa la excepción del art. 11 bis, da fundamento a una DEC parcial frente al Coordinador y hace defendible el envase ambiental elegido.

4. **Corrección 3 — Decidir el envase ambiental antes de la separación societaria, no después.** Si la Fase 2 se va a vender, **DIA independiente con RCA propia**: con predios a ≥2 km y DIA en ambos casos, la exposición al criterio de unidad de proyecto es manejable, y evita dividir una RCA conjunta más adelante.

5. **Si el criterio de identidad de titular resulta restrictivo**, migrar a la vía D (capacidad contratada), que no depende de él. Es el plan B que impide que la estrategia se rompa.

### 8.2 Velocidad vs. reducción de riesgo

El *trade-off* que se planteó, resuelto:

| Estrategia | Velocidad | Exposición en acceso abierto | Separabilidad de la Fase 2 |
|---|---|---|---|
| **Una SPV + fehaciente temprano** (recomendada) | **Alta** — no toca la SAC en curso | **Baja** si la consigna de fehaciencia se obtiene sin RCA; media si exige RCA | Media: resoluble con división de sociedad y DIA independiente |
| Una SPV + contrato de transporte temprano | Alta | **Baja** y no depende del estado de permisos de la Fase 2 | Alta |
| Dos SPV desde el inicio | **Baja** — consume la ventana de modificación | Media: obliga a vía C o D | Alta |
| Statu quo, decidir después del IAC | Alta hoy | **Alta** — ventana abierta desde ene-2027 | Indeterminada |

La conclusión relevante es que **no hay que elegir** entre velocidad y riesgo: la combinación de una sola SPV con instrumento de Capa 2 temprano da ambas. El *trade-off* real aparece solo si la consigna de fehaciencia exige RCA de la Fase 2, caso en el cual la vía D lo resuelve.

### 8.3 Plan de avance

**Bloque I — Antes de que llegue el IAC Preliminar (ventana de días)**

| # | Acción | Responsable |
|---|---|---|
| I.1 | **Consulta formal al Coordinador** sobre tres puntos binarios: (i) antecedentes exigidos para consignar un proyecto como fehaciente y si la Fase 2 puede calificar **sin RCA**; (ii) si una DEC parcial por 150 MW conserva el remanente de 100 MW hasta el vencimiento del plazo del IAC o gatilla caducidad parcial; (iii) si un arrendatario o usufructuario de la SET califica para declarar fehaciente, dada la tensión entre la definición y el criterio de aplicación | Regulatorio |
| I.2 | Resolver la **tensión vs. tipología** de la línea de la Fase 2: ≤23 kV o alta tensión con SET propia, con ingeniería y permisos en la misma mesa (§4.3) | Ingeniería + Ambiental |
| I.3 | Revisar el **texto publicado del DS 17/2025**: nuevo art. 2 g.1 y umbral de 2 km de la tipología b.1 | Ambiental |
| I.4 | Decidir el **destino comercial de la Fase 2** al menos a nivel de escenario, porque decide el envase ambiental | Negocio |
| I.5 | Definir cómo se estructura el **uso del BESS de la Fase 1 por la Fase 2**: contrato, medida y asignación de inyecciones | Regulatorio + Comercial |

**Bloque II — Ventana de observaciones al IAC Preliminar (única oportunidad)**

| # | Acción |
|---|---|
| II.1 | Revisar el Preliminar contra la arquitectura de dos etapas: capacidad total autorizada, dimensionamiento del equipamiento dedicado, plazo a DEC y carta Gantt |
| II.2 | Si procede, presentar **la única modificación admitida**, incorporando el desarrollo por etapas |
| II.3 | Negociar el **plazo a DEC y la carta Gantt** de modo que la ventana cubra también el hito de la Fase 2 |

**Bloque III — Del IAC Final al Definitivo (~2,5 meses de referencia) y 2027**

| # | Acción |
|---|---|
| III.1 | Cerrar el IAC Final y Definitivo por los 250 MW |
| III.2 | **Inmediatamente tras el Definitivo:** declarar el proyecto fehaciente de la Fase 2, o firmar el contrato de transporte si la vía B no está disponible. **No esperar la DEC** |
| III.3 | Completar RCA e IFC de la Fase 1 y presentar la **DEC ante la CNE** (permisos sectoriales, órdenes de compra, cronograma de obras) |
| III.4 | **Ingresar la DIA de la Fase 2 durante 2027**, en el envase decidido en I.4, describiendo SET, LAT y BESS como infraestructura existente y resolviendo impactos acumulativos |

**Bloque IV — 2028 a 2029**

| # | Acción |
|---|---|
| IV.1 | Inicio de construcción Fase 1 (objetivo ene-2028) |
| IV.2 | Obtener RCA, permisos sectoriales e IFC de la Fase 2 |
| IV.3 | Ejecutar la separación societaria elegida, **antes** de que el instrumento de Capa 2 requiera rectificación, con el cambio de titularidad ante el SEA mapeado |
| IV.4 | **DEC de la Fase 2 antes de ene-2029.** Hito crítico: tratar ene-2029 como fecha de planificación y ene-2031 como colchón, no como objetivo |

### 8.4 Qué falta confirmar

**Bloqueantes:**
1. Antecedentes exigidos para la consigna de fehaciencia, y si la Fase 2 califica sin RCA. **[V]** — determina si la ventana de acceso abierto se cierra en 2027 o más tarde.
2. Si la DEC parcial conserva el remanente de capacidad o gatilla caducidad parcial. **[V]**
3. Si arrendatario o usufructuario califica para fehaciente, o el criterio es estrictamente "mismo propietario". **[V]**
4. Destino comercial de la Fase 2, al menos como escenario.

**Para cerrar el cronograma:**
5. Estado de la tramitación ambiental de la Fase 1 y si declara etapas o capacidad adicional.
6. Nivel de tensión definitivo de la conexión de la Fase 2 y si tendrá SET propia.
7. Estructura del uso del BESS de la Fase 1 por la Fase 2.
8. Naturaleza del punto de conexión al SEN (nacional o zonal) y tenencia de los terrenos de la Fase 2.
9. Plazo de observaciones efectivo al IAC Preliminar: 15 o 30 días hábiles. **[V]**

---

## 9. Fuentes

Documentos del Coordinador Eléctrico Nacional:
- [Procedimiento Interno de Interconexión de Proyectos (v. dic-2024)](https://www.coordinador.cl/wp-content/uploads/2024/12/Procedimiento-Interno-de-Interconexion-de-Proyectos-1.pdf)
- [Criterios para la Aplicación del Régimen de Acceso Abierto (DAA-PIC v2, abr-2023)](https://www.coordinador.cl/wp-content/uploads/2023/04/2304-DAA-PIC-V2.pdf)
- [Consideración y Gestión de Proyectos Fehacientes (jul-2021)](https://www.coordinador.cl/wp-content/uploads/2021/07/Consideracion-y-Gestion-de-Proyectos-Fehacientes.pdf)
- [Guía Técnica: Criterios de Clasificación de Proyectos del Proceso de Conexión (dic-2021)](https://www.coordinador.cl/wp-content/uploads/2022/01/GUIA-TECNICA-CRITERIOS-DE-CLASIFICACION-DE-PROYECTOS-DEL-PROCESO-DE-CONEXION-v1-1.pdf)
- [Preguntas Frecuentes Régimen de Acceso Abierto (mar-2022)](https://www.coordinador.cl/wp-content/uploads/2022/03/Preguntas-Frecuentes-en-Acceso-Abierto-2.pdf)
- [Informe de Autorización de Conexión Definitivo — PFV BESS El Peral (oct-2025)](https://cartas.coordinador.cl/download_anexos/690a1513356357710f683b20/0)
- [Minuta de Revisión de Antecedentes Proyecto Fehaciente](https://cartas.coordinador.cl/download_anexos/678160233563575774927dfe/0)
- [Informe de Autorización de Conexión de Proyecto Fehaciente (abr-2025)](https://cartas.coordinador.cl/download_anexos/680963123563574614c7ae9f/0)
- [Guía de ayuda al usuario: presentación y gestión de solicitudes](https://cartas.coordinador.cl/download_anexos/689a1386356357392ac8bb46/0)

Normativa y autoridades:
- [LGSE, art. 72°-17 — Construcción, interconexión, puesta en servicio y operación](https://leyes-cl.com/ley_general_de_servicios_electricos_en_materia_de_energia_electrica/72-17.htm)
- [Ley N° 20.936 — Nuevo sistema de transmisión eléctrica](https://www.bcn.cl/leychile/navegar?idLey=20936&tipoVersion=0)
- [Ley N° 19.300, art. 11 bis — Prohibición de fraccionamiento](https://leyes-cl.com/aprueba_ley_sobre_bases_generales_del_medio_ambiente/11_bis.htm)
- [CNE — Declaración de proyectos en construcción (ficha ciudadana N° 4)](https://www.cne.cl/wp-content/uploads/2024/10/RCiudadano_N4.pdf)
- [SEA — Guías relacionadas al artículo 11 de la Ley N° 19.300](https://www.sea.gob.cl/guias-relacionadas-al-articulo-11-de-la-ley-ndeg19300)
- [SEA — Preguntas frecuentes SEIA](https://www.sea.gob.cl/soporte/preguntas-frecuentes-seia)
- [SEA — Principales cambios de la modificación al Reglamento del SEIA](https://www.sea.gob.cl/noticias/conoce-los-principales-cambios-que-considera-la-modificacion-al-reglamento-del-seia)
- [SEA — Consulta de pertinencia PFV Crucero Este (de 127,87 a 213,12 MW)](https://pertinencia.sea.gob.cl/sea-pertinence-web/services/public/document/801147BB-E736-4C73-B9BB-36657A61FEBE)

Análisis sobre el DS N° 17/2025:
- [Carey — Aprueban nueva reforma al Reglamento del SEIA](https://www.carey.cl/aprueban-nueva-reforma-al-reglamento-del-sistema-de-evaluacion-de-impacto)
- [Guerrero — Claves regulatorias para el diseño y modificación de proyectos](https://guerrero.cl/en/noticia/modificacion-al-reglamento-del-seia-claves-regulatorias-para-el-diseno-y-modificacion-de-proyectos/)
- [Redimin — DS 17/2025 redefine cuándo una modificación debe reingresar](https://www.redimin.cl/reglamento-del-seia-ds-17-2025-sube-umbral-a-850-000-litros-y-redefine-cuando-una-modificacion-debe-reingresar/)
- [Reporte Minero — Nuevos umbrales, excepciones y qué cambia para el ingreso de proyectos](https://www.reporteminero.cl/noticia/noticias/2026/01/modificacion-reglamento-seia-nuevos-umbrales-excepciones)

Jurisprudencia y casos:
- [SEC — No procede instruir al Coordinador para aprobar prórroga de DEC y autorización de conexión de parque eólico](https://electromineria.cl/sec-no-procede-instruir-al-coordinador-electrico-para-aprobar-prorroga-de-declaracion-de-construccion-y-autorizacion-de-conexion-de-parque-eolico/)
- [SEA — Resolución de cambio de titularidad de RCA (ejemplo documental)](https://amuprohu.cl/wp-content/uploads/2021/10/cambio-titularidad-rca.pdf)
- [Caducidad de la RCA y Reglamento del SEIA — Revista de Derecho (SciELO)](https://www.scielo.cl/scielo.php?script=sci_arttext&pid=S0718-34372016000200009)
