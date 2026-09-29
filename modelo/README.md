# Modelo de evaluación — PPA SQM Nueva Victoria

Modelo horario que respalda los documentos
[`docs/propuesta-sqm-ppa-pfv-bess.md`](../docs/propuesta-sqm-ppa-pfv-bess.md) y
[`docs/escenarios-y-hoja-de-ruta-sqm.md`](../docs/escenarios-y-hoja-de-ruta-sqm.md).
Todas las cifras de ambos documentos se reproducen ejecutando estos scripts.

## Requisitos

```
pip install numpy scipy
```

## Módulos

| Archivo | Qué hace |
|---|---|
| `solar.py` | Generación FV horaria (8.760 h) para Nueva Victoria / Pozo Almonte, con geometría solar y modelo de cielo claro. Estructura fija y seguidor de un eje. |
| `model.py` | Perfil de consumo de SQM, despacho heurístico, y la capa económica: CAPEX, OPEX, CRF, factor de impuestos y LCOE. |
| `market.py` | Señal horaria de costo marginal de la barra Tarapacá. |
| `dispatch_lp.py` | Despacho óptimo por programación lineal, horizonte semanal con SOC cíclico. |
| `evaluate.py` | Evaluación económica integrada de una configuración (escenario base fijo). |
| `final.py` | Evaluación por escenario de mercado — es el módulo que usa el documento. |
| `optim2.py` | Barridos de optimización: duración del BESS, potencia del BESS y superficie FV × BESS. |
| `pricing.py` | Escalera de precios PPA, sensibilidades a WACC y CAPEX, y valorización de la compra del proyecto. |
| `poi.py` | Sensibilidad a la capacidad del punto de inyección. |
| `escenarios.py` | Matriz vehículo regulatorio × configuración. Añade el conmutador de peajes sobre la energía servida en sitio (con o sin figura de autoconsumo). |
| `opt_autoconsumo.py` | Óptimo del BESS **sin** derecho de inyección: el óptimo se desplaza de 5 a 8 horas. |
| `matriz.py` | Matriz final D0/E1/E2/E3, descomposición del valor y precio ofertable. |
| `descomposicion.py` | Descomposición del valor de coordinar sobre configuración idéntica. |
| `merchant.py` | Valor del activo como planta merchant, sin PPA con SQM. |
| `reconcilia.py` | Reconcilia el déficit de 9 GWh de la minuta con el modelo horario. |
| `charts_data.py` | Genera `charts.json` con las series de los gráficos. |
| `svg.py` / `svg2.py` | Generan las figuras SVG (1–3 y 4–5 respectivamente). |
| `_style.py` | CSS y helper de tablas compartidos por los dos generadores de HTML. |
| `build_html.py` / `build_html2.py` | Generan las versiones HTML de cada documento. |

## Uso

```bash
python3 solar.py        # valida el recurso: 169,9 GWh con estructura fija ≈ los 170 GWh de la DIA
python3 final.py        # tabla principal: costo de servir por configuración y escenario
python3 optim2.py       # curva de optimización del almacenamiento
python3 pricing.py      # precio ofertable y VAN de la operación
python3 poi.py          # sensibilidad al punto de inyección
python3 matriz.py       # matriz de escenarios regulatorios y precio ofertable
python3 reconcilia.py   # reconciliación del balance energético con la minuta
python3 merchant.py     # valor del activo sin PPA

# regenerar figuras y documentos HTML
python3 charts_data.py && python3 svg.py && python3 svg2.py
python3 build_html.py && python3 build_html2.py
```

`svg.py` lee `charts.json` desde su propio directorio, así que hay que ejecutar
`charts_data.py` antes, desde esa misma carpeta.

## Validaciones de calibración

El modelo se contrasta contra dos referencias externas, sin ajustar parámetros para
conseguirlo:

- **Generación:** 169,9 GWh/año con estructura fija a 76,5 MWp, frente a los **170 GWh**
  declarados en la DIA de SQM.
- **CAPEX:** US$ 111,2 M para el diseño de la DIA (76,5 MWp fija + 320 MWh/20 MW + LT 66 kV),
  frente a los **US$ 111 M** declarados en el SEIA.

## Limitaciones

Ver §12.4 del documento. En particular: el despacho por PL supone previsión perfecta
(los escenarios castigan la captura a 70–90%), el perfil de costo marginal es sintético
y calibrado a referencias públicas —no una proyección con modelo de despacho del SEN—,
y el reconocimiento de potencia firme del BESS requiere validación con el CEN.
