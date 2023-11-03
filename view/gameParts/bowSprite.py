import math

import arcade


class BowSprite(arcade.Sprite):
    def __init__(self, scale, update_per_frame) : 
         # Set up parent class
        super().__init__()

        # Used for flipping between image sequences
        self.cur_texture = 0
        self.update_per_frame = update_per_frame

        self.change_bandage = 0
        self.bandage = 0
        self.max_bandage = 100

        self.scale = scale

        # Load texture for idle animation
        self.bow_idle = arcade.load_texture("assets/idle_bow.png")


        # Load texture for bandage animation
        self.bow_shooting_textures = arcade.load_spritesheet("assets/bandage_bow.png", 70, 90, 6, 24)
        print(len(self.bow_shooting_textures))


    def update_animation(self, delta_time: float = 1 / 60):
        # bow Idle animation
        if self.change_bandage == 0 :
            self.texture = self.bow_idle
            self.cur_texture = 0
            return

        # bow bandage animation
        self.cur_texture += 1

        if self.cur_texture > (len(self.bow_shooting_textures)-1) * self.update_per_frame :
            self.cur_texture = 0

        frame = self.cur_texture // self.update_per_frame
        self.texture = self.bow_shooting_textures[frame] 

    def update(self):
        # Convert angle in degrees to radians.
        angle_rad = math.radians(self.angle)

        # Rotate the bow
        self.angle += self.change_angle

        # bow bandage animation
        self.bandage += self.change_bandage