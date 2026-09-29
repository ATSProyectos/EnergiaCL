# Escenarios y hoja de ruta — PPA SQM Nueva Victoria

**Versión:** 1.0 · **Fecha:** septiembre de 2026
**Complementa:** [`propuesta-sqm-ppa-pfv-bess.md`](propuesta-sqm-ppa-pfv-bess.md)
**Incorpora:** minuta de reunión interna del 29-sep-2026 (Cata, Nico, Rodrigo, Juan)
**Propósito:** fijar los escenarios de estructuración, la estrategia regulatoria y la secuencia
para presentar internamente y luego a SQM.

---

## 1. Qué cambia respecto del análisis anterior

La minuta introduce un eje que el análisis previo no tenía: **el vehículo regulatorio no es un
detalle de implementación, es la variable que más mueve el precio.** Tres aportes concretos:

| Aporte de la minuta | Consecuencia sobre el análisis |
|---|---|
| La figura de autoconsumo **exige mismo propietario**, o estructurarse vía mandato/contrato | Invalida la estructura propuesta en §3 del documento anterior (GR compra y es propietario) si se quiere conservar el beneficio de autoconsumo |
| El reglamento **busca impedir que grandes clientes usen la figura para alimentar consumo existente** sin ampliaciones reales; las proyecciones de SQM para 2026–2027 no muestran crecimiento | El riesgo no es de precio, es de **elegibilidad**. Rodrigo ya fue advertido |
| El caso Data Center evalúa **tres** alternativas: SGC, PPA tradicional y autoconsumo | Da el marco correcto: son tres vehículos distintos, no dos configuraciones |

El acuerdo n.° 3 de la minuta —calcular CAPEX y OPEX para determinar el LCOE y definir la tarifa
de PPA competitiva— es exactamente lo que entrega el documento anterior. Este documento cierra
el acuerdo n.° 2: integrar el análisis legal y decidir el vehículo.

---

## 2. Tres hallazgos nuevos

### 2.1 El déficit de 9 GWh no se sostiene con un BESS de 20 MW

La minuta registra un déficit estimado de **9 GWh/año**. Al reproducir ese balance en el modelo
horario, ese número sólo aparece si la batería puede descargar muy por encima de los 20 MW de la
DIA:

| Supuesto | Déficit resultante | Vertimiento |
|---|---:|---:|
| 220 GWh · consumo plano 19,0 MW · BESS 320 MWh / **20 MW** | 23,8 GWh | 68,5 GWh |
| 220 GWh · consumo plano 20,0 MW · BESS 320 MWh / **20 MW** | 29,0 GWh | 64,9 GWh |
| 220 GWh · consumo plano 19,0 MW · BESS 320 MWh / **70 MW** | **1,4 GWh** | 43,0 GWh |
| 207 GWh · consumo real variable · BESS 320 MWh / **30 MW** | **5,2 GWh** | 34,3 GWh |
| 170 GWh (DIA) · consumo real variable · BESS 320 MWh / 20 MW | 27,5 GWh | 22,5 GWh |

El déficit bajo de la simulación previa es consistente con la nota «Potencia de Retiro del BESS
(70 MW)» de la lámina *Generación Estimada PV+BESS – Industria TEA*, **no** con los «20 MW durante
16 horas continuas» que declara la DIA.

> **El diagnóstico correcto del diseño de SQM no es que sobra energía almacenada, es que falta
> potencia de descarga.** El proyecto es rico en energía y pobre en potencia, que es exactamente al
> revés de lo que conviene.

Y la corrección es barata. Subir el BESS de 20 a 30 MW manteniendo los 320 MWh cuesta ≈ **US$ 0,95 M**
adicionales de conversión y reduce el costo de servir de 74,1 a 58,5 USD/MWh — unos **US$ 2,6 M al
año**. Payback inferior a cinco meses. Es la mejora de mejor relación costo-beneficio de todo el
rediseño y, a diferencia del resto, no exige discutir el tamaño de la batería con SQM.

### 2.2 Coordinar vale cuatro veces más que el autoconsumo

Descomposición sobre configuración idéntica (76,5 MWp con seguidor + 150 MWh / 30 MW,
escenario base):

