from view.game_parts.BowSprite import BowSprite


class Bow:
    def __init__(self, angle, max_power=100, speed_power=1):
        self.angle = angle
        self.change_angle = 0
        self.power = 0
        self.max_power = max_power
        self.speed_power = speed_power
        self.is_charging = False
        self.sprite: BowSprite = None

    def load_sprite(self, sprite: BowSprite):
        self.sprite = sprite

    def set_angle(self, angle):
        self.angle = angle

    def add_angle(self, angle):
        self.angle += angle

    def turn_left(self, change_angle=5):
        self.change_angle = change_angle

    def turn_right(self, change_angle=5):
        self.change_angle = -change_angle

    def stop_turn(self):
        self.change_angle = 0
        self.sprite.change_angle = 0

    def update(self):
        if self.is_charging:
            self.power += self.speed_power
            if self.power > self.max_power:
                self.power = 0
        if self.change_angle != 0:
            self.angle += self.change_angle

    def get_angle(self):
        return self.angle

    def bandage(self):
        self.is_charging = True

    def stop_bandage(self):
        self.is_charging = False
        self.power = 0
