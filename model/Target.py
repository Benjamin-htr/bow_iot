class Target:
    """Class to represent the logic of a target (NOT USED)

    Attributes:
        y (int): Position of the target on the y-axis
        direction (int): Direction of the target
        hit_box_lower (int): Lower bound of the hit box
        hit_box_upper (int): Upper bound of the hit box
        arrow_position_y (int): Position of the arrow on the y-axis
    """

    def __init__(self, arrow_position_y):
        self.y = 50
        self.direction = 1
        self.hit_box_lower = 30
        self.hit_box_upper = 70
        self.arrow_position_y = arrow_position_y

    def move(self):
        """Method to move the target"""
        self.y += self.direction
        if self.y == 100 or self.y == 0:
            self.direction *= -1
        self.hit_box_lower = (
            self.y - 20
        )  # evolution de la hit box en fonction de la position de la cible
        self.hit_box_upper = self.y + 20

    def get_score(self):
        """Method to get the score of the player"""
        # calule la distance entre la cible et la fleche en utilisant la fonction eclidian
        distance = self.y - self.arrow_position_y
        # calcule le score en fonction de la distance
        if distance <= 10:
            return 3
        elif distance <= 20:
            return 2
        elif distance <= 30:
            return 1
        else:
            return 0

    def target_position_y(self):
        """Method to get the position of the target on the y-axis"""
        return self.hit_box_lower

    def hit_box(self):
        """Method to get the hit box of the target"""
        return self.hit_box_lower, self.hit_box_upper

    def is_hit(self, arrow_position_y):
        """Method to check if the arrow has hitted the target"""
        if (
            arrow_position_y >= self.hit_box_lower
            and arrow_position_y <= self.hit_box_upper
        ):
            self.get_score()
            return True

        else:
            return False
        pass
