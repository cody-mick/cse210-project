import arcade 
import constants
import __main__


class Menu(arcade.View):
   """ Class that manages the 'menu' view. """

   def __init__(self):
      super().__init__()
      self.background = None

   def setup():
      self.background = arcade.load_texture("assets/images/Covidman_menu.jpg")

   def on_show(self):
      """ Called when switching to this view"""
      
      arcade.set_background_color(arcade.color.WHITE)

   def on_draw(self):
      """ Draw the menu """
      arcade.start_render()
      arcade.draw_text("Menu Screen - click to advance", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2,
                        arcade.color.BLUE, font_size=30, anchor_x="center")
      #arcade.load_texture("project_template/game/assets/images/Covidman_menu.jpg")

      arcade.draw_lrwh_rectangle_textured(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, self.background)

   def on_mouse_press(self, _x, _y, _button, _modifiers):
      """ Use a mouse press to advance to the 'game' view. """
      game_view = __main__.MyGame()
      game_view.setup()
      self.window.show_view(game_view)
