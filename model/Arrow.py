import math


class Arrow:
    """Class to represent the logic of an arrow"""

    def __init__(self, position: tuple):
        self.position = position  # La position est un tuple (x, y)
        self.velocity = (0, 0)  # La vitesse est aussi un tuple (vx, vy)
        self.gravity = -9.81  # m/s², direction négative vers le bas

    def set_initial_velocity(self, angle, power):
        """Method to set the initial velocity of the arrow

        Args:
            angle (int): Angle of the arrow in degrees
            power (int): Power of the arrow in N
        """
        # Convertir l'angle en radians
        angle_rad = math.radians(angle)
        # Calculer les composantes de la vitesse initiale
        self.velocity = (
            power / 1.3 * math.cos(angle_rad),  # vx
            power / 1.3 * math.sin(angle_rad),  # vy
        )

    def update_position_and_velocity(self, time_delta):
        """Method to update the position and velocity of the arrow

        Args:
            time_delta (float): Time step
        """
        # print(f"Position actuelle : {self.position}")
        # print(f"Vélocité actuelle : {self.velocity}")
        # Mettre à jour la position de la flèche
        self.position = (
            self.position[0] + self.velocity[0] * time_delta,
            self.position[1] + self.velocity[1] * time_delta,
        )
        # Mettre à jour la vitesse verticale
        self.velocity = (
            self.velocity[0],  # vx reste constante
            # vy est affectée par la gravité
            self.velocity[1] + self.gravity * time_delta,
        )

    def get_angle(self):
        """Method to get the angle of the arrow in degrees"""
        return math.degrees(
            math.atan(self.velocity[1] / self.velocity[0] if self.velocity[0] else 1)
        )

    def get_nb_next_positions(self, position_nb):
        """Method to get the next positions of the arrow

        Args:
            position_nb (int): Number of positions to get
        """
        positions = []
        position_initiale = self.position
        velocity_initiale = self.velocity
        for i in range(position_nb):
            self.update_position_and_velocity(0.3)
            positions.append(self.position)
        self.position = position_initiale
        self.velocity = velocity_initiale
        return positions

    def reset(self):
        """Method to reset the arrow"""
        self.position = (0, 20)
        self.velocity = (0, 0)
