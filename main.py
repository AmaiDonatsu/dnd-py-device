import os
import time

os.environ['GPIOZERO_PIN_FACTORY'] = 'mock'

from gpiozero import LED, Button, Device


def main():
    print("Hello from dnd-py-device!")
    test_simulation()

def test_simulation():
    led = LED(17)
    button = Button(2)

    print(f"---init test in {Device.pin_factory}---")
    print("simulating button press...")

    if button.is_pressed:
        print("button is pressed, turning on LED")
        led.on()

    time.sleep(1)
    led.off()
    print(f"LED turned off: {not led.is_lit}")


if __name__ == "__main__":
    main()
