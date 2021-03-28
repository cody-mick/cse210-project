import arcade
from arcade.sprite import Sprite
from arcade.sprite_list import SpriteList
import constants
import random
from PIL import Image

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

        # The width and height of the stones used to make the border
        stone_width = constants.stone_img_width 
        stone_height = constants.stone_img_height

        # -- Set up the boundary walls

        # bottom wall
        self.create_wall_list(constants.SCREEN_WIDTH, int(stone_width), 0)
        # top wall
        self.create_wall_list(constants.SCREEN_WIDTH, int(stone_width), constants.SCREEN_HEIGHT - stone_height)
        # left wall 
        self.create_wall_list(constants.SCREEN_HEIGHT, int(stone_height), 0)
        # right wall
        self.create_wall_list(constants.SCREEN_HEIGHT, int(stone_height), constants.SCREEN_WIDTH - stone_height)

        # -- Set up the solid walls 
        self.create_wall_list(constants.SCREEN_WIDTH, stone_width * 2, int(constants.SCREEN_HEIGHT - stone_height * 3))
        self.create_wall_list(constants.SCREEN_WIDTH, stone_width * 2, int(stone_height * 3))


    def create_wall_list(self, side, size, ref_point):
        """Method for creating wall lists needed to create boundary of the game

            parameters: 
                side: the side of the screen that the walls will be created on (either width(x) or height(y))
                size: the size of the image that we are using to create the borders (in this case- the size of the stone image)
                ref_point: specific point of some of the wall attributes
        """

        for i in range(0, side, size): 
            wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png", constants.SPRITE_SCALING)

            if side == constants.SCREEN_WIDTH:
                wall.left = i
                wall.bottom = ref_point

            elif side == constants.SCREEN_HEIGHT:
                wall.left = ref_point
                wall.bottom = i
            
            self.wall_list.append(wall)
            

        # # Create the bottom wall
        # for x in range(0, constants.SCREEN_WIDTH, 64): #We can change 64 by something like (img_width/2 * SCALING)
        #     wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png", constants.SPRITE_SCALING)
        #     wall.left = x
        #     wall.bottom = 0 
        #     self.wall_list.append(wall)

        # # Create the top wall
        # for x in range(0, constants.SCREEN_WIDTH, 64): #We can change 64 by something like (img_width/2 * SCALING)
        #     wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png", constants.SPRITE_SCALING)
        #     wall.left = x
        #     wall.top = constants.SCREEN_HEIGHT
        #     self.wall_list.append(wall)

        # # Create a left wall
        # for y in range(0, constants.SCREEN_HEIGHT, 64):
        #     wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png", constants.SPRITE_SCALING)
        #     wall.left = 0
        #     wall.bottom = y
        #     self.wall_list.append(wall)

        # # Create a right wall
        # for y in range(0, constants.SCREEN_HEIGHT, 64):
        #     wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png", constants.SPRITE_SCALING)
        #     wall.right = constants.SCREEN_WIDTH
        #     wall.bottom = y
        #     self.wall_list.append(wall)

        # #Create solid blocks
        # for x in range(128, constants.SCREEN_WIDTH-128, 128): 
        #     wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png", constants.SPRITE_SCALING)
        #     wall.left = x
        #     wall.bottom = 192 #Change this to a constant later haha
        #     self.wall_list.append(wall)

        # #Create solid blocks
        # for x in range(128, constants.SCREEN_WIDTH-128, 128): 
        #     wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png", constants.SPRITE_SCALING)
        #     wall.left = x
        #     wall.bottom = 384 #Change this to a constant later haha
        #     self.wall_list.append(wall)
