# Propuesta Grenergy → SQM: adquisición del PFV + BESS Nueva Victoria y PPA de suministro

**Versión:** 1.0 · **Fecha:** septiembre de 2026
**Destinatario interno:** R. Hernández (Development Director Chile) · J. Friedl / J. Álvarez (GR Power) · N. Machuca · M. Aguilera
**Contraparte:** SQM — C. Pavesi, R. Vera, A. Veroiza, R. Fuenzalida (hilo «Grenergy – SQM Sinergias de PPAs»)
**Estado:** documento de trabajo para la reunión con GR Power. Cifras indicativas de modelación propia — no constituyen oferta vinculante.

---

## 1. Resumen ejecutivo

Grenergy propone a SQM una operación de dos piezas: **(i) adquirir el proyecto «Parque Fotovoltaico y Línea de Transmisión para el abastecimiento de instalaciones SQM en la Región de Tarapacá»**, hoy en evaluación ante el SEA, y **(ii) suscribir un PPA de largo plazo** por el que GR, como propietario y operador, abastece el consumo de SQM en el Tap Off Nueva Victoria 110 kV.

Se estructuran **dos alternativas de suministro**. El análisis cuantitativo arroja tres conclusiones que conviene fijar antes de sentarse con SQM:

1. **El proyecto tal como está diseñado no es competitivo.** Con estructura fija, BESS de 320 MWh/20 MW (16 horas) y operación en autoconsumo puro sin inyección, el costo de servir el bloque 24/7 de SQM resulta de **≈ 110 USD/MWh** — por encima de lo que SQM paga hoy como cliente libre (referencia de mercado ≈ 100–107 USD/MWh). El proyecto destruye valor en esa configuración.

2. **Tres decisiones de diseño lo transforman.** Coordinar la instalación con el CEN en lugar de operarla aislada (−43,6 USD/MWh), pasar de estructura fija a seguidor de un eje (+22% de energía por +8% de CAPEX en el campo FV) y **redimensionar el BESS de 16 horas a 4–5 horas** llevan el costo de servir a **≈ 46 USD/MWh** en escenario base y **≈ 54 USD/MWh** en escenario conservador.

3. **La batería de 16 horas es el error de diseño más caro.** Cada hora de almacenamiento más allá de la sexta *añade* entre 1,5 y 6,8 USD/MWh al costo del bloque completo. Pasar de 5 h a 16 h encarece el suministro en **≈ 31 USD/MWh** sin mejorar la posición de SQM: el déficit se cubre mejor desde la cartera de Grenergy Power que con acero y litio inmovilizados en Nueva Victoria.

### Recomendación

| | Alternativa 1 — PPA 24/7 con BESS de 16 h | **Alternativa 2 — PPA híbrido optimizado** |
|---|---|---|
| Configuración | 76,5 MWp (seguidor) + 320 MWh / 20 MW | 76,5 MWp (seguidor) + **150 MWh / 30 MW** |
| CAPEX | US$ 117 M | **US$ 93 M** |
| Costo de servir (conserv. / base) | 78,5 / 74,1 USD/MWh | **54,4 / 45,6 USD/MWh** |
| **Precio PPA a ofertar** | **85 – 92 USD/MWh** | **62 – 68 USD/MWh** |
| Ahorro para SQM vs. ≈100 USD/MWh | 8 – 15% | **32 – 38%** |
| Margen GR a 70 USD/MWh | −0,7 M USD/año | **+4,1 M USD/año (VAN ≈ US$ 37 M a 15 años)** |

**Se recomienda llevar la Alternativa 2 como oferta principal y la Alternativa 1 como opción de contraste**, presentada explícitamente con su sobrecosto para que SQM vea el precio de la autonomía física. La Alternativa 2 es la única que genera una bolsa de valor (VAN ≈ US$ 37–43 M) suficiente para pagar el activo de desarrollo a SQM *y* dejar retorno incremental a GR.

---

## 2. Punto de partida

### 2.1 El proyecto de SQM

| Elemento | Dato | Fuente |
|---|---|---|
| Nombre | «Parque Fotovoltaico y Línea de Transmisión para el abastecimiento de instalaciones SQM en la Región de Tarapacá» | SEIA |
| Ubicación | Pozo Almonte, provincia del Tamarugal, Región de Tarapacá | SEIA |
| Potencia FV | 76,5 MWp | DIA / hilo |
| Generación declarada | 170 GWh el primer año de operación | DIA / hilo |
| Almacenamiento | 320 MWh — «20 MW durante 16 horas continuas» | DIA / hilo |
| Transmisión | LT 66 kV de ≈ 6,6 km + SE seccionadora sobre línea existente | SEIA |
| Inversión declarada | **US$ 111 M** | SEIA / prensa |
| Estado ambiental | PAC cerrada (6-mar a 6-abr-2026); primera adenda en preparación; **RCA estimada para noviembre** | Hilo (C. Pavesi, 3-jul-2026) |

### 2.2 El consumo a abastecer

Punto de suministro: **Tap Off Nueva Victoria 110 kV**. Proyección entregada por SQM bajo NDA (promedio 2026–2040):

| Proceso / planta | MWh/año |
|---|---|
| Lixiviación NV | 78.289 |
| Recursos Hídricos | 39.148 |
| Yoduro NV | 22.848 |
| Pozas SV | 20.840 |
| Yodo NV | 5.046 |
| Iris / Porteos TEA | 0 |
| **Total** | **166.170** |
| **Potencia horaria 24/7 equivalente** | **19,0 MW** |

La potencia media anual proyectada va de 17,0 MW (2026) a un máximo de 20,2 MW (2037–2038), cerrando en 19,9 MW (2040).

