import arcade

from view.GameView import GameView

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class ChooseNameView(arcade.View):
    """Represents the view where the player can choose his name

    Args:
        arcade (arcade.Sprite): Parent class

    """

    def __init__(self):
        super().__init__()
        self.name = "AAA"
        self.current_letter = 0

        self.letter_pos_y = self.window.height - 300

        button_style = {
            "font_name": ("Comic Sans MS"),
            "font_size": 20,
            "font_color": arcade.color.BLACK,
            "border_width": 2,
            "border_color": None,
            "bg_color": arcade.color.GRULLO,
        }

        confirm_button = arcade.gui.UIFlatButton(
            text="Confirm", width=200, height=50, style=button_style
        )

        confirm_button.on_click = self.confirm_name

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                align_y=-150,
                anchor_x="center_x",
                anchor_y="center_y",
                child=confirm_button,
            )
        )
        self.is_confirm = False

    def on_show_view(self):
        if self.window.mqtt_obs:
            self.window.mqtt_obs.reset()
            self.window.mqtt_obs.onButton1Pressed = self.next_letter
            self.window.mqtt_obs.onPotarChanged = self.change_name_with_angle
            self.window.mqtt_obs.onButton1Pressed = self.previous_letter
            self.window.mqtt_obs.onButton2Pressed = self.confirm_name

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()

        arcade.draw_text(
            "Choose your name",
            self.window.width / 2,
            self.window.height - 100,
            arcade.color.WHITE,
            font_size=40,
            anchor_x="center",
            anchor_y="center",
        )

        # Draw the name
        for index, letter in enumerate(self.name):
            arcade.draw_text(
                letter,
                self.window.width / 2 - 100 + 100 * index,
                self.letter_pos_y,
                arcade.color.WHITE,
                font_size=40,
                anchor_x="center",
                anchor_y="center",
            )

        self.draw_around_letter()
        self.draw_cursor()

        # Draw the instructions
        arcade.draw_text(
            "Press ENTER or CLICK on BUTTON to confirm",
            self.window.width / 2,
            self.window.height - 580,
            arcade.color.WHITE,
            font_size=20,
            anchor_x="center",
            anchor_y="center",
        )

        # Draw button
        self.manager.draw()

        if self.is_confirm:
            self.window.logic.player.name = self.name
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)

    # change the name the angle of the potar between 0 and 360
    def change_name_with_angle(self, potar_angle):
        """Change the name with the angle of the potar"""
        self.name = (
            self.name[: self.current_letter]
            + ALPHABET[int(potar_angle / 360 * (len(ALPHABET) - 1))]
            + self.name[self.current_letter + 1 :]
        )

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.increase_letter()
        elif key == arcade.key.DOWN:
            self.decrease_letter()
        elif key == arcade.key.LEFT:
            self.previous_letter()
        elif key == arcade.key.RIGHT:
            self.next_letter()
        elif key == arcade.key.ENTER:
            self.confirm_name(None)

    def increase_letter(self):
        """Increase the current letter"""
        self.name = (
            self.name[: self.current_letter]
            + self.new_letter(self.name[self.current_letter], "up")
            + self.name[self.current_letter + 1 :]
        )

    def decrease_letter(self):
        """Decrease the current letter"""
        self.name = (
            self.name[: self.current_letter]
            + self.new_letter(self.name[self.current_letter], "down")
            + self.name[self.current_letter + 1 :]
        )

    def next_letter(self):
        """Change the current letter to the next one"""
        self.current_letter = (self.current_letter + 1) % len(self.name)

    def previous_letter(self):
        """Change the current letter to the previous one"""
        self.current_letter = (self.current_letter - 1) % len(self.name)

    def new_letter(self, letter, direction):
        """Returns the new letter

        Args:
            letter (str): Letter to change
            direction (str): Direction to change the letter
        """
        index = ALPHABET.index(letter)
        if direction == "up":
            index += 1
        elif direction == "down":
            index -= 1
        index = index % len(ALPHABET)
        return ALPHABET[index]

    def draw_around_letter(self):
        """Draws the letters around the current letter"""
        arcade.draw_text(
            ALPHABET[
                (ALPHABET.index(self.name[self.current_letter]) + 1) % len(ALPHABET)
            ],
            self.window.width / 2 - 100 + 100 * self.current_letter,
            self.letter_pos_y + 50,
            arcade.color.DIM_GRAY,
            font_size=25,
            anchor_x="center",
            anchor_y="center",
        )

        arcade.draw_text(
            ALPHABET[
                (ALPHABET.index(self.name[self.current_letter]) - 1) % len(ALPHABET)
            ],
            self.window.width / 2 - 100 + 100 * self.current_letter,
            self.letter_pos_y - 50,
            arcade.color.DIM_GRAY,
            font_size=25,
            anchor_x="center",
            anchor_y="center",
        )

    def draw_cursor(self):
        """Draw a rectangle around the current letter"" """
        arcade.draw_rectangle_outline(
            self.window.width / 2 - 100 + 100 * self.current_letter,
            self.letter_pos_y,
            50,
            55,
            arcade.color.BLUE,
            4,
        )

    def confirm_name(self, event=None):
        """Confirm the name and start the game

        Args:
            event (arcade.gui.UIEvent, optional): Event. Defaults to None.
        """
        self.is_confirm = True
