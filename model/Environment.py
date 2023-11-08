class Environnement:
    """
    Class that represents the environment of the game. (NOT USED)

    Attributes:
        hit_box_lower (int): Lower bound of the hit box
        hit_box_upper (int): Upper bound of the hit box
        arrow_position_y (int): Position of the arrow on the y-axis
    """

    def __init__(self, hit_box_lower, hit_box_upper, arrow_position_y):
        self.hit_box_lower = hit_box_lower
        self.hit_box_upper = hit_box_upper
        self.arrow_position_y = arrow_position_y

    def is_hit(self, arrow_position_y):
        """Method to check if the arrow has hitted the target

        Args:
            arrow_position_y (int): Position of the arrow on the y-axis
        """
        if (
            arrow_position_y >= self.hit_box_lower
            and arrow_position_y <= self.hit_box_upper
        ):
            return True
        else:
            return False
