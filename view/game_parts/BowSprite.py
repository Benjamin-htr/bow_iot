import arcade


class BowSprite(arcade.Sprite):
    """Repsents the bow sprite

    Args:
        arcade (arcade.Sprite): Parent class
    """

    def __init__(self, scale, center_x, center_y, bow_logic):
        # Set up parent class
        super().__init__()
        self.center_x = center_x
        self.center_y = center_y

        self.bow_logic = bow_logic

        self.scale = scale

        # Load texture for idle animation
        self.bow_idle = arcade.load_texture("../assets/idle_bow.png")

        # Load texture for bandage animation
        self.bow_shooting_textures = arcade.load_spritesheet(
            "../assets/bandage_bow_shorter.png", 70, 90, 6, 12
        )
        print(len(self.bow_shooting_textures))

    def update_animation(self, delta_time: float = 1 / 60):
        # bow Idle animation
        if not self.bow_logic.is_charging:
            self.texture = self.bow_idle
            return

        # Calculate the frame based on the power level
        frame = (
            self.bow_logic.power
            * (len(self.bow_shooting_textures) - 1)
            // self.bow_logic.max_power
        )

        # Ensure frame index is within the range of available textures
        frame = max(0, min(frame, len(self.bow_shooting_textures) - 1))

        # Set the texture for the current frame
        self.texture = self.bow_shooting_textures[frame]

    def update(self):
        # Rotate the bow
        self.angle = self.bow_logic.get_angle()