**Lectura de los medidores 2026** (TPVITORA_220_J1_SQM, retiro de energía activa horaria) — extracción de N. Machuca:

| Mes 2026 | Promedio | Máximo | Mínimo |
|---|---|---|---|
| Enero | 12,8 MW | 14,3 | 11,3 |
| Febrero | 10,7 | 14,1 | 0 |
| Marzo | 12,6 | 14,6 | 6,8 |
| Abril | 13,1 | 22,2 | 10,0 |
| Mayo | **19,6** | 24,9 | 13,8 |
| Junio | 20,2 | 25,6 | 16,9 |
| Julio | 20,9 | **31,3** | 15,7 |
| Agosto | 19,7 | 26,3 | 15,6 |
| Septiembre | 20,1 | 26,9 | 5,2 |

Dos hechos relevantes para el dimensionamiento:

- **La carga es esencialmente plana** (proceso continuo de lixiviación y plantas de yodo/yoduro), sin ciclo diario apreciable. Es el perfil ideal para un PPA de bloque y el peor posible para un proyecto solar sin almacenamiento.
- **Hay un escalón estructural entre abril y mayo de 2026**, de ≈ 13 a ≈ 19,6 MW promedio, que se sostiene hasta septiembre. Es consistente con la proyección de 19,0 MW plano. **El máximo horario de 31,3 MW (julio) excede la potencia de descarga de 20 MW del BESS diseñado**: en esas horas el proyecto no puede sostener el consumo aun con batería llena.

### 2.3 Rendimiento del recurso solar — validación independiente

Se modeló la generación horaria del sitio (lat −20,70 / lon −69,78, ≈ 1.000 msnm) con modelo de cielo claro y geometría solar, sin calibración previa:

| Configuración | GHI | Generación anual | Rendimiento específico |
|---|---|---|---|
| Estructura fija 20° norte, DC/AC 1,20 | 2.689 kWh/m² | **169,9 GWh** | 2.220 kWh/kWp |
| **Seguidor 1 eje N-S, DC/AC 1,30** | 2.689 kWh/m² | **207,1 GWh** | 2.707 kWh/kWp |

El modelo **reproduce con exactitud los 170 GWh declarados en la DIA**, lo que confirma que el diseño de SQM asume **estructura fija**. Pasar a seguidor de un eje entrega **+37 GWh/año (+22%)** por un sobrecosto de ≈ US$ 5,4 M en el campo FV.

> ⚠ **Discrepancia a resolver.** La simulación interna previa de Grenergy («Generación Estimada PV+BESS – Industria TEA») asume **220 GWh/año**, un 6% por encima de nuestro caso con seguidor y un 29% sobre la DIA. También declara **POI de 17 MW** y una «potencia de retiro del BESS de 70 MW» que no cuadra con los 20 MW × 16 h de la DIA. Antes de fijar precio hay que cerrar estas tres cifras: **rendimiento específico, capacidad del punto de inyección y potencia nominal del BESS**. Una diferencia de 50 GWh/año equivale a ≈ US$ 3,5 M/año de energía.

---

## 3. Estructura de la transacción

> ⚠ **Actualización tras la reunión interna del 29-sep-2026.** La minuta advierte que la figura de
> autoconsumo **exige mismo propietario** para la generación y el consumo, o bien estructurarse vía
> mandato/contrato. La estructura descrita en esta sección —GR adquiere el activo y es propietario—
> conserva el beneficio de peajes sólo si se resuelve esa restricción. El análisis de escenarios y la
> estrategia regulatoria están en
> [`escenarios-y-hoja-de-ruta-sqm.md`](escenarios-y-hoja-de-ruta-sqm.md), que además muestra que el
> beneficio en juego (11 USD/MWh) es mucho menor que el de coordinar con el CEN (44 USD/MWh).


```
┌─ Fase 1 ─────────────────────────────────────────────────────────────┐
│  SQM mantiene la titularidad y lleva la DIA hasta RCA firme (nov-26) │
│  GR ejecuta due diligence técnico-legal sobre el expediente          │
└──────────────────────────────────────────────────────────────────────┘
                                   ↓
┌─ Fase 2 ─────────────────────────────────────────────────────────────┐
│  Compraventa del vehículo (share deal sobre la SPV titular de la     │
│  RCA, servidumbres, CUO/terrenos y avance de conexión)               │
│  Precio = componente fija al cierre + earn-out contra hitos          │
└──────────────────────────────────────────────────────────────────────┘
                                   ↓
┌─ Fase 3 ─────────────────────────────────────────────────────────────┐
│  GR rediseña (seguidores, BESS redimensionado, POI ampliado),        │
│  tramita la modificación de RCA, construye, opera y es propietario   │
└──────────────────────────────────────────────────────────────────────┘
                                   ↓
┌─ Fase 4 ─────────────────────────────────────────────────────────────┐
│  PPA de suministro GR → SQM en el Tap Off Nueva Victoria 110 kV      │
│  Bloque 24/7 · 15–20 años · precio fijo en USD indexado              │
│  GR Power respalda el déficit desde cartera (Oasis de Atacama/Elena) │
└──────────────────────────────────────────────────────────────────────┘
```

**Por qué esta estructura le sirve a SQM:** libera ≈ US$ 111 M de capital que no es *core* para una minera no metálica, traslada el riesgo de construcción, de operación, de degradación del BESS y de mercado eléctrico a un operador especializado, y fija un precio de energía por 15–20 años muy por debajo de su costo actual. SQM conserva el beneficio ambiental del proyecto que originó.

