import arcade


class PowerIndicator() : 
  def __init__(self, center_x, center_y, width, height, border_width) :
    self.center_x = center_x
    self.center_y = center_y
    self.width = width
    self.height = height
    self.border_width = border_width
    self.power = 0

  def update(self, power) :
    self.power = power 


  def draw(self) :
    arcade.draw_rectangle_outline(self.center_x, self.center_y, self.width + self.border_width/2  , self.height+self.border_width/2, arcade.color.BLACK, self.border_width)
    arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, arcade.color.WHITE)
    arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.power, arcade.color.RED)