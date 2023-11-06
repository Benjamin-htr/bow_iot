import json
# Ajout pour le plot
import math
from time import sleep

import arcade

from model.Arrow import Arrow
from model.Logic import Logic
from model.Player import Player
from model.Target import Target
from view.game import GameView, test_game
from view.menu import MainMenuView

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 619

# Constantes pour le plot
GRAVITY = -9.81  # Accélération due à la gravité (m/s^2)
TIME_STEP = 0.1  # Pas de temps pour la simulation (s)


class Main:
    def __init__(self):
        self.player = Player("Player1", "RFID1234")  # Exemple de joueur
        self.arrow = Arrow()
        self.target = Target((90, 0), (2, 2))  # Exemple de cible
        self.running = True
        self.MAX_HEIGHT = 100
        self.MAX_WIDTH = 100
        print("Initialisation du jeu...")
        print(f"Joueur actuel : {self.player.name}")
        print(f"Score actuel : {self.player.score}")
        print(f"Cible : {self.target.position} - {self.target.size}")
        print("Initialisation terminée.")

    # ... (Les autres méthodes restent inchangées) ...

    # Ajout de la méthode plot_trajectory pour l'affichage
    def plot_trajectory(self):
        # Calculer la trajectoire en fonction de la position et de la vélocité de la flèche

        # Créer le graphique ASCII
        for y in range(self.MAX_HEIGHT, -1, -1):
            row = ''
            for x in range(self.MAX_WIDTH + 1):
                char = ' '
                if int(round(self.arrow.position[0])) == x and int(round(self.arrow.position[1])) == y:
                    char = '*'
                if int(round(self.target.position[0])) == x and int(round(self.target.position[1])) == y:
                    char = 'X'  # Marquer la cible
                row += char
            print(row)

    def get_user_input(self):
        # Simuler la saisie de l'angle et de la puissance (vitesse initiale)
        angle = float(input("Entrez l'angle de tir (en degrés) : "))
        power = float(input("Entrez la puissance de tir (0-100) : "))
        return angle, power

    def main_loop(self):
        while self.running:
            print("Nouveau tir !")
            angle, power = self.get_user_input()

            # Configurer la flèche
            self.arrow.set_initial_velocity(angle, power)

            # Afficher la vélocité et l'angle
            print(f"Angle de tir: {angle} degrés")
            print(f"Vélocité initiale: {self.arrow.velocity} m/s")

            # Simuler le tir et afficher la trajectoire
            # Vérifier si la cible est touchée
            # hit = self.simulate_shot()
            while self.arrow.position[1] > 0:
                self.arrow.update_position_and_velocity(1)
                self.plot_trajectory()
                #print(self.arrow.get_angle())
                sleep(TIME_STEP)

            # Afficher le résultat
            if True:
                print("Touché !")
                # Ajouter des points pour un tir réussi
                self.player.update_score(10)
            else:
                print("Manqué...")

            print(f"Score actuel : {self.player.score}")

            # Option pour quitter
            if input("Tirer à nouveau ? (y/n) : ") != 'y':
                self.running = False

    # ... (Les autres méthodes restent inchangées) ...


# Exemple d'exécution
# if __name__ == "__main__":
#     game = Main()
#     try:
#         game.main_loop()
#     except KeyboardInterrupt:
#         print("\nArrêt du jeu...")
#     finally:
#         # game.save_game_state()
#         print("État du jeu sauvegardé.")

def LaunchApp() : 
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Archer challenge")
    window.logic = Logic()
    menu_view = MainMenuView()
    window.show_view(menu_view)
    arcade.run()

if __name__ == "__main__":
    LaunchApp()
