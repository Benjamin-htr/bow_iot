"""
This program shows how to:
  * Have one or more instruction screens
  * Show a 'Game over' text and halt the game
  * Allow the user to restart the game

Make a separate class for each view (screen) in your game.
The class will inherit from arcade.View. The structure will
look like an arcade.Window as each view will need to have its own draw,
update and window event methods. To switch a view, simply create a view
with `view = MyView()` and then use the view.show() method.

This example shows how you can set data from one View on another View to pass data
around (see: time_taken), or you can store data on the Window object to share data between
all Views (see: total_score).

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.view_instructions_and_game_over.py
"""
import os
import random

import arcade
import arcade.gui

from view.choose_name import ChooseName
from view.game import GameView
from view.score import ScoreView

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)


WIDTH = 800
HEIGHT = 600
SPRITE_SCALING = 0.5


class MainMenuView(arcade.View):
    def __init__(self):
        super().__init__()

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        button_style = {
            "font_name": ("Comic Sans MS"),
            "font_size": 20,
            "font_color": arcade.color.BLACK,
            "border_width": 2,
            "border_color": None,
            "bg_color": arcade.color.GRULLO,
        }

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout(space_between=20)

        start_button = arcade.gui.UIFlatButton(text="Play", width=200, height=50, style=button_style)

        score_button = arcade.gui.UIFlatButton(text="Score", width=200, height=50, style=button_style)

        quit_button = arcade.gui.UIFlatButton(text="Exit", width=200, height=50, style=button_style)

        quit_button.on_click = self.exit
        score_button.on_click = self.showScores
        start_button.on_click = self.showChooseName

        self.v_box.add(start_button)
        self.v_box.add(score_button)
        self.v_box.add(quit_button)


        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                align_y=-100,
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box,
            )
        )



    def on_show_view(self):
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

    def on_draw(self):
        self.clear()
        arcade.draw_text(
            "Welcome to Archer Challenge",
            WIDTH / 1.5,
            HEIGHT / 1.5,
            arcade.color.BLACK,
            font_size=40,
            anchor_x="center",
            anchor_y="center",
        )

        self.manager.draw()

    def exit(self, event):
        arcade.exit()

    def showScores(self, event):
        score_view = ScoreView()
        self.window.show_view(score_view)

    def showGame(self, event):
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)

    def showChooseName(self, event) :
        choose_name_view = ChooseName()
        self.window.show_view(choose_name_view)


def main():
    window = arcade.Window(WIDTH, HEIGHT, "Archer challenge")
    window.total_score = 0
    menu_view = MainMenuView()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()
