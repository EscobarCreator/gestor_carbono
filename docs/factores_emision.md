# Factores de emisión

| Actividad | Factor | Unidad | Fuente |
|---|---|---|---|
| Consumo de luz | 0.444 | kg CO2e por kWh | SEMARNAT, aviso FESEN 2024 |
| Gasolina | 2.32 | kg CO2 por litro | EPA, GHG Emission Factors Hub 2025, Tabla 2 |
| Diésel | 2.70 | kg CO2 por litro | EPA, GHG Emission Factors Hub 2025, Tabla 2 |
| Residuo a relleno sanitario | 0.64 | kg CO2e por kg | EPA, GHG Emission Factors Hub 2025, Tabla 9 |
| Reciclaje | 0.10 | kg CO2e por kg | EPA, GHG Emission Factors Hub 2025, Tabla 9 |

## Cómo obtuve los valores

El factor de la luz es el oficial de México. La SEMARNAT publicó que el factor del Sistema Eléctrico Nacional 2024 es de 0.444 toneladas de CO2e por MWh, y en mayo de 2026 avisó que se sigue usando mientras sale el de 2025. Como 1 tonelada son 1000 kg y 1 MWh son 1000 kWh, el valor queda igual en kg por kWh.

Para gasolina y diésel usé la Tabla 2 de la EPA, que da 8.78 kg de CO2 por galón de gasolina y 10.21 por galón de diésel. Dividí entre 3.785, que son los litros que tiene un galón, porque en el programa las cantidades se capturan en litros.

Los residuos salen de la Tabla 9 de la EPA, renglón Mixed MSW, columna Landfilled (0.58), y renglón Mixed Recyclables, columna Recycled (0.09). Esos valores vienen en toneladas métricas de CO2e por tonelada corta, así que multipliqué por 1000 y dividí entre 907.18, que son los kg de una tonelada corta.

Comparado con la guía, la luz, la gasolina y el diésel casi no cambian. Los que sí cambian son relleno (de 0.5 a 0.64) y reciclaje (de 0.05 a 0.10), así que hay que actualizarlos en modelos/actividad.py.