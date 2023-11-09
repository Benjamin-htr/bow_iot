import arcade

UPDATES_PER_FRAME = 3


class DummySprite(arcade.Sprite):
    """Represents the dummy sprite

    Args:
        arcade (arcade.Sprite): Parent class
    """

    def __init__(self, scale, center_x, center_y, window_height):
        super().__init__()
        self.center_x = center_x
        self.center_y = center_y

        self.scale = scale
        self.hitted = False

        self.cur_texture = 0

        self.window_height = window_height

        # Load texture for idle animation
        self.idle_dummy = arcade.load_texture("../assets/static_dummy.png")

        # Load texture for hitted animation
        self.hitted_dummy_textures = arcade.load_spritesheet(
            "../assets/hitted_dummy.png", 140, 110, 3, 6
        )

    def set_center_y(self, center_y):
        """Set the center y of the dummy

        Args:
            center_y (int): Center y of the dummy
        """
        max_y = self.window_height - self.idle_dummy.height / 2
        min_y = self.idle_dummy.height / 2
        if min_y < center_y < max_y:
            self.center_y = max(min_y, min(center_y, max_y))

    def update_animation(self, delta_time: float = 1 / 60):
        # dummy Idle animation
        if not self.hitted:
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
