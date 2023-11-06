import arcade


class ChooseName(arcade.View):
    def __init__(self):
        super().__init__()
        self.name = ""

        self.letter1 = "A"
        self.letter2 = "A"
        self.letter3 = "A"

    def on_show_view(self):
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

        arcade.draw_text(
            self.letter1,
            self.window.width / 2 - 100,
            self.window.height - 200,
            arcade.color.WHITE,
            font_size=40,
            anchor_x="center",
            anchor_y="center",
        )

        arcade.draw_text(
            self.letter2,
            self.window.width / 2,
            self.window.height - 200,
            arcade.color.WHITE,
            font_size=40,
            anchor_x="center",
            anchor_y="center",
        )

        arcade.draw_text(
            self.letter3,
            self.window.width / 2 + 100,
            self.window.height - 200,
            arcade.color.WHITE,
            font_size=40,
            anchor_x="center",
            anchor_y="center",
        )
        

        

      
        
