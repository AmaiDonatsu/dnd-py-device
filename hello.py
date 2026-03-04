from src.utils.physical_plataform import we_are_in_SBC
from src.utils.physical_plataform import get_SBC_model

import time

from gpiozero import LED, Button, Device


def main():
    print("Hello from dnd-py-device!")

    if we_are_in_SBC():
        print("Running on SBC.")
        print(f"SBC Model: {get_SBC_model()}")
    else:
        print("Running on desktop.")
        from src.simulation_flow.index import flow
        flow()

if __name__ == "__main__":
    main()