| US$ M/año | A · Autoconsumo puro | B · SGC coordinado | C · PPA tradicional |
|---|---:|---:|---:|
| Costo de capital | 8,83 | 8,83 | 8,83 |
| OPEX | 2,97 | 3,19 | 3,19 |
| Peajes sobre energía servida en sitio | 0,00 | 0,00 | **1,85** |
| (−) Margen de mercado | −3,89 | +0,09 | +0,09 |
| (−) Potencia de suficiencia | 0,00 | **3,66** | **3,66** |
| (−) Servicios complementarios | 0,00 | **0,60** | **0,60** |
| **Costo de servir (USD/MWh)** | **94,2** | **46,1** | **57,3** |
| Vertimiento | 75,1 GWh | 0 | 0 |

El salto de A a B son **48,1 USD/MWh**, y se descompone así:

| Componente | USD/MWh |
|---|---:|
| Margen de mercado por poder inyectar excedentes en vez de verterlos | 23,9 |
| Potencia de suficiencia reconocida al BESS | 22,0 |
| Servicios complementarios | 3,6 |
| (−) Mayor OPEX por mayor ciclado | −1,4 |
| **Total** | **48,1** |

Perder la figura de autoconsumo (de B a C) cuesta **+11,1 USD/MWh**: los peajes sobre los 103 GWh
que se sirven en sitio.

> **Esto invierte la prioridad regulatoria de la reunión.** La preocupación fue si la figura de
> autoconsumo es elegible. Los números dicen que el autoconsumo es el vehículo **menos** valioso de
> los tres: un PPA tradicional con GR propietario, sin ningún beneficio de autoconsumo pero
> coordinado con el CEN, es **33 USD/MWh más barato** que un autoconsumo puro perfectamente
> elegible. Lo que hay que pelear es el **derecho a inyectar y coordinar**, no la figura de
> autoconsumo.

La conclusión resiste el escenario conservador, donde la compresión de spreads y la caída del precio
de potencia castigan justamente los dos componentes mayores: E1 queda en 90,9 y E2 en 54,7, una
brecha que sigue siendo de 36 USD/MWh.

### 2.3 El activo no se sostiene solo: el vehículo es existencial

Valorizado como planta merchant, sin PPA con SQM, con toda la energía al sistema:

| Configuración | CAPEX | EBITDA | Yield | VAN 25 años |
|---|---:|---:|---:|---:|
| 76,5 MWp sin BESS | 67,3 M | 2,60 M | 3,9% | **−37,0 M** |
| 76,5 MWp + 150 MWh / 30 MW | 92,7 M | 9,57 M | 10,3% | **+18,8 M** |
| 76,5 MWp + 320 MWh / 20 MW (diseño SQM) | 117,0 M | 7,33 M | 6,3% | **−31,5 M** |
| 76,5 MWp + 320 MWh / 30 MW | 118,0 M | 9,92 M | 8,4% | −2,4 M |

Y por escenario, para la configuración optimizada: VAN de **−15,0 M** (conservador), **+18,8 M**
(base), **+47,9 M** (optimista).

> **Comprar Nueva Victoria como activo merchant no se sostiene.** Sólo el caso base da VAN positivo,
> y el conservador lo destruye. El valor del activo para GR está en el PPA con SQM, no en el mercado
> spot. Por lo tanto la pregunta del vehículo regulatorio no es una condición de borde del negocio:
> **es el negocio**. Si no hay vehículo que permita coordinar e inyectar, no hay operación que
> justifique la compra.
>
> Corolario para la negociación: la opción de **desacoplar** —comprar el activo como planta de
> cartera y venderle a SQM un PPA desde el portafolio de GR Power— no es una alternativa de repliegue
> atractiva. Si el vehículo falla, lo razonable es **no comprar el activo** y competir por el PPA
> de SQM desde la cartera existente (Oasis de Atacama / Elena), que es donde GR ya tiene costo marginal.

---

## 3. Matriz de escenarios

Costo de servir el bloque 24/7 de SQM (166,4 GWh/año), cada escenario con su configuración óptima:

| | Escenario | Conserv. | Base | Optim. | CAPEX | Autosuf. | Vertido |
|---|---|---:|---:|---:|---:|---:|---:|
| **D0** | Diseño SQM tal cual — fija, 320 MWh/20 MW, aislado | 111,7 | 109,7 | 108,0 | 111,2 M | 74,8% | 38,3 GWh |
| **E1** | Autoconsumo puro — SQM propietario, sin inyección · *240 MWh/30 MW* | 90,9 | 90,1 | 89,4 | 106,1 M | 92,3% | 43,0 GWh |
| **E3** | PPA tradicional — GR propietario, sin beneficio de peaje · *150 MWh/30 MW* | 66,3 | 57,3 | 52,0 | 92,7 M | 61,9% | 0 |
| **E2** | **SGC coordinado — con inyección y beneficio de peaje · *150 MWh/30 MW*** | **54,7** | **46,1** | **41,3** | **92,7 M** | 61,9% | 0 |

