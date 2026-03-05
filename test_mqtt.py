import time
from src.client.mqtt_admin import connect_mqtt, send_note, stop_mqtt

def test_connection():
    print("🚀 [TEST] Iniciando prueba de conexión MQTT...")
    connect_mqtt()
    
    # Esperamos 2 segundos para dar tiempo a que se conecte el loop en segundo plano
    time.sleep(2)
    
    print("📡 [TEST] Enviando nota de prueba...")
    send_note(440.0, "La4-Test")
    
    # Esperamos un poco más para asegurar que el mensaje sale
    time.sleep(2)
    
    print("🛑 [TEST] Cerrando conexión...")
    stop_mqtt()
    print("✅ [TEST] Prueba finalizada.")

if __name__ == "__main__":
    test_connection()
