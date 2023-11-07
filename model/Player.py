from utils.serializable import Serializable


class Player:
    def __init__(self, rfid_tag, name,score = 0):
        self.rfid_tag = rfid_tag
        self.name = name
        self.score = score

    def update_score(self, points):
        self.score += points
        


