class Target:
  def __init__(self):
    self.x = 0
    self.y = 50
    self.direction = 1
  
  def move(self):
    self.x += self.direction
    if self.x == 100 or self.x == 0:
      self.direction *= -1
  
  def get_score(self, arrow_x, arrow_y):
    #formule de calcul de la distance entre deux points dans un environnement 2D avec Euclidean
    distance = ((arrow_x - self.x) ** 2 + (arrow_y - self.y) ** 2) ** 0.5
    #exemple de score
    if distance <= 10:
      return 3
    elif distance <= 20:
      return 2
    elif distance <= 30:
      return 1
    else:
      return 0
  
  def target_position_y(self):
    return (self.y)
