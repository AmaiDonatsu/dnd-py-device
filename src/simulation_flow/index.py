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

    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting simulation...")


