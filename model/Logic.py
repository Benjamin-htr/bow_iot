import json

from model.Arrow import Arrow
from model.Bow import Bow
from model.Player import Player
from model.Timer import Timer


class Logic:
    """Class to represent the main logic of the game"""

    def __init__(self):
        self.player = Player("12345", "Player1")
        self.bow = Bow(0)
        self.arrows = []
        self.timer = Timer()

    def launch_arrow(self):
        """Method to add an arrow to the logic

        Args:
            position (tuple): Position of the arrow
        """
        new_arrow = Arrow((0, 0))
        print("launch arrow : ", self.bow.angle, self.bow.power)
        new_arrow.set_initial_velocity(self.bow.angle, self.bow.power)
        self.arrows.append(new_arrow)

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
            print(id)
            result = False
            for obj in data:
                print("uuid ", obj["uuid"])
                if obj["uuid"] == id:
                    self.player = Player(obj["uuid"], obj["name"], obj["score"])
                    result = True
                    return result
                else:
                    self.player.rfid_tag = id
            return result

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

    def start_game(self):
        """Method to start the game"""
        self.timer = Timer()
        self.arrows = []
        self.player.score = 0

    def stop_game(self):
        """Method to stop the game"""
        self.timer.stop()
        self.save_player()
