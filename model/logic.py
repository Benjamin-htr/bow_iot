from model.Arrow import Arrow
from model.Player import Player
import json

class Logic():

    def __init__(self):
        self.player = Player("Player1", "RFID1234")
        self.arrows = []

    def add_arrow(self, position):
        self.arrows.append(Arrow(position))
        return len(self.arrows)-1

    def update_arrow(self, id, step):
        self.arrows[id].update_position_and_velocity(step)

    def get_arrow(self, id):
        return self.arrows[id]

    def rm_arrow(self, id):
        self.arrows[id] = None

    def get_arrows(self):
        return self.arrows

    def hitted(self, id):
        self.player.score = self.player.score + 1
        self.player.score += 1

    def set_player(self, id):
        with open("../score.json", "r") as json_file:
            data = json.load(json_file)
            for obj in data:
                if obj["uuid"] == id:
                    self.player = Player(obj["name"],obj["uuid"],obj["score"])
                else:
                    return "non"

    def set_player_with_info(self, id,name,score):
        self.player = Player(id,name,score)

    def save_player(self):
        new_user = {
            "uuid": self.player.rfid_tag,
            "name": self.player.name,
            "score": self.player.score
        }
        with open("../score.json", "r") as json_file:
            data = json.load(json_file)
            data.append(new_user)

        with open("../score.json", "w") as json_file:
            json.dump(data,json_file,indent=4)