**Por qué le sirve a GR:** entra a un activo con RCA en etapa avanzada — el permiso más lento de la cadena chilena — con un offtaker *investment grade* ya identificado y un punto de conexión definido, y suma un nodo en Tarapacá que complementa geográficamente la plataforma de Antofagasta.

---

## 4. Las dos alternativas de suministro

### 4.1 Alternativa 1 — PPA 24/7 con almacenamiento dedicado de 16 horas

Es el concepto original de SQM, ejecutado por GR. El PFV y el BESS de 320 MWh cubren el consumo en régimen 24/7; el déficit residual (horas de baja irradiancia, invierno, mantenimientos) lo abastece **Grenergy Power** desde su cartera.

**Resultados (76,5 MWp con seguidor + 320 MWh/20 MW, coordinado, POI ≥ 25 MW):**

| Métrica | Valor |
|---|---|
| Generación | 207 GWh/año |
| CAPEX | US$ 117,0 M |
| Autosuficiencia física | 79,9% |
| Importación desde GR Power | 33,5 GWh/año |
| Exportación de excedentes | 64,2 GWh/año |
| Ciclos equivalentes del BESS | 242/año |
| **Costo de servir (conserv. / base / optim.)** | **78,5 / 74,1 / 73,4 USD/MWh** |

**Ventaja:** máxima autonomía física en sitio, relato de autoabastecimiento renovable muy nítido, menor exposición a la red.
**Desventaja:** el BESS de 320 MWh cuesta US$ 46 M y solo cicla 242 veces al año. Su productividad de capital es mala y se traduce íntegra en el precio.

### 4.2 Alternativa 2 — PPA híbrido optimizado (recomendada)

Se dimensiona el almacenamiento por **valor**, no por autonomía. La instalación se declara como **sistema de generación-consumo** coordinado con el CEN: abastece a SQM con prioridad, inyecta excedentes cuando le sobra, retira de la red cuando le conviene, y participa del mercado de potencia y de servicios complementarios. El bloque 24/7 hacia SQM se cierra con la cartera de GR Power.

**Resultados (76,5 MWp con seguidor + 150 MWh/30 MW, POI ≥ 25–30 MW):**

| Métrica | Valor |
|---|---|
| Generación | 207 GWh/año |
| CAPEX | **US$ 92,7 M** (−US$ 24,3 M vs. Alternativa 1) |
| Autosuficiencia física | 61,5% |
| Importación desde GR Power | 64,0 GWh/año a ≈ 54 USD/MWh promedio |
| Exportación de excedentes | 95,1 GWh/año a ≈ 51 USD/MWh promedio |
| Ciclos equivalentes del BESS | 496/año |
| Potencia firme reconocible | 30 MW |
| **Costo de servir (conserv. / base / optim.)** | **54,4 / 45,6 / 40,4 USD/MWh** |

**El punto clave:** la autosuficiencia *física* baja de 80% a 62%, pero el suministro sigue siendo **100% renovable y 24/7 en términos contractuales**, porque el respaldo viene de la cartera renovable de Grenergy Power. SQM no pierde el atributo verde; pierde solo la autonomía física — y por esa autonomía estaría pagando ≈ 28 USD/MWh adicionales, unos **US$ 4,7 M al año**.

---

## 5. Análisis de LCOE: dónde está el dinero

### 5.1 Por qué el diseño actual sale caro

Modelando el proyecto exactamente como está descrito en la DIA —estructura fija, 320 MWh/20 MW, autoconsumo puro sin inyección— el resultado es:

| Concepto | US$ M/año |
|---|---|
| Costo de capital anualizado | 10,60 |
| OPEX | 3,79 |
| Compras de energía para cubrir déficit (42,0 GWh) | 3,04 |
| Ingresos por exportación, potencia y SSCC | **0,00** |
| **Total / 166,4 GWh** | **109,7 USD/MWh** |

Tres fugas de valor simultáneas:

1. **38,3 GWh/año vertidos** (23% de la generación) porque sin derecho de inyección el excedente de verano no tiene destino.
2. **Cero ingresos de potencia y servicios complementarios**, porque una instalación no coordinada no participa de esos mercados.
3. **El BESS cicla 173 veces al año.** Se pagan 320 MWh y se usan como si fueran 120.

### 5.2 Las cuatro palancas, cuantificadas

| # | Palanca | Efecto sobre el costo de servir |
|---|---|---|
| 1 | **Coordinar con el CEN** (de autoconsumo aislado a generación-consumo): habilita inyección, pago por potencia y SSCC | **−43,6 USD/MWh** (94,2 → 50,6 con POI de 17 MW) |
| 2 | **Redimensionar el BESS** de 16 h a 4–5 h | **−31 USD/MWh** (76,5 → 45,6) |
| 3 | **Seguidor de un eje** en lugar de estructura fija: +22% de energía por +8% de CAPEX FV | **−5 a −6 USD/MWh** |
| 4 | **Ampliar el POI** de 17 a 25–30 MW | **−4,5 USD/MWh** (50,6 → 46,1) |

### 5.3 La curva de optimización del almacenamiento

Costo de servir el bloque 24/7 en función de la duración del BESS (FV 76,5 MWp con seguidor, BESS de 30 MW, POI 40 MW):