Nota sobre el dimensionamiento: **el óptimo del BESS depende del vehículo.** Con derecho de
inyección el óptimo son 4–6 horas (150 MWh/30 MW); sin derecho de inyección el óptimo se desplaza a
**8 horas** (240 MWh/30 MW), porque el excedente que no se puede vender conviene almacenarlo. En
ningún vehículo el óptimo se acerca a las 16 horas del diseño actual.

### Precio ofertable y margen

Anclado en el escenario **conservador** más margen, contra la referencia de ≈100 USD/MWh que paga
hoy un cliente libre:

| | Piso conservador | PPA sugerido | Ahorro para SQM | Margen GR | VAN 15 años |
|---|---:|---:|---:|---:|---:|
| **D0** | 111,7 | — | — | — | — |
| **E1** | 90,9 | ~100 | 0% | 1,65 M | 15,0 M |
| **E3** | 66,3 | **72** | 28% | 2,45 M | 22,4 M |
| **E2** | **54,7** | **65** | **35%** | **3,14 M** | **28,6 M** |

**D0 y E1 no son ofertables.** D0 cuesta más que la tarifa actual del cliente. E1 tiene un piso
conservador de 90,9: cualquier margen razonable lo deja en el entorno de lo que SQM ya paga, con lo
cual la operación pierde su razón de ser para ambas partes.

---

## 4. Estrategia regulatoria recomendada

**Perseguir el SGC (sistema de generación-consumo) como vehículo primario, y el PPA tradicional
coordinado como plan B. Tratar el autoconsumo como lo que es: un beneficio marginal de 11 USD/MWh
que no justifica condicionar la estructura de la operación.**

Fundamento:

1. El DS 32/2026 crea expresamente la figura de sistemas de generación-consumo para «complejos
   productivos que combinan proceso industrial, generación propia y almacenamiento». Es la figura
   diseñada para este caso.
2. La restricción que preocupa a la reunión —impedir alimentar consumo existente sin ampliaciones
   reales— es una restricción del reglamento de **autoconsumo**. Hay que verificar si alcanza también
   al SGC; si no alcanza, el problema de elegibilidad desaparece.
3. Aun en el peor caso —ningún beneficio de peaje, GR propietario, PPA tradicional— el proyecto
   coordinado sirve a 57,3 USD/MWh y es ofertable a 72 con 28% de ahorro para SQM.

### Las preguntas legales que deciden la operación

Son para Cata, y están en el camino crítico. Cada una tiene un valor cuantificado:

| # | Pregunta | Qué está en juego |
|---|---|---|
| **L1** | ¿El SGC admite que la generación y el consumo tengan **propietarios distintos**, o exige «generación propia» en sentido estricto? | **Decide la estructura completa.** Si exige mismo propietario, GR no puede ser dueño del activo y conservar el beneficio |
| **L2** | Si exige mismo propietario, ¿el **mandato/contrato** que menciona la minuta es suficiente? ¿Qué forma debe tener —arriendo, usufructo, comodato, mandato de operación? | 11 USD/MWh + viabilidad de la compra |
| **L3** | ¿La restricción de «consumo existente sin ampliaciones» alcanza al **SGC** o sólo al autoconsumo? | Elegibilidad de E2 |
| **L4** | ¿Qué reconocimiento de **potencia de suficiencia** obtiene un BESS dentro de un SGC, y con qué criterio de bloque de punta? | **22,0 USD/MWh** — el componente individual más grande |
| **L5** | ¿Puede un SGC participar del mercado de **servicios complementarios**? | 3,6 USD/MWh |
| **L6** | ¿Qué capacidad de inyección admite el punto de seccionamiento en 66 kV, y qué se requiere para llevarla a ≥ 25 MW? | 43,6 USD/MWh (el salto de 0 a inyectar) |

L1 y L4 concentran el riesgo. **Hasta que L1 esté respondida no se puede definir la estructura de la
operación**, y hasta que L4 esté respondida el precio ofertable tiene una incertidumbre de ±22 USD/MWh.

---

