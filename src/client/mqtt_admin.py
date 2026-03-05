import paho.mqtt.client as mqtt
import json
import time

# Configuración del Broker Público
BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "instrumento/telemetria/nota"

def on_connect(client, userdata, flags, rc, properties=None):
    """Callback que se ejecuta cuando el cliente se conecta al broker."""
    if rc == 0:
        print("✅ [MQTT] Conectado al broker correctamente!")
    else:
        print(f"❌ [MQTT] Error de conexión, código: {rc}")

def on_disconnect(client, userdata, flags, rc, properties=None):
    """Callback que se ejecuta cuando el cliente se desconecta."""
    print(f"⚠️ [MQTT] Desconectado del broker (Código: {rc}).")

# Inicializar el cliente (usando la API v2 de Paho)
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_disconnect = on_disconnect

def connect_mqtt():
    """Establece la conexión y arranca el bucle en segundo plano."""
    try:
        print(f"🔗 [MQTT] Conectando a {BROKER}...")
        client.connect(BROKER, PORT, 60)
        # loop_start() corre en un hilo separado para no bloquear la app
        client.loop_start()
    except Exception as e:
        print(f"❌ [MQTT] No se pudo conectar: {e}")

def send_note(frec, note_name):
    """Envía un mensaje JSON con la frecuencia y el nombre de la nota."""
    payload = {
        "timestamp": int(time.time()),
        "frequency": round(frec, 2),
        "note": note_name
    }
    
    # Publicar el mensaje (qos=0 es 'enviar y olvidar', ideal para telemetría rápida)
    result = client.publish(TOPIC, json.dumps(payload), qos=0)
    
    # Verificar si el mensaje se envió a la cola de salida
    if result.rc != mqtt.MQTT_ERR_SUCCESS:
        print("❌ [MQTT] Error al intentar publicar el mensaje.")

def stop_mqtt():
    """Limpia la conexión antes de salir."""
    client.loop_stop()
    client.disconnect()
    print("🛑 [MQTT] Conexión cerrada.")
