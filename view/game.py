import math

import arcade
from gameParts.bowSprite import BowSprite
from gameParts.powerIndicator import PowerIndicator

BOW_SCALING = 1

UPDATES_PER_FRAME = 3

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

ANGLE_SPEED = 5
BANDAGE_SPEED = 1


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        # Set up the bow
        self.bow = None
        self.power_indicator = None

        self.score = 0

    def setup(self):
        # Set up the bow
        self.bow = BowSprite(BOW_SCALING)

        # Set up the power indicator
        self.power_indicator = PowerIndicator(SCREEN_WIDTH - 50, SCREEN_HEIGHT // 2, 20, 100, 5)

        self.bow.center_x = 50
        self.bow.center_y = SCREEN_HEIGHT // 2



    def on_show_view(self):
        arcade.set_background_color(arcade.color.VIOLET_BLUE)
        return

    def on_draw(self):
        self.clear()

         # Draw all the sprites.
        self.bow.draw()

        # Draw power indicator bar
        self.power_indicator.draw()

         # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)


    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        #when the key is pressed, the bow is bandaged, it depends on the time the key is pressed
        if key == arcade.key.SPACE:
            self.bow.change_power = BANDAGE_SPEED

        # Rotate left/right
        elif key == arcade.key.LEFT:
            self.bow.change_angle = ANGLE_SPEED
        elif key == arcade.key.RIGHT:
            self.bow.change_angle = -ANGLE_SPEED


    def on_key_release(self, key, modifiers):
        #when the key is released, the arrow is shot
        if key == arcade.key.SPACE:
            self.bow.change_power = 0

        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.bow.change_angle = 0
             

    def on_update(self, delta_time):
        # Move the player
        self.bow.update()

        # Update the players animation
        self.bow.update_animation()

        # Update the power indicator
        self.power_indicator.update(self.bow.power)


        print("bandage : ", self.bow.power, " angle :", self.bow.angle)



def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Archer challenge")
    window.total_score = 0
    game_view = GameView()
    game_view.setup()
    window.show_view(game_view)
    arcade.run()
    

if __name__ == "__main__":
    main()