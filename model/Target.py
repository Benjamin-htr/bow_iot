class Target:
    def __init__(self, arrow_position_y):
        self.y = 50
        self.direction = 1
        self.hit_box_lower = 30
        self.hit_box_upper = 70
        self.arrow_position_y = arrow_position_y

    def move(self):
        self.y += self.direction
        if self.y == 100 or self.y == 0:
            self.direction *= -1
        self.hit_box_lower = (
            self.y - 20
        )  # evolution de la hit box en fonction de la position de la cible
        self.hit_box_upper = self.y + 20

    def get_score(self):
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
        return self.hit_box_lower

    def hit_box(self):
        return self.hit_box_lower, self.hit_box_upper

    def is_hit(self, arrow_position_y):
        if (
            arrow_position_y >= self.hit_box_lower
            and arrow_position_y <= self.hit_box_upper
        ):
            self.get_score()
            return True

        else:
            return False
        pass
