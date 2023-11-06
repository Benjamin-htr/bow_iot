import os

import arcade
import arcade.gui

from view.choose_name import ChooseName
from view.game import GameView
from view.score import ScoreView

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)


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
            self.window.width / 2,
            self.window.height / 1.5,
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
