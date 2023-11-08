import arcade
import os
from model.Logic import Logic
from view.GameView import GameView
from view.MenuView import MenuView

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 619


def launch_app():
    """Main function"""
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Archer challenge")
    window.logic = Logic()
    menu_view = MenuView()
    window.show_view(menu_view)
    # game_view = GameView()
    # game_view.setup()
    # window.show_view(game_view)
    arcade.run()


if __name__ == "__main__":
    os.environ['PYOPENGL_PLATFORM'] = 'egl'
    launch_app()