| Horas | MWh | Conservador | **Base** | Optimista | Ciclos/año | Autosuficiencia |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 78,9 | 88,9 | 102,1 | 0 | 46,3% |
| 1 | 30 | 69,4 | 70,6 | 75,2 | 1.224 | 46,6% |
| 2 | 60 | 63,0 | 61,0 | 62,3 | 829 | 49,5% |
| 3 | 90 | 58,1 | 53,4 | 52,2 | 653 | 53,3% |
| **4** | **120** | **54,1** | 47,1 | 43,8 | 558 | 57,2% |
| **5** | **150** | 54,4 | **45,6** | 40,4 | 496 | 61,5% |
| 6 | 180 | 56,6 | 47,1 | **40,2** | 454 | 66,1% |
| 8 | 240 | 61,6 | 50,5 | 41,4 | 399 | 75,1% |
| 10 | 300 | 68,1 | 56,2 | 46,1 | 358 | 80,6% |
| 12 | 360 | 75,0 | 63,0 | 52,6 | 306 | 80,8% |
| 14 | 420 | 81,8 | 69,7 | 59,4 | 264 | 80,7% |
| **16** | **480** | **88,6** | **76,5** | **66,1** | 231 | 80,6% |

**El óptimo está en 4–6 horas en los tres escenarios de mercado, y la configuración recomendada de
5 horas queda a menos de 0,3 USD/MWh del mínimo en cada uno de ellos** (conservador: mínimo 54,1 en
4 h, 54,4 en 5 h; base: mínimo 45,6 en 5 h; optimista: mínimo 40,2 en 6 h, 40,4 en 5 h). La
recomendación no depende de qué escenario de mercado se materialice.

Costo marginal de cada hora adicional de almacenamiento, sobre el bloque completo (escenario base):

| Tramo | Efecto | US$/año |
|---|---:|---:|
| 0 → 1 h | −18,3 USD/MWh | −3,05 M |
| 1 → 2 h | −9,6 | −1,60 M |
| 2 → 3 h | −7,6 | −1,27 M |
| 3 → 4 h | −6,3 | −1,05 M |
| 4 → 5 h | −1,5 | −0,25 M |
| **5 → 6 h** | **+1,5** | **+0,25 M** |
| 6 → 8 h | +3,4 | +0,57 M |
| 8 → 10 h | +5,7 | +0,95 M |
| 10 → 12 h | +6,8 | +1,13 M |
| 12 → 14 h | +6,7 | +1,12 M |
| 14 → 16 h | +6,8 | +1,13 M |

A partir de la sexta hora **cada hora adicional cuesta más de lo que ahorra**. Las horas 11 a 16 del diseño de SQM destruyen ≈ US$ 3,4 M al año.

**La razón física:** con 76,5 MWp generando 207 GWh contra un consumo de 166 GWh, el balance anual es ajustado. En verano sobra energía y en invierno falta; una batería diaria no resuelve un desbalance estacional. Las horas 6 a 16 quedan esperando un excedente que solo aparece unos pocos meses al año, y mientras tanto pagan capital.

### 5.4 Por qué importa el punto de inyección

Sensibilidad del costo de servir a la capacidad del POI (configuración recomendada, 150 MWh/30 MW):

| POI | Conservador | Base | Optimista | Exportación | Vertimiento |
|---:|---:|---:|---:|---:|---:|
| 0 (aislado) | 96,1 | 94,2 | 92,7 | 0 GWh | 75,1 GWh |
| 10 MW | 66,7 | 56,5 | 49,7 | 53,5 | 37,8 |
| **17 MW** (supuesto GR actual) | 59,6 | 50,6 | 45,2 | 77,4 | 16,2 |
| **25 MW** | 55,1 | 46,8 | 42,5 | 93,8 | 0,5 |
| 30 MW | 54,7 | 46,1 | 41,3 | 94,6 | 0 |
| 40 MW | 54,4 | 45,6 | 40,4 | 95,1 | 0 |

El salto de 0 a 17 MW vale 43,6 USD/MWh; de 17 a 25–30 MW, otros 4 a 4,5. **Por encima de 30 MW satura.** El diseño objetivo debe asegurar **POI ≥ 25 MW** — algo que hay que verificar contra la capacidad real de la LT de 66 kV y del punto de seccionamiento.

### 5.5 Dónde se genera el valor: la forma horaria del precio

El norte del SEN presenta hoy una estructura horaria de costo marginal muy pronunciada, que es exactamente lo que remunera al almacenamiento:

| Bloque | Costo marginal medio |
|---|---|
| Horas solares (09–17) | ≈ 13 USD/MWh (22% de las horas del año bajo 10 USD/MWh) |
| Rampa vespertina (18–22) | ≈ 137 USD/MWh |
| Noche (23–08) | ≈ 64 USD/MWh |

Un BESS de 30 MW / 5 h captura ese diferencial 496 veces al año. Uno de 20 MW / 16 h lo captura 242 veces. **La misma inversión en litio rinde el doble cuando se dimensiona para el ciclo diario en lugar de para la autonomía.**

### 5.6 Sensibilidades

| | WACC 6% | WACC 7% | WACC 8% | WACC 9% |
|---|---:|---:|---:|---:|
| Alternativa 1 | 67,5 | 74,1 | 81,0 | 88,2 |
| **Alternativa 2** | **40,4** | **45,6** | **51,1** | **56,8** |

| | CAPEX −15% | CAPEX base | CAPEX +15% | CAPEX +30% |
|---|---:|---:|---:|---:|
| Alternativa 1 | 64,5 | 74,1 | 83,7 | 93,3 |
| **Alternativa 2** | **38,2** | **45,6** | **53,0** | **60,4** |

La Alternativa 2 domina a la Alternativa 1 en todo el rango explorado — incluso con CAPEX 30% por encima del supuesto y WACC de 9%, sigue por debajo del caso base de la Alternativa 1.

---

## 6. Benchmark de mercado y casos comparables

### 6.1 Referencias de precio en Chile

