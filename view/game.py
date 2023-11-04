import math

import arcade
from gameParts.bowSprite import BowSprite
from gameParts.dummySprite import DummySprite
from gameParts.powerIndicator import PowerIndicator

BOW_SCALING = 1.5
DUMMY_SCALING = 2

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 619

ANGLE_SPEED = 5
BANDAGE_SPEED = 1


class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        self.bow = None
        self.dummy = None
        self.power_indicator = None
        self.background = None

        self.score = 0

    def setup(self):
        # Set up the bow
        self.bow = BowSprite(BOW_SCALING)

        #Set up the dummy
        self.dummy = DummySprite(DUMMY_SCALING)

        # Set up the power indicator
        self.power_indicator = PowerIndicator(SCREEN_WIDTH - 50, 100, 20, 100, 5)

        # Set up the background
        self.background = arcade.load_texture("assets/background.png")

        self.bow.center_x = 60
        self.bow.center_y = SCREEN_HEIGHT // 3.5

        self.dummy.center_x = SCREEN_WIDTH - 150
        self.dummy.center_y = SCREEN_HEIGHT // 3.5



    def on_show_view(self):
        return

    def on_draw(self):
        self.clear()

        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

         # Draw all the sprites.
        self.bow.draw()

        # Draw the dummy
        self.dummy.draw()

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

        self.dummy.hitted = False


    def on_key_release(self, key, modifiers):
        #when the key is released, the arrow is shot
        if key == arcade.key.SPACE:
            self.bow.change_power = 0
            self.dummy.hitted = True

        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.bow.change_angle = 0
             

    def on_update(self, delta_time):
        # Move the player
        self.bow.update()

        # Update the players animation
        self.bow.update_animation()

        # Update the power indicator
        self.power_indicator.update(self.bow.power)

        # Update the dummy animation
        self.dummy.update_animation()


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