import os
import time
import threading
import numpy as np

os.environ['GPIOZERO_PIN_FACTORY'] = 'mock'

from gpiozero import LED, Button, Device

def audio_processing():
    garbage_list = []

    FS = 44100  # Frecuencia de muestreo
    CHUNK_SIZE = 1024  # Tamaño del bloque de audio
    F_NOTE = 440.0  # Frecuencia de la nota (A4)

    print(f"[Audio] Simulando procesamiento de audio a {FS} Hz, bloque de {CHUNK_SIZE} muestras, nota {F_NOTE} Hz")

    print("--- Hilo de procesamiento de audio iniciado ---")

    n=0
    while True:
        t = np.arange(n, n + CHUNK_SIZE) / FS
        digital_signal = np.sin(2 * np.pi * F_NOTE * t).astype(np.float32)
        processed = digital_signal * 0.5  # Simulación de procesamiento (reducción de volumen)

        _ = processed.tobytes()

        n+= CHUNK_SIZE
        time.sleep(CHUNK_SIZE / FS)
        

def setup():
    led = LED(17)
    button = Button(2)

    button.when_pressed = led.toggle
    print("Setup complete. Press the button to toggle the LED.")
    print(f" pines: LED(17), Button(2) | Factory: {Device.pin_factory}")

def flow():
    setup()

    audio_thread = threading.Thread(target=audio_processing, daemon=True)
    audio_thread.start()

    print("--- Simulación activa (Presiona Ctrl+C para salir) ---")
    try:
        while True:
            # Aquí podrías simular eventos o simplemente esperar
            time.sleep(2)
            print("Heartbeat: Simulación corriendo...")
    except KeyboardInterrupt:
        print("\nExiting simulation...")