| Indicador | Valor | Período |
|---|---|---|
| Precio Medio de Mercado (PMM), SEN | 109,2 USD/MWh | dic-2025 |
| Precio final promedio a clientes libres | US$ 87 → **US$ 107/MWh** | 2020 → 2024 |
| Proyección de precio para nuevos clientes libres | 60 – 70 USD/MWh | 2026 |
| Licitación de suministro regulado (ofertas) | 38 – 120 USD/MWh; promedio por oferente 60,9 – 81,2 | 2026 |
| Costo marginal barra Tarapacá | 53,5 (dic-25) → **63,6 USD/MWh** (may-26) | |
| Costo marginal barra Crucero | 50,6 (dic-25) → 60,7 USD/MWh (may-26) | |

La referencia relevante para SQM es el **precio final de cliente libre en torno a 100–107 USD/MWh**. Contra esa base, la Alternativa 2 a 62–68 USD/MWh representa un ahorro de 32–38%.

### 6.2 Operaciones comparables

| Operación | Estructura | Volumen / plazo | Lectura |
|---|---|---|---|
| **Grenergy – Codelco** (abr-2025) | Primer PPA 24/7 de GR en Chile | 0,5 TWh/año · 15 años | Precedente directo del producto 24/7 con respaldo de cartera |
| **Grenergy – offtaker** (jun-2026) | PPA nocturno desde BESS Elena (3,5 GWh, ampliable a 7) | **1 TWh/año · 15 años**, horario no solar | Demuestra que GR puede vender el bloque nocturno *sin* batería dedicada del cliente |
| **Grenergy – Algarrobal** (jun-2026) | PPA híbrido, offtaker *investment grade* | 350 GWh/año · 12 años, desde 1-ene-2028 | Estructura híbrida ya validada comercialmente |
| **Grenergy** (jul-2026) | Subasta de energía solar + almacenada | 1,5 TWh/año | Referencia de precio interna disponible |
| **Atlas – Codelco** (mar-2024) | PPA 24/7 solar + BESS | 375 GWh/año · 15 años; proyecto 215 MW / 1,6 GWh, financiamiento US$ 510 M | Competidor directo en el mismo producto |
| **Sonnedix – Copec EMOAC** (abr-2026) | Tres PPAs sobre BESS | 117 MW / **643,8 MWh ≈ 5,5 h** · COD abr-2027 | **Confirma el óptimo de 4–6 h** |
| **Atlas – COPEC** | BESS 200 MW / 800 MWh = **4 h** | | **Confirma el óptimo de 4–6 h** |
| **BHP – Sungrow** | 195 MW solar + 960 MWh en Escondida y Spence | | Autoconsumo minero con almacenamiento acotado |
| Proyecto minero (sep-2026) | 10 MWp FV + **40 MWh (4 h)** | −23% de costo energético, 90% renovable | **Confirma el óptimo de 4–6 h** |

> **Hallazgo del benchmark:** en todas las operaciones comparables de solar + almacenamiento para consumo industrial en Chile, **la duración del BESS está entre 4 y 6 horas**. No hay precedente de un almacenamiento de 16 horas asociado a un consumo industrial. El diseño de SQM es un *outlier* de mercado, y el análisis explica por qué: la autonomía de 16 horas es una especificación de continuidad operacional, no una decisión económica.

Este es el argumento más potente para la conversación con SQM: **no estamos proponiendo recortar su proyecto, estamos proponiendo alinearlo con lo que hace todo el mercado**, incluidos sus pares mineros.

---

## 7. Precio ofertable y valorización de la compra

### 7.1 Escalera de precios

**Alternativa 1 — PPA 24/7 con BESS de 16 h**

| Escenario | Costo de servir | +10% | +20% | +30% |
|---|---:|---:|---:|---:|
| Conservador | 78,5 | 86,4 | 94,3 | 102,1 |
| Base | 74,1 | 81,6 | 89,0 | 96,4 |
| Optimista | 73,4 | 80,7 | 88,1 | 95,4 |

**Alternativa 2 — PPA híbrido optimizado**

| Escenario | Costo de servir | +10% | +20% | +30% |
|---|---:|---:|---:|---:|
| Conservador | 54,4 | 59,8 | 65,3 | 70,7 |
| Base | 45,6 | 50,1 | 54,7 | 59,3 |
| Optimista | 40,4 | 44,4 | 48,5 | 52,5 |

**Precio recomendado a poner sobre la mesa: 62–68 USD/MWh** para la Alternativa 2, anclado en el escenario **conservador** (54,4) más margen. Deja 8–14 USD/MWh de colchón contra compresión de spreads y, aun así, ofrece a SQM un ahorro de un tercio sobre su costo actual.

Para la Alternativa 1 el precio ofertable honesto es **85–92 USD/MWh** — útil precisamente para mostrar el costo de la autonomía.

### 7.2 Bolsa de valor para pagar el activo

Margen anual de GR y su valor presente (7% real), según el precio PPA acordado:

| Precio PPA | Alt. 1 margen | VAN 15 a | VAN 20 a | **Alt. 2 margen** | **VAN 15 a** | **VAN 20 a** |
|---:|---:|---:|---:|---:|---:|---:|
| 60 | −2,35 M | −21,4 M | −24,9 M | +2,40 M | 21,8 M | 25,4 M |
| 65 | −1,52 M | −13,9 M | −16,1 M | +3,23 M | 29,4 M | 34,2 M |
| **70** | **−0,69 M** | **−6,3 M** | **−7,3 M** | **+4,06 M** | **37,0 M** | **43,0 M** |
| 75 | +0,14 M | 1,3 M | 1,5 M | +4,90 M | 44,6 M | 51,9 M |
| 80 | +0,97 M | 8,9 M | 10,3 M | +5,73 M | 52,2 M | 60,7 M |

