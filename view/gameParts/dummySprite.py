import arcade

UPDATES_PER_FRAME = 3


class DummySprite(arcade.Sprite):
    def __init__(self, scale, center_x, center_y):
        super().__init__()
        self.center_x = center_x
        self.center_y = center_y

        self.scale = scale
        self.hitted = False

        self.cur_texture = 0

        # Load texture for idle animation
        self.idle_dummy = arcade.load_texture("../assets/static_dummy.png")

        # Load texture for hitted animation
        self.hitted_dummy_textures = arcade.load_spritesheet(
            "../assets/hitted_dummy.png", 140, 110, 3, 6
        )

    def update_animation(self, delta_time: float = 1 / 60):
        # dummy Idle animation
        if self.hitted == False:
            self.texture = self.idle_dummy
            return

        # dummy hitted animation
        self.cur_texture += 1
        if self.cur_texture > 5 * UPDATES_PER_FRAME:
            self.cur_texture = 0
        frame = self.cur_texture // UPDATES_PER_FRAME
        self.texture = self.hitted_dummy_textures[frame]

        if frame == 5:
            self.hitted = False

    def update(self):
        return
