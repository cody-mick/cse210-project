"""
Sprite Move With Walls
Simple program to show basic sprite usage.
Artwork from http://kenney.nl
If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_walls
"""
from arcade.sprite import Sprite
from arcade.sprite_list import SpriteList
import arcade
import os
import constants 
from destroyable_blocks import Destroyable_blocks
from virus_cells import Virus_cells

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.destroyable_blocks = Destroyable_blocks()
        self.virus_cells = Virus_cells()

        # Sprite lists
        self.coin_list = None
        self.wall_list = None
        self.player_list = None
        self.random_wall_list = self.destroyable_blocks.random_wall_list 
        self.enemies = self.virus_cells.virus_cells
        self.all_obstacles = None
        
        self.player_sprite = None
        self.physics_engine = None

        self.background = None

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.all_obstacles = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png",
                                           constants.SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)

        # -- Set up the walls
        # Create the bottom wall
        for x in range(0, constants.SCREEN_WIDTH, 64): #We can change 64 by something like (img_width/2 * SCALING)
            wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png", constants.SPRITE_SCALING)
            wall.left = x
            wall.bottom = 0 
            self.wall_list.append(wall)

        # Create the top wall
        for x in range(0, constants.SCREEN_WIDTH, 64): #We can change 64 by something like (img_width/2 * SCALING)
            wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png", constants.SPRITE_SCALING)
            wall.left = x
            wall.top = constants.SCREEN_HEIGHT
            self.wall_list.append(wall)

        # Create a left wall
        for y in range(0, constants.SCREEN_HEIGHT, 64):
            wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png", constants.SPRITE_SCALING)
            wall.left = 0
            wall.bottom = y
            self.wall_list.append(wall)

        # Create a right wall
        for y in range(0, constants.SCREEN_HEIGHT, 64):
            wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png", constants.SPRITE_SCALING)
            wall.right = constants.SCREEN_WIDTH
            wall.bottom = y
            self.wall_list.append(wall)

        #Create solid blocks
        for x in range(128, constants.SCREEN_WIDTH-128, 128): 
            wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png", constants.SPRITE_SCALING)
            wall.left = x
            wall.bottom = 192 #Change this to a constant later haha
            self.wall_list.append(wall)

        #Create solid blocks
        for x in range(128, constants.SCREEN_WIDTH-128, 128): 
            wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png", constants.SPRITE_SCALING)
            wall.left = x
            wall.bottom = 384 #Change this to a constant later haha
            self.wall_list.append(wall)

        # Add all of the obstacles 
        self.all_obstacles.extend(self.wall_list)
        self.all_obstacles.extend(self.random_wall_list)
        self.all_obstacles.extend(self.enemies)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.all_obstacles)  

        # Set the background color
        self.background = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, self.background)

        # Draw all the sprites.
     
        self.all_obstacles.draw()
        self.player_list.draw()
 


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = constants.MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -constants.MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -constants.MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = constants.MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()


def main():
    """ Main method """
    window = MyGame(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main() 