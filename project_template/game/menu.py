import arcade 
import constants
from __main__ import MyGame


class Menu(arcade.View):
     """ Class that manages the 'menu' view. """


     def on_show(self):
        """ Called when switching to this view"""
        # arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")
        arcade.set_background_color(arcade.color.WHITE)

     def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        arcade.draw_text("Menu Screen - click to advance", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2,
                         arcade.color.BLUE, font_size=30, anchor_x="center")

     def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ Use a mouse press to advance to the 'game' view. """
        game_view = MyGame()
        game_view.setup()
        self.window.show_view(game_view)