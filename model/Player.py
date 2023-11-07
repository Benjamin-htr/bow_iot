from utils.serializable import Serializable


class Player:
    """Class to represent a player"""

    def __init__(self, rfid_tag, name, score=0):
        self.rfid_tag = rfid_tag
        self.name = name
        self.score = score

    def update_score(self, points):
        """Method to update the score of the player

        Args:
            points (int): Points to add to the score
        """
        self.score += points
