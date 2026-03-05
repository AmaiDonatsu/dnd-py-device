# Developer Docs

## Resumen
código fuente de dnd-py-device, el dispositivo físico de medición de la arquitectura de danami

## Arquitectura

### Danami

Danami es una apliación escritorio con la función de analizar de forma digital lecturas de circuitos electricos, organizando los datos crudos del circuito en lecturas sintetizada

### Danami dnd-py-device

Danami recibe los datos de los circuitos en tiempo real por parte de dnd-py-device, este dispositivo, construido en base orange pi / raspberry pi, se encarga de procesar los datos digitalizados (por otro componente conectado), y enviarlos al servidor principal de danami

el código fuente se divide en 2, la simulación de lectura en un docker image [index](../../src/simulation_flow/index.py) y el código de producción para funcionar en orange pi [proximo]