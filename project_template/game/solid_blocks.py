import arcade
from arcade.sprite import Sprite
from arcade.sprite_list import SpriteList
import constants
import random

class Solid_blocks(arcade.Sprite):
    """ 
    In charge of making solid blocks
    """

    def __init__(self):
        super().__init__
        self.wall_list = None
        self.setup()

    def setup(self):
        self.wall_list = arcade.SpriteList()


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