**Lectura para la negociación:** a 70 USD/MWh la Alternativa 2 genera un VAN de **US$ 37–43 M**. Esa es la bolsa desde la cual se paga (i) el activo de desarrollo a SQM y (ii) el retorno incremental de GR. **La Alternativa 1 al mismo precio es deficitaria** (−US$ 6,3 M): si SQM insiste en las 16 horas, el precio no puede bajar de ≈ 85 USD/MWh.

Sugerencia de estructura de pago del activo: **componente fija modesta al cierre** (reconociendo el gasto de desarrollo y el expediente SEA) **+ earn-out** contra RCA firme, contra obtención del POI ≥ 25 MW y contra COD. Así el precio del activo sigue al valor que efectivamente se materialice.

---

## 8. Marco regulatorio y ruta de permisos

### 8.1 El DS 32/2026 cambia el tablero

El **Decreto Supremo N° 32 del Ministerio de Energía**, publicado en junio de 2026, modifica el Reglamento de Coordinación y Operación del SEN (DS 125/2017) e incorpora tres figuras que son directamente aplicables a esta operación:

- **Sistemas de Almacenamiento de Energía (SAE)** entre las instalaciones sujetas a coordinación, con reglas para su incorporación a la programación de la operación.
- **Sistemas de generación-consumo**, figura pensada precisamente para complejos productivos que combinan proceso industrial, generación propia y almacenamiento. **Es la figura que habilita la Alternativa 2.**
- **Cliente con autoconsumo**, definido como aquel que, teniendo generación y/o almacenamiento propios, **no inyecta excedentes al sistema**. Es la figura que corresponde a la Alternativa 1 en su versión aislada.

El Coordinador dispone de hasta 24 meses desde la publicación para desarrollar los procedimientos. **Esa ventana coincide con el cronograma del proyecto y hay que gestionarla activamente**: conviene participar en el proceso de elaboración de los procedimientos aplicables a generación-consumo, dado que definirán el reparto de inyecciones y las condiciones de reconocimiento de potencia.

### 8.2 Rutas de tramitación (base: análisis de N. Machuca)

| | **Opción off-grid** (autoconsumo) | **Opción on-grid** (generación-consumo) |
|---|---|---|
| Declaración | SEC — proyecto como autoconsumo (plazos por confirmar) | Fehaciente híbrido: **4–6 meses** |
| Permisos post-RCA | IFC, SEREMI, DOM: **6–9 meses** | IFC, SEREMI, DOM: **6–9 meses** |
| CNE | — | Declaración en construcción: **2 meses** |
| CEN | — | Proceso PGP para operación: **10–12 meses** |
| **Camino crítico incremental** | — | **≈ 12–18 meses adicionales** |

**Este es el costo real de la Alternativa 2: entre 12 y 18 meses más de tramitación.** Contra los ≈ 28 USD/MWh anuales de diferencia (≈ US$ 4,7 M/año), el retraso se paga en menos de un año de operación. Pero hay que gestionarlo en paralelo desde el día uno, no en secuencia.

> **Recomendación de secuencia:** iniciar el fehaciente híbrido y la conversación con el CEN **antes** del cierre de la compraventa, en paralelo con la adenda ambiental de SQM, usando el NDA vigente. El PGP de 10–12 meses es el camino crítico y no admite recuperación posterior.

### 8.3 Modificación de la RCA

El rediseño propuesto (seguidores, BESS de 150 MWh/30 MW, POI ampliado) requiere evaluar si cabe dentro de la envolvente de la RCA en trámite o exige una modificación. Consideraciones preliminares:

- **Reducir** la capacidad de almacenamiento de 320 a 150 MWh reduce impactos y ocupación: es favorable.
- **Aumentar** la potencia del BESS de 20 a 30 MW y ampliar el POI sí podría requerir pronunciamiento.
- El cambio de estructura fija a seguidor modifica la superficie ocupada y el perfil de sombras.

**Acción:** que el equipo ambiental evalúe si conviene **introducir la flexibilidad de diseño en la adenda que SQM está preparando ahora**, antes de la RCA. Es mucho más barato que una modificación posterior, y es una petición concreta y de bajo costo para hacerle a SQM en la próxima reunión.

---

## 9. Riesgos y mitigantes

| Riesgo | Exposición | Mitigante |
|---|---|---|
| **Compresión del spread horario.** El almacenamiento instalado en Chile (≈ 1.700 MW a feb-2026) se duplica hacia dic-2026; el diferencial solar-vespertino se estrecha | Alto — es el principal supuesto del caso | Precio anclado en escenario conservador (spread comprimido 45%, captura 70%, sin SSCC). La Alternativa 2 sigue siendo superior en ese escenario |
| **Caída del precio de potencia** por entrada masiva de BESS | Medio (US$ 3,7 M/año en el caso base) | Escenario conservador ya asume 6,5 USD/kW-mes |
| **POI limitado a 17 MW** o menos por capacidad de la LT 66 kV | Alto — vale 4,5 USD/MWh, y por debajo de 10 MW el caso se deteriora rápido | Verificar capacidad real antes de fijar precio. Condición suspensiva en el SPA |
| **RCA se retrasa o llega con condiciones** | Medio | Earn-out contra RCA firme; no adelantar pagos |
| **Rediseño exige nueva evaluación ambiental** | Medio-alto | Introducir flexibilidad en la adenda actual de SQM |
| **Crecimiento del consumo de SQM** por sobre 20,2 MW proyectados | Bajo-medio | Cláusula de ampliación con precio predefinido; la configuración híbrida escala mejor que la aislada |
| **Máximos horarios de 31,3 MW** superan la descarga del BESS | Cierto en el diseño actual | 30 MW de potencia BESS en la Alternativa 2 lo cubre casi por completo; el resto desde la red |
| **Captura merchant imperfecta** (el modelo usa despacho óptimo) | Medio | Escenario conservador castiga la captura a 70% |

