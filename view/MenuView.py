import os

import arcade
import arcade.gui

from view.ChooseNameView import ChooseNameView
from view.GameView import GameView
from view.ScoreView import ScoreView

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)


class MenuView(arcade.View):
    """Represents the view of the main menu where the player can choose to play or see the scores (or quit)

    Args:
        arcade (arcade.View): Parent class
    """

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

        start_button = arcade.gui.UIFlatButton(
            text="Play", width=200, height=50, style=button_style
        )

        score_button = arcade.gui.UIFlatButton(
            text="Score", width=200, height=50, style=button_style
        )

        quit_button = arcade.gui.UIFlatButton(
            text="Exit", width=200, height=50, style=button_style
        )

        quit_button.on_click = self.exit
        score_button.on_click = self.show_scores
        start_button.on_click = self.show_choose_name

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
        """Exits the game

        Args:
            event (arcade.gui.UIEvent): Event that triggered the function
        """
        arcade.exit()

    def show_scores(self, event):
        """Shows the scores

        Args:
            event (arcade.gui.UIEvent): Event that triggered the function
        """
        score_view = ScoreView()
        self.window.show_view(score_view)

    def show_game(self, event):
        """Shows the game

        Args:
            event (arcade.gui.UIEvent): Event that triggered the function
        """
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)

    def show_choose_name(self, event):
        """Shows the choose name view

        Args:
            event (arcade.gui.UIEvent): Event that triggered the function
        """
        choose_name_view = ChooseNameView()
        self.window.show_view(choose_name_view)
