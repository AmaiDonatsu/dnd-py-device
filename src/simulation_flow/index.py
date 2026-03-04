import os
import time
import threading

os.environ['GPIOZERO_PIN_FACTORY'] = 'mock'

from gpiozero import LED, Button, Device

def audio_processing():
    garbage_list = []
    print("--- Hilo de procesamiento de audio iniciado ---")
    while True:
        # Simular carga de CPU con cálculos matemáticos
        _ = [x**2 for x in range(5000)]
        
        # Simular consumo de memoria añadiendo datos a una lista
        # Cada iteración añade unos 8KB aproximadamente
        garbage_list.append([0.1] * 1000)
        
        # Cada 50 iteraciones imprimimos el estado de la memoria simulada
        if len(garbage_list) % 50 == 0:
            print(f"Carga: {len(garbage_list)} bloques en memoria...")
            
        time.sleep(0.1)

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


