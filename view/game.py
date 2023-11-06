import math

import arcade

from model.Arrow import Arrow
from view.gameParts.arrowSprite import ArrowSprite
from view.gameParts.bowSprite import BowSprite
from view.gameParts.dummySprite import DummySprite
from view.gameParts.powerIndicator import PowerIndicator

BOW_SCALING = 1.5
DUMMY_SCALING = 2
ARROW_SCALING = 1.5

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 619

ANGLE_SPEED = 5
BANDAGE_SPEED = 1

# Transform from the meters position to the pixel position
def transform_position(position) :
    return (position[0] * 12 + 60, position[1] * 12 + SCREEN_HEIGHT // 3.5)


class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        self.bow = None
        self.dummy = None
        self.arrows = arcade.SpriteList()
        self.power_indicator = None
        self.background = None

        self.score = 0

    def setup(self):
        # Set up the bow
        self.bow = BowSprite(BOW_SCALING, 60, SCREEN_HEIGHT // 3.5)

        #Set up the dummy
        self.dummy = DummySprite(DUMMY_SCALING, SCREEN_WIDTH - 150, SCREEN_HEIGHT // 3.5)

        # Set up the power indicator
        self.power_indicator = PowerIndicator(SCREEN_WIDTH - 50, 100, 20, 100, 5)

        # Set up the background
        self.background = arcade.load_texture("../assets/background.png")

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

        # Draw the arrow
        self.arrows.draw()


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
            self.launch_arrow()

        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.bow.change_angle = 0
             

    def on_update(self, delta_time):
        # Move the player
        self.bow.update()

        # Update the players animation
        self.bow.update_animation()

        # Update the power indicator
        self.power_indicator.update(self.bow.power)

        # Generate a list of all sprites that collided with the player.
        arrows_hit_list = arcade.check_for_collision_with_list(self.dummy,
                                                              self.arrows)

        # Loop through each colliding sprite, remove it, and add to the score.
        for arrow in arrows_hit_list:
            self.window.logic.rm_arrow(arrow.arrow_logic_id)
            arrow.remove_from_sprite_lists()
            self.dummy.hitted = True
            self.score += 1

        # Update the arrow animation
        self.arrows.update_animation()

        for arrow in self.arrows:
            self.window.logic.update_arrow(arrow.arrow_logic_id, delta_time)
            new_position = transform_position(self.window.logic.get_arrow(arrow.arrow_logic_id).position)
            arrow.update(new_position[0], new_position[1], self.window.logic.get_arrow(arrow.arrow_logic_id).get_angle())

        #delete the arrow if it is out of the screen
        for arrow in self.arrows:
            if arrow.center_x > SCREEN_WIDTH or arrow.center_x < 0 or arrow.center_y < 0:
                self.window.logic.rm_arrow(arrow.arrow_logic_id)
                arrow.remove_from_sprite_lists()


        print("arrow number : ", len(self.arrows))


        # Update the dummy animation
        self.dummy.update_animation()


        print("bandage : ", self.bow.power, " angle :", self.bow.angle)

    def launch_arrow(self):
        new_arrow_index = self.window.logic.add_arrow((0, 0))
        self.window.logic.get_arrow(new_arrow_index).set_initial_velocity(self.bow.angle, self.bow.power)
        self.arrows.append(ArrowSprite(ARROW_SCALING, 60, SCREEN_HEIGHT // 3.5, self.bow.angle, new_arrow_index))





def test_game():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Archer challenge")
    window.total_score = 0
    game_view = GameView()
    game_view.setup()
    window.show_view(game_view)
    arcade.run()

if __name__ == "__main__":
    test_game()
