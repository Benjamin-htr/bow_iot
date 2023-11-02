class Environnement:
  def __init__(self, target_position):
    self.target_position = target_position
    self.arrow_position = arrow_position
  def is_hit(self, arrow_position):
    if arrow_position == self.target_position:
      return True
    else:
      return False
