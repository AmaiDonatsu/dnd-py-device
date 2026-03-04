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
    button.pin.drive_low()

    if button.is_pressed:
        led.on()
        print(f"button is pressed, turning on LED {led.is_lit}")
        

    time.sleep(1)
    led.off()
    print(f"LED turned off: {not led.is_lit}")


if __name__ == "__main__":
    main()
