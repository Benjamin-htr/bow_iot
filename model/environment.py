class Environnement:
  def __init__(self, hit_box_lower, hit_box_upper,arrow_poistion_y):
    self.hit_box_lower = hit_box_lower
    self.hit_box_upper = hit_box_upper
    self.arrow_position_y = arrow_position_y
    
  def is_hit(self, arrow_position):
    if arrow_position_y >= self.hit_box_lower and arrow_position_y <= self.hit_box_upper:
      return True
    else:
      return False