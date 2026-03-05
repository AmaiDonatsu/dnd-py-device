import paho.mqtt.client as mqtt
import json
import time

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "instrumento/telemetria/nota"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado ao broker MQTT!")
    else:
        print("Falha na conexão, código de erro:", rc)

client = mqtt.Client()
client.on_connect = on_connect

client.connect(BROKER, PORT, 60)
client.loop_start()

def send_note(frec, note_name):
    payload = {
        "timestamp": int(time.time()),
        "frequency": frec,
        "note": note_name
    }
    client.publish(TOPIC, json.dumps(payload), qos=0)