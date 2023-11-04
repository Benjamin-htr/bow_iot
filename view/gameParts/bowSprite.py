import math

import arcade


class BowSprite(arcade.Sprite):
    def __init__(self, scale, center_x, center_y):
         # Set up parent class
        super().__init__()
        self.center_x = center_x
        self.center_y = center_y

        self.change_power = 0
        self.power = 0
        self.max_power = 100

        self.scale = scale

        # Load texture for idle animation
        self.bow_idle = arcade.load_texture("assets/idle_bow.png")


        # Load texture for bandage animation
        self.bow_shooting_textures = arcade.load_spritesheet("assets/bandage_bow_shorter.png", 70, 90, 6, 12)
        print(len(self.bow_shooting_textures))


    def update_animation(self, delta_time: float = 1 / 60):
        # bow Idle animation
        if self.change_power == 0 :
            self.texture = self.bow_idle
            return

        # Calculate the frame based on the power level
        frame = self.power * (len(self.bow_shooting_textures) - 1) // self.max_power

        # Ensure frame index is within the range of available textures
        frame = max(0, min(frame, len(self.bow_shooting_textures) - 1))

        # Set the texture for the current frame
        self.texture = self.bow_shooting_textures[frame]

    def update(self):
        # Convert angle in degrees to radians.
        angle_rad = math.radians(self.angle)

        # Rotate the bow
        self.angle += self.change_angle

        # bow bandage animation
        self.power += self.change_power
        if self.power > self.max_power :
            self.power = 0

        if self.change_power == 0 :
            self.power = 0