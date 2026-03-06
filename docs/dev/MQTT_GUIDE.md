# 📡 Guía de MQTT para Desarrolladores

Esta guía explica cómo funciona la comunicación por MQTT en este proyecto y cómo puedes monitorear los datos que se están transmitiendo.

## 🏗️ Cómo funciona en este proyecto

El flujo de simulación en `src/simulation_flow/index.py` utiliza un cliente MQTT definido en `src/client/mqtt_admin.py`.

1.  **Conexión**: Al iniciar la simulación (`flow()`), se llama a `connect_mqtt()`.
2.  **Broker Público**: Actualmente usamos `test.mosquitto.org` en el puerto `1883`.
3.  **Transmisión**: Cada vez que el hilo de audio detecta una nota con alta probabilidad (> 95%), envía un JSON al tópico:
    `instrumento/telemetria/nota`

### Ejemplo del mensaje enviado (JSON):

```json
{
  "timestamp": 1709654400,
  "frequency": 440.0,
  "note": "A4-Sim"
}
```

---

## 🔍 Cómo monitorear la transmisión

Tienes varias formas de ver si los datos se están enviando correctamente:

### 1. Usando el script del proyecto (Recomendado)

He creado un pequeño script de "suscriptor" que escucha los mismos mensajes que envía la simulación. Abre una terminal nueva y ejecuta:

```bash
uv run test_mqtt_subscriber.py
```

_Si la simulación está corriendo en otra terminal, empezarás a ver los mensajes JSON llegar en tiempo real._

### 2. Usando herramientas de línea de comandos (`mosquitto_sub`)

Si tienes instalado el cliente de mosquitto en tu sistema:

```bash
mosquitto_sub -h test.mosquitto.org -t "instrumento/telemetria/nota" -v
```

### 3. Usando herramientas gráficas (MQTT Explorer)

Es la mejor opción para ver los datos de forma visual:

1.  Descarga e instala [MQTT Explorer](http://mqtt-explorer.com/).
2.  Crea una nueva conexión a: `test.mosquitto.org`.
3.  Busca en el árbol de tópicos: `instrumento` -> `telemetria` -> `nota`.

---

## 🛠️ Modificar el comportamiento

*   **Cambiar el Tópico**: Edita `src/client/mqtt_admin.py` y cambia la variable `TOPIC`.
*   **Frecuencia de envío**: En `src/simulation_flow/index.py`, ajusta la línea `if np.random.rand() > 0.95:`. Si bajas el `0.95` a `0.50`, enviará mensajes con mucha más frecuencia.
*   **Cambiar el Broker**: Si prefieres usar un broker local o uno privado, cambia la variable `BROKER` en `src/client/mqtt_admin.py`.