## 5. Hoja de ruta interna

### Etapa A — Cierre técnico y legal (semanas 1–3)

| # | Acción | Responsable | Entregable |
|---|---|---|---|
| A1 | Responder L1–L3 sobre la base del reglamento que compartirá Cata | Cata + J. Vergara | Memo legal de una página con la respuesta a cada pregunta |
| A2 | Consultar a la CNE/CEN de manera informal sobre L4 y L5 | Regulación | Lectura preliminar del reconocimiento de potencia |
| A3 | Cerrar las tres cifras técnicas discrepantes: rendimiento específico, capacidad del POI, potencia nominal del BESS | N. Machuca / M. Aguilera | Ficha técnica única de referencia |
| A4 | Verificar capacidad de inyección real de la LT 66 kV (L6) | Ingeniería / Conexiones | Capacidad máxima y obras requeridas |
| A5 | Validar precio de transferencia de GR Power para el bloque de respaldo | J. Friedl / J. Álvarez | Precio interno por bloque horario |
| A6 | Contrastar el CAPEX del modelo contra cotizaciones vigentes de EPC y BESS | Ingeniería | Rango de CAPEX validado |

### Etapa B — Decisión interna (semana 4)

Comité con Rodrigo, Juan, Cata y el equipo de desarrollo. **Tres decisiones, en este orden:**

1. **Vehículo.** SGC, PPA tradicional, o no avanzar. Determinado por A1–A2.
2. **Estructura de propiedad.** Compra del activo, mandato, o sólo PPA desde cartera.
   Determinada por la anterior.
3. **Mandato de negociación.** Precio piso, precio objetivo, y hasta dónde se puede ceder en
   configuración técnica.

**Regla de decisión sugerida:** si L1 permite propiedad de terceros bajo SGC → comprar el activo y
estructurar E2. Si L1 exige mismo propietario y L2 no ofrece un vehículo contractual sólido → **no
comprar el activo**; ofrecer a SQM el rol de desarrollador/EPC/O&M más un PPA desde cartera, y
competir por el suministro sin inmovilizar capital.

### Etapa C — Preparación de la presentación a SQM (semana 5)

Material a preparar una vez decidido el vehículo:
- Una lámina de validación (nuestro modelo reproduce sus 170 GWh y sus US$ 111 M)
- Una lámina del hallazgo de potencia del BESS (el regalo técnico)
- Una lámina del valor de inyectar (el problema compartido)
- Una lámina de oferta (precio y ahorro)
- Una lámina de estructura (las opciones de propiedad)

---

## 6. Hoja de ruta con SQM

### 6.1 El orden de la conversación importa

La secuencia natural —«compramos su proyecto, pero antes hay que rediseñarlo»— pone tres pedidos
sobre la mesa al mismo tiempo y activa la defensa del proyecto. La secuencia recomendada separa lo
que es de interés común de lo que es negociación:

| Paso | Mensaje | Por qué en esta posición |
|---|---|---|
| **1. Validación** | «Modelamos su proyecto de forma independiente y nos da 169,9 GWh contra sus 170, y US$ 111,2 M contra sus US$ 111 M» | Construye credibilidad técnica antes de cualquier crítica. No cuesta nada y cambia el tono |
| **2. El hallazgo técnico** | «El limitante de su diseño no es la energía almacenada, es la potencia de descarga. Con 30 MW en vez de 20 el déficit cae de 24 a 5 GWh, por US$ 0,95 M» | Es un regalo: barato, verificable, y mejora *su* proyecto sea quien sea el dueño |
| **3. El problema compartido** | «El derecho a inyectar y coordinar vale unos 44 USD/MWh. Sin él, ningún dimensionamiento hace competitivo el proyecto» | Alinea intereses: ambos quieren que el activo valga más. Aquí se propone la estrategia regulatoria conjunta |
| **4. La oferta** | «Con esos dos ajustes podemos ofrecerles un PPA 24/7 a X USD/MWh, un tercio bajo lo que pagan hoy» | Llega después de haber demostrado competencia y aportado valor |
| **5. La estructura** | Las opciones de propiedad y las condiciones | Es lo único puramente distributivo. Va al final |

### 6.2 Qué mostrar y qué no

**Mostrar:**
- La validación de generación y CAPEX
- El benchmark de duración de almacenamiento (Sonnedix/Copec 5,5 h, Atlas/COPEC 4 h, el caso minero
  de 4 h). Es el argumento más fuerte y no es nuestro: es el mercado
