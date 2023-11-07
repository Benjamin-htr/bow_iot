import json

from model.Arrow import Arrow
from model.Player import Player
from model.Timer import Timer


class Logic:
    """Class to represent the main logic of the game"""

    def __init__(self):
        self.player = Player("Player1", "RFID1234")
        self.arrows = []
        self.timer = Timer()

    def add_arrow(self, position):
        """Method to add an arrow to the logic

        Args:
            position (tuple): Position of the arrow
        """
        self.arrows.append(Arrow(position))
        return len(self.arrows) - 1

    def update_arrow(self, id, step):
        """Method to update the position and velocity of an arrow

        Args:
            id (int): ID of the arrow
            step (float): Time step
        """
        self.arrows[id].update_position_and_velocity(step)

    def get_arrow(self, id):
        """Method to get an arrow

        Args:
            id (int): ID of the arrow
        """
        return self.arrows[id]

    def rm_arrow(self, id):
        """Method to remove an arrow

        Args:
            id (int): ID of the arrow
        """
        self.arrows[id] = None

    def get_arrows(self):
        """Method to get all the arrows"""
        return self.arrows

    def hitted(self):
        """Method to check if an arrow has hitted the target"""
        self.player.score += 1

    def set_player(self, id):
        """Method to set the player

        Args:
            id (int): ID of the player
        """
        with open("../score.json", "r") as json_file:
            data = json.load(json_file)
            for obj in data:
                if obj["uuid"] == id:
                    self.player = Player(obj["name"], obj["uuid"], obj["score"])
                else:
                    return "non"

    def set_player_with_info(self, id, name, score):
        """Method to set the player with info

        Args:
            id (int): ID of the player
            name (string): Name of the player
            score (int): Score of the player
        """
        self.player = Player(id, name, score)

    def save_player(self):
        """Method to save the player"""

        new_user = {
            "uuid": self.player.rfid_tag,
            "name": self.player.name,
            "score": self.player.score,
        }
        with open("../score.json", "r") as json_file:
            data = json.load(json_file)
            data.append(new_user)

        with open("../score.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
