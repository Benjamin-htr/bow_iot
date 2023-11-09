import arcade
import arcade.gui as gui

from view.ChooseNameView import ChooseNameView
from view.GameView import GameView


class ScanRfidTag(arcade.View):
    """Represents the view where the player can scan his junia isen card

    Args:
        arcade (arcade.View): Parent class
    """

    def __init__(self):
        super().__init__()
        self.manager = gui.UIManager()
        self.manager.enable()
        self.h_box = gui.UIBoxLayout(vertical=False, space_between=50)
        self.is_confirm = False
        self.go_to_game = False

        # Create an text input field
        self.input_field = gui.UIInputText(
            color=arcade.color.DARK_BLUE_GRAY,
            font_size=24,
            width=200,
            text=self.window.logic.player.rfid_tag,
        )

        # Create a button
        submit_button = gui.UIFlatButton(
            color=arcade.color.DARK_BLUE_GRAY, text="Confirmer"
        )
        submit_button.on_click = self.confirm_rfid

        self.h_box.add(self.input_field)
        self.h_box.add(submit_button)

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                align_y=100,
                child=self.h_box,
            )
        )

    def on_show_view(self):
        self.set_rfid_tag(self.input_field.text)

        arcade.set_background_color(arcade.color.BUD_GREEN)

    def on_update(self, delta_time):
        if self.is_confirm:
            if self.go_to_game:
                self.show_game()
            else:
                self.show_choose_name()

    def on_draw(self):
        self.clear()
        self.manager.draw()

        arcade.draw_text(
            "Scan your Junia Isen card",
            self.window.width / 2,
            self.window.height - 100,
            arcade.color.WHITE,
            font_size=40,
            anchor_x="center",
            anchor_y="center",
        )

        arcade.draw_text(
            "Rfid tag: ",
            250,
            self.window.height - 200,
            arcade.color.WHITE,
            font_size=40,
            anchor_x="center",
            anchor_y="center",
        )

        arcade.draw_text(
            "Corresponding name: ",
            self.window.width / 2,
            self.window.height - 300,
            arcade.color.WHITE,
            font_size=40,
            anchor_x="center",
            anchor_y="center",
        )

        corresponding_name = "Pas de nom correspondant"
        if self.go_to_game:
            corresponding_name = self.window.logic.player.name

        arcade.draw_text(
            corresponding_name,
            self.window.width / 2,
            100,
            arcade.color.WHITE,
            font_size=40,
            anchor_x="center",
            anchor_y="center",
        )

    def on_key_press(self, key, modifiers):
        self.set_rfid_tag(self.input_field.text)
        return

    def set_rfid_tag(self, rfid_tag):
        self.go_to_game = self.window.logic.set_player(rfid_tag)
        return

    def confirm_rfid(self, event=None):
        """Confirm the rfid tag

        Args:
            event (arcade.gui.UIEvent, optional): Event. Defaults to None.
        """
        self.go_to_game = self.window.logic.set_player(self.input_field.text)
        print(self.window.logic.player.rfid_tag)
        print(self.window.logic.player.name)
        self.is_confirm = True

    def show_game(self):
        """Shows the game

        Args:
            event (arcade.gui.UIEvent): Event that triggered the function
        """
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)

    def show_choose_name(self):
        """Shows the choose name view

        Args:
            event (arcade.gui.UIEvent): Event that triggered the function
        """
        choose_name_view = ChooseNameView()
        self.window.show_view(choose_name_view)
