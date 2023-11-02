class GravitationalEffect:
    def __init__(self):
        self.gravity = -9.81  # Gravité en m/s^2
    
    def apply_gravity(self, time_delta, initial_velocity_y):
        # Mettre à jour la vitesse en fonction de la gravité
        final_velocity_y = initial_velocity_y - self.gravity * time_delta
        return final_velocity_y
