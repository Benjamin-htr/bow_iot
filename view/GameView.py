import threading

import arcade

from view.game_parts.ArrowSprite import ArrowSprite
from view.game_parts.BowSprite import BowSprite
from view.game_parts.DummySprite import DummySprite
from view.game_parts.PowerIndicator import PowerIndicator
from view.game_parts.TopBarGui import TopBarGui
from view.ScoreView import ScoreView

BOW_SCALING = 1.5
DUMMY_SCALING = 2
ARROW_SCALING = 1.5


def transform_position(position, initial_position=(0, 0)):
    """Transforms the position of the arrow from the logic to the view

    Args:
        position (tuple): Position of the arrow in the logic
        initial_position (tuple, optional): Initial position of the arrow in the view. Defaults to (0, 0).
    """
    return (
        position[0] * 12 + initial_position[0],
        position[1] * 12 + initial_position[1],
    )


class GameView(arcade.View):
    """Represents the view where the player can play the game

    Args:
        arcade (arcade.View): Parent class
    """

    def __init__(self):
        super().__init__()

        self.bow: BowSprite = None
        self.dummy = None
        self.arrows = arcade.SpriteList()
        self.power_indicator = None
        self.top_bar_gui = None
        self.background = None
        self.initial_position_x = 60
        self.initial_position_y = self.window.height // 3.5

    def setup(self):
        """Set up the game"""

        # Set up the bow
        self.bow = BowSprite(
            BOW_SCALING,
            self.initial_position_x,
            self.initial_position_y,
            self.window.logic.bow,
        )
        self.window.logic.bow.load_sprite(self.bow)

        # Set up the dummy
        self.dummy = DummySprite(
            DUMMY_SCALING,
            self.window.width - 150,
            self.window.height // 3.5,
            window_height=self.window.height,
        )

        # Set up the power indicator
        self.power_indicator = PowerIndicator(self.window.width - 50, 100, 20, 100, 5)

        # Set up the top bar GUI
        self.top_bar_gui = TopBarGui(
            20,
            self.window.logic.player.name,
            self.window.width,
            self.window.height,
        )

        # Set up the background
        self.background = arcade.load_texture("../assets/background.png")

    def on_show_view(self):
        """Called when the view is shown"""

        if self.window.mqtt_obs:
            self.window.mqtt_obs.reset()
            self.window.mqtt_obs.onButton1Pressed = self.window.logic.bow.bandage
            self.window.mqtt_obs.onButton1Released = self.launch_arrow
            self.window.mqtt_obs.onPotarChanged = self.window.logic.bow.set_angle

        self.window.logic.start_game()

        return

    def on_draw(self):
        self.clear()

        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(
            0, 0, self.window.width, self.window.height, self.background
        )

        # Draw all the sprites.
        self.bow.draw()

        # Draw the dummy
        self.dummy.draw()

        # Draw power indicator bar
        self.power_indicator.draw()

        # Draw the top bar gui
        self.top_bar_gui.draw()

        # Draw the arrow
        self.arrows.draw()

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        # when the key is pressed, the bow is bandaged, it depends on the time the key is pressed
        if key == arcade.key.SPACE:
            self.window.logic.bow.bandage()

        # Rotate left/right
        elif key == arcade.key.LEFT:
            self.window.logic.bow.turn_left()
        elif key == arcade.key.RIGHT:
            self.window.logic.bow.turn_right()
        elif key == arcade.key.ESCAPE:
            self.finish_game()
        elif key == arcade.key.A:
            self.window.logic.bow.add_angle(40)
        elif key == arcade.key.Z:
            self.window.logic.bow.add_angle(-40)
        elif key == arcade.key.UP:
            self.dummy.set_center_y(self.dummy.center_y + 10)
        elif key == arcade.key.DOWN:
            self.dummy.set_center_y(self.dummy.center_y - 10)

    def on_key_release(self, key, modifiers):
        # when the key is released, the arrow is shot
        if key == arcade.key.SPACE:
            self.launch_arrow()

        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.window.logic.bow.stop_turn()

    def on_update(self, delta_time):
        # We check if the game is finished
        if self.window.logic.timer.remaining_time <= 0:
            self.finish_game()

        # We update the bow
        self.bow.update()
        self.window.logic.bow.update()

        # Update the players animation
        self.bow.update_animation()

        # Update the power indicator
        self.power_indicator.update(self.window.logic.bow.power)

        # Update the top bar gui
        self.top_bar_gui.update(
            self.window.logic.timer.remaining_time,
            self.window.logic.player.score,
        )

        self.check_colissions()

        # Update the arrow animation
        self.arrows.update_animation()

        for arrow in self.arrows:
            self.window.logic.update_arrow(arrow.arrow_logic_id, delta_time)
            new_position = transform_position(
                self.window.logic.get_arrow(arrow.arrow_logic_id).position,
                (self.initial_position_x, self.initial_position_y),
            )
            print(new_position)
            arrow.update(
                new_position[0],
                new_position[1],
                self.window.logic.get_arrow(arrow.arrow_logic_id).get_angle(),
            )

        # delete the arrow if it is out of the screen
        for arrow in self.arrows:
            if (
                arrow.center_x > self.window.width
                or arrow.center_x < 0
                or arrow.center_y < 0
            ):
                self.window.logic.rm_arrow(arrow.arrow_logic_id)
                arrow.remove_from_sprite_lists()

        # Update the dummy animation
        self.dummy.update_animation()

        print(
            "bow logic angle : ",
            self.window.logic.bow.get_angle(),
            "bow sprite angle : ",
            self.bow.angle,
        )
        print(
            "bow logic power : ",
            self.window.logic.bow.power,
        )
        print(
            "nb arrows logic : ",
            len(self.window.logic.get_arrows()),
            "nb arrows view : ",
            len(self.arrows),
        )

    def check_colissions(self):
        """Check if an arrow has hit the dummy"""
        # Generate a list of all sprites that collided with the player.
        arrows_hit_list = arcade.check_for_collision_with_list(self.dummy, self.arrows)

        # Loop through each colliding sprite, remove it, and add to the score.
        for arrow in arrows_hit_list:
            self.window.logic.rm_arrow(arrow.arrow_logic_id)
            arrow.remove_from_sprite_lists()
            self.dummy.hitted = True
            self.window.logic.hitted()

    def launch_arrow(self):
        """Launch an arrow"""
        new_arrow_index = self.window.logic.launch_arrow()
        self.arrows.append(
            ArrowSprite(
                ARROW_SCALING,
                self.initial_position_x,
                self.initial_position_y,
                self.window.logic.bow.get_angle(),
                new_arrow_index,
            )
        )
        self.window.logic.bow.stop_bandage()
        self.window.logic.timer.start()

    def finish_game(self):
        """Finishes the game and shows the score"""
        self.window.logic.stop_game()
        score_view = ScoreView()
        self.window.show_view(score_view)
