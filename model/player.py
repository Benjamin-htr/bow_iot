from utils.serializable import Serializable


class Player:
    def __init__(self, rfid_tag, name):
        self.rfid_tag = rfid_tag
        self.name = name
        self.score = 0

    def update_score(self, points):
        self.score += points
        


