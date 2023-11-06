import arcade.gui
import arcade
import json


WIDTH = 800
HEIGHT = 600
SPRITE_SCALING = 0.5


class ScoreView(arcade.View):
    def __init__(self):
        super().__init__()
        self.scroll_offset = 0  # Initial scroll offset
        self.scroll_speed = 1  # Scroll speed
        self.nb_lines_to_display = 15  # Number of lines to display
        self.text_color = arcade.color.BLACK  # Couleur du texte (Dark Cyan)
        self.data = []  # Your data from the JSON file
        with open("../score.json", "r") as json_file:
            self.data = json.load(json_file)
        self.data = sorted(self.data, key=lambda x: x["score"], reverse=True)
        self.arrow_up_texture = arcade.load_texture(
            ":resources:onscreen_controls/shaded_dark/up.png"
        )
        self.arrow_down_texture = arcade.load_texture(
            ":resources:onscreen_controls/shaded_dark/down.png"
        )
        self.exit_texture = arcade.load_texture(":resources:images/tiles/signExit.png")

        self.arrow_button_width = self.arrow_up_texture.width
        self.arrow_button_height = self.arrow_up_texture.height

    def on_show_view(self):
        background_color = (255, 228, 181)  # Couleur de fond (Blanched Almond)
        self.text_color = arcade.color.BLACK  # Couleur du texte (Dark Cyan)

        arcade.set_background_color(background_color)
        self.window.on_key_press = self.on_key_press
        self.window.on_key_release = self.on_key_release

    def on_draw(self):
        # Open and read the JSON file

        self.clear()
        arcade.draw_texture_rectangle(
            WIDTH - 650,
            HEIGHT - 420,
            self.exit_texture.width,
            self.exit_texture.height,
            self.exit_texture,
        )
        arcade.draw_text(
            "Highest scores : ",
            WIDTH / 2,
            HEIGHT / 1.25,
            self.text_color,  # Utilisation de la couleur de texte
            font_size=40,
            anchor_x="center",
        )
        self.uimanager = arcade.gui.UIManager()
        self.uimanager.enable()

        # Determine the starting and ending indices for the visible lines
        start_index = self.scroll_offset
        end_index = start_index + self.nb_lines_to_display

        # Iterate through the data and draw the visible lines
        y = HEIGHT - 150  # Initial Y position for the first line
        for i in range(start_index, min(end_index, len(self.data))):
            item = self.data[i]
            name = item["name"]
            score = item["score"]

            # Create a formatted string for each data line
            data_line = f" {name}, Score: {score}"

            # Draw the data line
            arcade.draw_text(
                data_line,
                WIDTH / 2,
                y,
                arcade.color.BLACK,
                font_size=16,
                anchor_x="center",
                anchor_y="center",
            )

            y -= 20  # Move the Y position for the next line

        if len(self.data) > self.nb_lines_to_display:
            arcade.draw_texture_rectangle(
                WIDTH - 60,
                HEIGHT - 60,
                self.arrow_button_width,
                self.arrow_button_height,
                self.arrow_up_texture,
            )

            # Arrow button (down)
            arcade.draw_texture_rectangle(
                WIDTH - 60,
                60,
                self.arrow_button_width,
                self.arrow_button_height,
                self.arrow_down_texture,
            )

        self.uimanager.draw()

    def scrollUp(self):
        self.scroll_offset += self.scroll_speed
        self.scroll_offset = max(0, min(self.scroll_offset, len(self.data) - 1))

    def scrollDown(self):
        self.scroll_offset -= self.scroll_speed
        self.scroll_offset = max(0, min(self.scroll_offset, len(self.data) - 1))

    def on_mouse_press(self, x, y, button, modifiers):
        if (
            WIDTH - 650 - self.exit_texture.width / 2
            <= x
            <= WIDTH - 650 + self.exit_texture.width / 2
            and HEIGHT - 420 - self.exit_texture.height / 2
            <= y
            <= HEIGHT - 420 + self.exit_texture.height / 2
        ):
            from menu import MainMenuView

            menu_view = MainMenuView()
            self.window.show_view(menu_view)

        if len(self.data) > self.nb_lines_to_display:
            if button == arcade.MOUSE_BUTTON_LEFT:
                # Check if the click is within the up arrow button
                if (
                    WIDTH - 60 - self.arrow_button_width / 2
                    <= x
                    <= WIDTH - 60 + self.arrow_button_width / 2
                    and HEIGHT - 60 - self.arrow_button_height / 2
                    <= y
                    <= HEIGHT - 60 + self.arrow_button_height / 2
                ):
                    self.scrollDown()

                # Check if the click is within the down arrow button
                elif (
                    WIDTH - 60 - self.arrow_button_width / 2
                    <= x
                    <= WIDTH - 60 + self.arrow_button_width / 2
                    and 60 - self.arrow_button_height / 2
                    <= y
                    <= 60 + self.arrow_button_height / 2
                ):
                    self.scrollUp()
