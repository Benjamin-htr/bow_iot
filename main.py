import json
# Ajout pour le plot
import math
from time import sleep

import arcade

from model.Logic import Logic
from view.menu import MainMenuView

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 619


def LaunchApp() : 
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Archer challenge")
    window.logic = Logic()
    menu_view = MainMenuView()
    window.show_view(menu_view)
    arcade.run()

if __name__ == "__main__":
    LaunchApp()
