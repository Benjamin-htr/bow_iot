import arcade

from view.game import GameView

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class ChooseName(arcade.View):
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

        confirm_button = arcade.gui.UIFlatButton(text="Confirm", width=200, height=50, style=button_style)

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
        
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.name = self.name[:self.current_letter] + self.new_letter(self.name[self.current_letter], "up") + self.name[self.current_letter + 1:]
        elif key == arcade.key.DOWN:
            self.name = self.name[:self.current_letter] + self.new_letter(self.name[self.current_letter], "down") + self.name[self.current_letter + 1:]
        elif key == arcade.key.LEFT:
            self.current_letter = (self.current_letter - 1) % len(self.name)
        elif key == arcade.key.RIGHT:
            self.current_letter = (self.current_letter + 1) % len(self.name)
        elif key == arcade.key.ENTER:
            self.confirm_name(None)

    def new_letter(self, letter, direction):
        index = ALPHABET.index(letter)
        if direction == "up":
            index += 1
        elif direction == "down":
            index -= 1
        index = index % len(ALPHABET)
        return ALPHABET[index]
    
    def draw_around_letter(self):
        arcade.draw_text(
            ALPHABET[(ALPHABET.index(self.name[self.current_letter]) + 1) % len(ALPHABET)],
            self.window.width / 2 - 100 + 100 * self.current_letter,
            self.letter_pos_y + 50,
            arcade.color.DIM_GRAY,
            font_size=25,
            anchor_x="center",
            anchor_y="center",
        )

        arcade.draw_text(
            ALPHABET[(ALPHABET.index(self.name[self.current_letter]) - 1) % len(ALPHABET)],
            self.window.width / 2 - 100 + 100 * self.current_letter,
            self.letter_pos_y - 50,
            arcade.color.DIM_GRAY,
            font_size=25,
            anchor_x="center",
            anchor_y="center",
        )
    def draw_cursor(self) : 
        arcade.draw_rectangle_outline(
            self.window.width / 2 - 100 + 100 * self.current_letter,
            self.letter_pos_y,
            50,
            55,
            arcade.color.BLUE,
            4,
        )

    def confirm_name(self, event):
        self.window.logic.player.name = self.name
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)

        



        


        



      
        