---

## 10. Información a solicitar a SQM

Para pasar de cifras indicativas a una oferta vinculante:

1. **Curva horaria de consumo completa** (8.760 h) de al menos dos años, no promedios anuales. Ya se tiene 2026 parcial desde medidores; falta el histórico y el desglose por proceso.
2. **Detalle del escalón abril-mayo 2026** (13 → 19,6 MW): ¿ampliación permanente, campaña, cambio de proceso?
3. **Estudio de generación del proyecto** con el que se calcularon los 170 GWh: software, configuración, pérdidas, P50/P90. Es imprescindible para cerrar la brecha con nuestros 207 GWh.
4. **Capacidad real de inyección** del punto de seccionamiento en 66 kV y estudios eléctricos asociados.
5. **Contratos de suministro vigentes de SQM**: precio, plazo, vencimiento y condiciones de salida. Sin esto no se puede calibrar el ahorro real ni el punto de entrada.
6. **Expediente SEA completo**, ICSARA y borrador de adenda.
7. **Situación de terrenos**: propiedad, CUO, servidumbres de la LT.
8. **Presupuesto y ofertas de EPC** que SQM haya recibido, para contrastar el CAPEX de US$ 111 M.

---

## 11. Próximos pasos propuestos

| # | Acción | Responsable | Plazo |
|---|---|---|---|
| 1 | Cerrar internamente las tres cifras discrepantes (rendimiento, POI, potencia BESS) | N. Machuca / M. Aguilera | 1 semana |
| 2 | Validar precio de transferencia de GR Power para el bloque de respaldo | J. Friedl / J. Álvarez | 1 semana |
| 3 | Revisión legal de la estructura de adquisición (share deal vs. asset deal) | J. Vergara | 2 semanas |
| 4 | Consulta al equipo ambiental sobre flexibilidad de diseño en la adenda | Equipo ambiental | 2 semanas |
| 5 | Reunión con SQM: presentar ambas alternativas y solicitar la información del §10 | R. Hernández / J. Friedl | 3 semanas |
| 6 | Term sheet no vinculante (PPA + opción de compra) | GR Power / Desarrollo | 6 semanas |

---

## 12. Anexo metodológico

### 12.1 Modelo

- **Generación FV:** modelo horario (8.760 h) con geometría solar para lat −20,70 / lon −69,78, irradiancia de cielo claro tipo ASHRAE calibrada a alta altitud y aire limpio, transposición al plano del arreglo (fija a 20° norte y seguidor de un eje N-S con backtracking, GCR 0,33), derrateo térmico con NOCT 45 °C y coeficiente −0,34%/°C, pérdidas de sistema 11,5%, disponibilidad y suciedad 96,5%, recorte por inversor según DC/AC. **Sin calibración a los datos de SQM:** el resultado de 169,9 GWh para estructura fija coincide de forma independiente con los 170 GWh declarados en la DIA.
- **Consumo:** perfil plano de 19,0 MW con variabilidad autocorrelacionada calibrada a la dispersión observada en los medidores 2026 (desviación ≈ 10,5%, rango 13,6–24,9 MW).
- **Precio horario:** perfil de costo marginal de la barra Tarapacá con media anual de 60 USD/MWh, forma horaria del norte del SEN (valle solar profundo, rampa vespertina alta) y volatilidad log-normal. 22,5% de las horas bajo 10 USD/MWh.
- **Despacho:** optimización por programación lineal con horizonte semanal (168 h) y SOC cíclico, minimizando el costo económico de servir el consumo, con todas las variables (carga, descarga, importación, exportación, vertimiento) valoradas a costo de oportunidad horario. Rendimiento de ida y vuelta 88%, profundidad de descarga 94%.
- **Economía:** CAPEX unitarios calibrados contra la inversión declarada de US$ 111 M (el modelo reproduce US$ 111,2 M para el diseño de la DIA). WACC real después de impuestos 7,0%, vida económica 25 años, tasa de impuesto 27% con depreciación lineal a 10 años, degradación FV 0,45%/año.

### 12.2 Supuestos de costo

| Partida | Valor |
|---|---|
| FV estructura fija | 620 USD/kWp |
| FV seguidor 1 eje | 690 USD/kWp |
| BESS — componente de potencia | 95 USD/kW |
| BESS — componente de energía | 138 USD/kWh |
| Infraestructura común (LT 66 kV, SE seccionadora, caminos, conexión) | US$ 9,5 M |
| Desarrollo + owner's cost + contingencia | 8% del subtotal |
| OPEX FV | 11,5 USD/kWp/año |
| OPEX BESS (O&M + reserva de aumentación) | 7,5 USD/kWh/año (ajustado por ciclado) |
| Seguros | 0,45% del CAPEX/año |
| Peajes + cargo por servicio público + pérdidas | 18 USD/MWh |

### 12.3 Escenarios de mercado

| Parámetro | Conservador | Base | Optimista |
|---|---:|---:|---:|
| Costo marginal medio | 55 USD/MWh | 60 | 65 |
| Compresión del spread horario | 45% | 25% | 0% |
| Captura del valor merchant | 70% | 80% | 90% |
| Precio de potencia | 6,5 USD/kW-mes | 8,5 | 9,5 |
| Ingreso por SSCC | 0 USD/kW-año | 20 | 35 |

### 12.4 Limitaciones

