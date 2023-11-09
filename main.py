import os

import arcade

from model.Logic import Logic
from mosquitto.controller import mqtt_observer
from view.MenuView import MenuView

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 619


def bool_input():
    """Ask the user if he wants to use the iot controller"""

    yes_no = input("Do you want to use iot controller (with mqtt) ? (y/n) ")
    while yes_no.lower() not in ["y", "n"]:
        yes_no = input("Do you want to use MQTT? (y/n) ")
    if yes_no.lower() == "y":
        return True
    return False


def launch_app():
    """Main function"""
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Archer challenge")
    window.logic = Logic()
    iot_controller_enabled = bool_input()
    if iot_controller_enabled:
        window.mqtt_obs = mqtt_observer()
    else:
        window.mqtt_obs = None
    menu_view = MenuView()
    window.show_view(menu_view)

    arcade.run()


if __name__ == "__main__":
    os.environ["PYOPENGL_PLATFORM"] = "egl"
    launch_app()
