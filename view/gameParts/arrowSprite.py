import arcade


class ArrowSprite(arcade.Sprite):
    def __init__(self, scale, center_x, center_y, angle, arrow_logic_id):
        super().__init__()
        self.scale = scale

        self.center_x = center_x
        self.center_y = center_y
        self.angle = angle
        self.arrow_logic_id = arrow_logic_id

        # Load texture for idle animation
        self.idle_arrow = arcade.load_texture("../assets/static_arrow.png")

    def update_animation(self, delta_time: float = 1 / 60):
        # arrow Idle animation
        self.texture = self.idle_arrow

    def update(self, center_x, center_y, angle):
        self.center_x = center_x
        self.center_y = center_y
        self.angle = angle

        return
