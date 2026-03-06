import paho.mqtt.client as mqtt
import json

# Misma configuración que en mqtt_admin.py
BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "instrumento/telemetria/nota"

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("✅ [Subscriber] Conectado al broker!")
        # Nos suscribimos al tópico de telemetría
        client.subscribe(TOPIC)
        print(f"📡 [Subscriber] Escuchando en el tópico: {TOPIC}")
        print("--- Esperando mensajes... ---")
    else:
        print(f"❌ Error de conexión: {rc}")

def on_message(client, userdata, msg):
    # Procesar el mensaje recibido
    try:
        payload = json.loads(msg.payload.decode())
        print(f"📦 Mensaje Recibido: {payload}")
    except Exception as e:
        print(f"⚠️ Error decodificando mensaje: {e}")

# Configurar cliente
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

try:
    print(f"🔗 Conectando a {BROKER}...")
    client.connect(BROKER, PORT, 60)
    # loop_forever() bloquea el hilo principal y se queda escuchando
    client.loop_forever()
except KeyboardInterrupt:
    print("\n🛑 Deteniendo el suscriptor...")
    client.disconnect()
