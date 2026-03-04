import os
import time
import threading

os.environ['GPIOZERO_PIN_FACTORY'] = 'mock'

from gpiozero import LED, Button, Device

def audio_processing():
    garbage_list = []
    while True:
        if len(garbage_list) > 1000:
            garbage_list.append([0.0] * 1000)
        time.sleep(0.01)

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


