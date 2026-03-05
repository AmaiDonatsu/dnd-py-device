import os
import time
import threading
import numpy as np

# Importamos nuestro administrador de MQTT
from src.client.mqtt_admin import connect_mqtt, send_note, stop_mqtt

os.environ['GPIOZERO_PIN_FACTORY'] = 'mock'

from gpiozero import LED, Button, Device

def audio_processing():
    FS = 44100  
    CHUNK_SIZE = 1024 
    F_NOTE = 440.0  # Frecuencia de la nota base (A4)

    print(f"[Audio] Simulando procesamiento de audio a {FS} Hz, bloque de {CHUNK_SIZE} muestras, nota {F_NOTE} Hz")
    print("--- Hilo de procesamiento de audio iniciado ---")

    while True:
        # Generar señal con ruido
        t = np.linspace(0, CHUNK_SIZE/FS, CHUNK_SIZE)
        signal = np.sin(2 * np.pi * F_NOTE * t) + np.random.normal(0, 0.1, CHUNK_SIZE)
        
        # Calcular FFT para detectar la frecuencia dominante
        spectr = np.abs(np.fft.fft(signal))
        freqs = np.fft.fftfreq(CHUNK_SIZE, 1/FS)
        indice_max = np.argmax(spectr[:CHUNK_SIZE//2])
        detected_freq = float(abs(freqs[indice_max]))

        # Simular envío de telemetría por MQTT de forma ocasional
        if np.random.rand() > 0.95:
            print(f"📡 [Telemetría] Enviando nota detectada: {detected_freq:.2f} Hz")
            # Enviamos al broker a través de nuestro cliente
            send_note(detected_freq, "A4-Sim")
            
        time.sleep(CHUNK_SIZE / FS)

def setup():
    led = LED(17)
    button = Button(2)

    button.when_pressed = led.toggle
    print("Setup complete. Press the button to toggle the LED.")
    print(f" pines: LED(17), Button(2) | Factory: {Device.pin_factory}")

def flow():
    # 1. Conectar a MQTT antes de empezar
    connect_mqtt()
    
    # 2. Configurar GPIO
    setup()

    # 3. Iniciar el hilo de procesamiento
    audio_thread = threading.Thread(target=audio_processing, daemon=True)
    audio_thread.start()

    print("--- Simulación activa (Presiona Ctrl+C para salir) ---")
    try:
        while True:
            time.sleep(2)
            print("Heartbeat: Simulación corriendo...")
    except KeyboardInterrupt:
        print("\nCerrando simulación y desconectando MQTT...")
        stop_mqtt()