- El despacho por programación lineal supone **previsión perfecta**; el escenario base castiga la captura a 80% y el conservador a 70%, pero la captura real depende de la calidad de la operación.
- El perfil de costo marginal es **sintético y calibrado a referencias públicas**, no una proyección de mercado con modelo de despacho del SEN. Antes de una oferta vinculante debe sustituirse por la proyección oficial de GR Power.
- El consumo se modela como un año representativo de 19,0 MW; no incorpora la trayectoria 2026–2040 ni la estacionalidad real, que a la fecha no está disponible con detalle horario.
- El reconocimiento de potencia firme del BESS usa el criterio de bloque de punta de 4 horas, acotado por la capacidad de inyección. **Requiere validación con el CEN.**
- No se modelan: impuestos diferidos, estructura de deuda de proyecto, cobertura cambiaria ni el detalle de las garantías del PPA.

### 12.5 Fuentes

**Documentación interna:** hilo de correo «Grenergy – SQM Sinergias de PPAs» (nov-2025 a sep-2026), incluyendo la tabla de proyección de consumo de SQM, la extracción de medidores de N. Machuca, la simulación «Generación Estimada PV+BESS – Industria TEA» y el análisis de rutas de tramitación.

**Fuentes públicas:**

- [SEA — Ficha del proyecto «Parque Fotovoltaico y Línea de Transmisión para el abastecimiento de instalaciones SQM en la Región de Tarapacá»](https://www.sea.gob.cl/portal-de-participacion-ciudadana-y-consulta-indigena/proyecto/parque-fotovoltaico-y-linea-de-0)
- [Revista Electricidad — «Minera SQM ingresa al SEIA proyecto solar y de almacenamiento por US$111 millones»](https://www.revistaei.cl/minera-sqm-ingresa-al-seia-proyecto-solar-y-de-almacenamiento-por-us111-millones/)
- [CNE — Reporte Mensual del Sector Energético, enero 2026](https://www.cne.cl/wp-content/uploads/2026/01/RMensual_v202601.pdf)
- [CNE — Reporte Mensual del Sector Energético, junio 2026](https://www.cne.cl/wp-content/uploads/2026/06/RMensual_v202606.pdf)
- [Electrominería — «Precio final promedio a clientes libres sube de US$87 a US$107 por MWh entre 2020 y 2024»](https://electromineria.cl/sistema-electrico-precio-final-promedio-a-clientes-libres-sube-de-us87-a-us107-por-mwh-entre-2020-y-2024/)
- [Energía Estratégica — «Chile activa el Decreto 32: las nuevas reglas que reordenan almacenamiento, PMGD y operación eléctrica»](https://www.energiaestrategica.com/es/notes/chile-activa-el-decreto-32-las-nuevas-reglas-que-reordenan-almacenamiento-pmgd-y-operacion-electrica)
- [Garrigues — «Chile: El Gobierno aprueba un decreto que redefine la operación del sistema eléctrico y el reparto de inyecciones»](https://www.garrigues.com/es_ES/noticia/chile-gobierno-aprueba-decreto-redefine-operacion-sistema-electrico-reparto-inyecciones)
- [pv magazine — «Grenergy firma un PPA nocturno de 1 TWh anual durante 15 años en Chile»](https://www.pv-magazine.es/2026/07/01/grenergy-firma-un-ppa-nocturno-de-1-twh-anual-durante-15-anos-en-chile/)
- [pv magazine LatAm — «Grenergy firma en Chile un PPA híbrido por 350 GWh anuales para la fase Algarrobal de Oasis de Atacama»](https://www.pv-magazine-latam.com/2026/06/01/grenergy-firma-en-chile-un-ppa-hibrido-por-350-gwh-anuales-para-la-fase-algarrobal-de-oasis-de-atacama/)
- [pv magazine LatAm — «Grenergy subasta en Chile 1,5 TWh anuales de energía solar y almacenada»](https://www.pv-magazine-latam.com/2026/07/02/grenergy-subasta-en-chile-15-twh-anuales-de-energia-solar-y-almacenada/)
- [pv-tech — «Atlas Renewable Energy signs 375GWh 24/7 PPA with Codelco»](https://www.pv-tech.org/atlas-renewable-energy-signs-375gwh-24-7-ppa-with-codelco/)
- [pv-tech — «Atlas Renewable Energy secures US$510 million financing for 215MW/1.6GWh solar-plus-storage in Chile»](https://www.pv-tech.org/atlas-renewable-energy-us510-million-financing-215mw-1-6gwh-solar-plus-storage-chile/)
- [Energy-Storage.news — «Atlas and COPEC sign PPA for 200MW/800MWh BESS in Chile»](https://www.energy-storage.news/atlas-copec-ppa-200mw-800mwh-bess-chile/)
- [pv magazine LatAm — «En Chile, Sonnedix firma tres PPAs con Copec EMOAC para un BESS de 117 MW / 643,8 MWh»](https://www.pv-magazine-latam.com/2026/04/24/en-chile-sonnedix-firma-tres-ppas-con-copec-emoac-para-un-bess-de-117-mw-6438-mwh/)
- [Reporte Minero — «Proyecto minero reduce 23% costos energéticos con solar y baterías»](https://www.reporteminero.cl/noticia/noticias/2026/09/proyecto-minero-reduce-costos-energeticos-solar-baterias-descarbonizacion)
- [Ember Energy — «How cheap is battery storage?»](https://ember-energy.org/latest-insights/how-cheap-is-battery-storage/)
- [Energía Estratégica — «Chile amplía el mercado eléctrico: ACEN proyecta precios de USD 70 por MWh para 2026»](https://www.energiaestrategica.com/chile-amplia-el-mercado-electrico-acen-proyecta-precios-de-usd-70-por-mwh-para-2026/)

---

*Documento de trabajo interno de Grenergy. Contiene información de SQM sujeta al NDA suscrito entre las partes.*
