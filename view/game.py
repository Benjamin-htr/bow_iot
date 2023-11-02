import arcade

BOW_SCALING = 1

UPDATES_PER_FRAME = 3

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Bow(arcade.Sprite):
    def __init__(self) : 
         # Set up parent class
        super().__init__()

        # Used for flipping between image sequences
        self.cur_texture = 0

        # Represent the power of the bow (0 to 100)
        self.bandage = 0

        self.scale = BOW_SCALING

        # Load texture for idle animation
        self.bow_idle = arcade.load_texture("assets/idle_bow.png")


        # Load texture for bandage animation
        self.bow_shooting_textures = arcade.load_spritesheet("assets/bandage_bow.png", 70, 90, 6, 24)
        print("oui")

    def update_animation(self, delta_time: float = 1 / 60):
        # bow Idle animation
        if self.bandage == 0 :
            self.texture = self.bow_idle
            self.cur_texture = 0
            return


        # bow bandage animation
        self.cur_texture += 1

        if self.cur_texture > 7 * UPDATES_PER_FRAME:
            self.cur_texture = 0

        frame = self.cur_texture // UPDATES_PER_FRAME

        self.texture = self.bow_shooting_textures[frame]



class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        # Sprite lists
        self.bow_list = None
        # Set up the bow
        self.bow = None
        self.score = 0

    def setup(self):
      self.bow_list = arcade.SpriteList()

      # Set up the bow
      self.bow = Bow()

      self.bow.center_x = SCREEN_WIDTH // 2
      self.bow.center_y = SCREEN_HEIGHT // 2

      self.bow_list.append(self.bow)


    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK_BEAN)
        return 

    def on_draw(self):
        self.clear()

         # Draw all the sprites.
        self.bow_list.draw()

         # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        #when the key is pressed, the bow is bandaged, it depends on the time the key is pressed
        if key == arcade.key.SPACE:
            self.bow.bandage += 1

    def on_key_release(self, key, modifiers):
        #when the key is released, the arrow is shot
        if key == arcade.key.SPACE:
            self.bow.bandage = 0
             

    def on_update(self, delta_time):
        # Move the player
        self.bow_list.update()

        # Update the players animation
        self.bow_list.update_animation()


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Archer challenge")
    window.total_score = 0
    game_view = GameView()
    game_view.setup()
    window.show_view(game_view)
    arcade.run()
    

if __name__ == "__main__":
    main()