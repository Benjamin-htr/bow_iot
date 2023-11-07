import arcade

TEXT_SCALE = 0.4
SCORE_SCALE = 0.2


class TopBarGui:
    """Represents the gui top bar"""

    def __init__(
        self,
        padding: int,
        name: str,
        window_width: int,
        window_height: int,
    ):
        self.padding = padding
        self.name = name
        self.window_width = window_width
        self.window_height = window_height

        self.timer = 0
        self.score = 0

        # Load texture for background of the text
        self.background_text = arcade.load_texture("../assets/banner_name.png")

        # Load texture for the score indicator
        self.point_score_background = arcade.load_texture(
            "../assets/point_score_background.png"
        )

    def update(self, timer: float, score: int):
        """Updates the top bar"""
        self.timer = timer
        self.score = score

    def draw(self):
        """Draws the top bar"""
        # Name is on the top left corner
        name_position_x = self.padding + (self.background_text.width * TEXT_SCALE) // 2
        name_position_y = (
            self.window_height
            - self.padding
            - (self.background_text.height * TEXT_SCALE) // 2
        )
        self.draw_name(name_position_x, name_position_y)

        # Score is on the top right corner
        score_position_x = (
            self.window_width
            - self.padding * 3
            - (self.point_score_background.width * SCORE_SCALE) // 2
        )
        score_position_y = (
            self.window_height
            - self.padding
            - (self.point_score_background.height * SCORE_SCALE) // 2
        )
        self.draw_score(score_position_x, score_position_y)

        # Timer is on the top center
        timer_position_x = self.window_width // 2
        timer_position_y = (
            self.window_height
            - self.padding
            - (self.background_text.height * TEXT_SCALE) // 2
        )

        self.draw_timer(timer_position_x, timer_position_y)

    def draw_score(self, center_x, center_y):
        """Draws the score"""

        # Space between the score text and the icon
        space_between = 4

        # Draw the score icon
        arcade.draw_texture_rectangle(
            center_x,
            center_y,
            self.point_score_background.width * SCORE_SCALE,
            self.point_score_background.height * SCORE_SCALE,
            self.point_score_background,
        )

        # Draw the score text
        arcade.draw_text(
            f"{self.score}",
            center_x + self.point_score_background.width * SCORE_SCALE + space_between,
            center_y,
            arcade.color.BLACK,
            20,
            width=self.background_text.width * TEXT_SCALE,
            align="center",
            anchor_x="center",
            anchor_y="center",
        )

    def draw_name(self, center_x, center_y):
        """Draws the name"""
        arcade.draw_texture_rectangle(
            center_x,
            center_y,
            self.background_text.width * TEXT_SCALE,
            self.background_text.height * TEXT_SCALE,
            self.background_text,
        )

        arcade.draw_text(
            self.name,
            center_x,
            center_y,
            arcade.color.BLACK,
            20,
            width=self.background_text.width * TEXT_SCALE,
            align="center",
            anchor_x="center",
            anchor_y="center",
        )

    def draw_timer(self, center_x, center_y):
        """Draws the timer"""
        arcade.draw_texture_rectangle(
            center_x,
            center_y,
            self.background_text.width * TEXT_SCALE,
            self.background_text.height * TEXT_SCALE,
            self.background_text,
        )

        arcade.draw_text(
            f"{round(self.timer, 1)}",
            center_x,
            center_y,
            arcade.color.BLACK,
            20,
            width=self.background_text.width * TEXT_SCALE,
            align="center",
            anchor_x="center",
            anchor_y="center",
        )
