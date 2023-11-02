class Environnement:
  def __init__(self, target_position_y, arrow_poistion_y):
    self.target_position_y = target_position_y
    self.arrow_position_y = arrow_position_y
  def is_hit(self, arrow_position):
    if arrow_position_y == self.target_position_y:
      return True
    else:
      return False
htestts