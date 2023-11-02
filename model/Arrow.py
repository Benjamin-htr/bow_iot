import math


class Arrow:
    def __init__(self):
        self.position = (0, 10)  # La position est un tuple (x, y)
        self.velocity = (0, 0)  # La vitesse est aussi un tuple (vx, vy)
        self.gravity = -9.81  # m/s², direction négative vers le bas

    def set_initial_velocity(self, angle, power):
        # Convertir l'angle en radians
        angle_rad = math.radians(angle)
        # Calculer les composantes de la vitesse initiale
        self.velocity = (
            power * math.cos(angle_rad),  # vx
            power * math.sin(angle_rad)   # vy
        )

    def update_position_and_velocity(self, time_delta):
        # print(f"Position actuelle : {self.position}")
        # print(f"Vélocité actuelle : {self.velocity}")
        # Mettre à jour la position de la flèche
        self.position = (
            self.position[0] + self.velocity[0] *
            time_delta,  # Mise à jour de x
            self.position[1] + self.velocity[1] * \
            time_delta   # Mise à jour de y
        )
        # Mettre à jour la vitesse verticale
        self.velocity = (
            self.velocity[0],  # vx reste constante
            # vy est affectée par la gravité
            self.velocity[1] + self.gravity * time_delta
        )

        # Si la flèche atteint le sol (y <= 0), on arrête la simulation
        if self.position[1] <= 0:
            self.position = (self.position[0], 0)
            self.velocity = (0, 0)

    def get_angle(self):
        return math.degrees(math.atan(self.velocity[1]/self.velocity[0]))