- La curva de optimización del BESS, sin los costos de GR
- El precio ofertable y el ahorro para SQM

**No mostrar:**
- El costo de servir de GR ni el margen
- El VAN de la operación ni la valorización del activo
- La descomposición de dónde viene el valor de coordinar — se comunica el resultado (44 USD/MWh),
  no el desglose entre potencia, SSCC y arbitraje, que es información comercial de GR

### 6.3 Qué pedirle a SQM en esta reunión

Además de la información del §10 del documento anterior, **dos pedidos concretos y de bajo costo
para ellos**:

1. **Introducir flexibilidad de diseño en la adenda que están preparando ahora** —rango de potencia
   del BESS, estructura con seguidores, capacidad de inyección ampliada—, antes de la RCA. Es mucho
   más barato que una modificación posterior y no compromete nada.
2. **Abordar conjuntamente la estrategia regulatoria del vehículo** ante CNE y CEN. GR aporta el
   equipo de regulación; SQM aporta la titularidad y el consumo. Es el pedido que más valor genera
   para ambos.

### 6.4 El punto de quiebre a anticipar

SQM presentó su proyecto al SEA como abastecimiento de sus instalaciones, y sus proyecciones
2026–2027 no muestran crecimiento. Si el reglamento de autoconsumo efectivamente les impide usar la
figura sobre consumo existente, **SQM tiene un problema con o sin Grenergy**, y su proyecto pierde
buena parte de su justificación económica.

Ese es el momento en que la conversación cambia de «nos quieren comprar el proyecto» a «nos traen la
salida». Conviene llegar con la respuesta preparada: la ruta SGC, el rediseño, y el PPA. **Es
probablemente el mejor argumento de la propuesta, y conviene reservarlo para cuando ellos planteen
la dificultad, no antes.**

---

## 7. Riesgos añadidos a la matriz anterior

| Riesgo | Exposición | Mitigante |
|---|---|---|
| **El SGC exige mismo propietario y el mandato no resiste el escrutinio regulatorio** | Existencial para la compra del activo | Plan B: no comprar; competir por el PPA desde cartera. Resolver L1–L2 antes de cualquier oferta |
| **El reconocimiento de potencia del BESS en un SGC es menor al supuesto** | 22,0 USD/MWh — el componente individual más grande | Escenario conservador ya asume 6,5 USD/kW-mes. Consulta informal al CEN antes de ofertar |
| **El reglamento de autoconsumo bloquea también al SGC** | Elimina E1 y E2; queda E3 a 66,3–57,3 | E3 sigue siendo ofertable a 72 con 28% de ahorro |
| **SQM no acepta rediseñar y exige el proyecto tal como está** | D0 no es ofertable | Presentar el benchmark de mercado y el hallazgo de potencia. Si aun así no cede, retirarse de la compra |
| **La adenda se presenta sin flexibilidad de diseño** | Obliga a modificar la RCA después, con retraso | Pedido explícito en la próxima reunión, por escrito |

---

## 8. Nota metodológica sobre los escenarios nuevos

Los escenarios E1, E2 y E3 se calculan con el mismo modelo horario del documento anterior. Las
diferencias entre ellos se implementan así:

- **E1 (autoconsumo puro):** sin capacidad de inyección (`inj_limit = 0`), sin participación en el
  mercado de potencia ni en servicios complementarios, sin carga del BESS desde la red. El
  excedente se vierte. Es la lectura literal de la definición de «cliente con autoconsumo» del
  DS 32, que excluye inyectar excedentes al sistema.
- **E2 (SGC coordinado):** inyección hasta el límite del POI, participación en potencia y SSCC,
  peajes sólo sobre la energía importada.
- **E3 (PPA tradicional):** idéntico a E2, salvo que **la energía servida en sitio también paga
  peajes** (18 USD/MWh), porque no existe figura que permita netear.

La atribución de ingresos por potencia y SSCC a E2 y E3, y su exclusión de E1, es el supuesto que
más pesa en la comparación: explica 25,6 de los 48,1 USD/MWh de diferencia entre E1 y E2. **Ese
supuesto es precisamente la pregunta L4–L5 para Cata**, y es la razón por la que el memo legal está
en el camino crítico y no puede resolverse con más modelación.

---

*Documento de trabajo interno de Grenergy. Contiene información de SQM sujeta al NDA suscrito entre
las partes.*
