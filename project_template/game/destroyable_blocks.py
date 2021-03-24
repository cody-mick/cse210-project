import arcade
from arcade.sprite import Sprite
from arcade.sprite_list import SpriteList
import constants
import random


class Destroyable_blocks(arcade.Sprite):
    """ 
    In charge of making destroyable blocks
    """
    def __init__(self):
        super().__init__
        self.random_wall_list = None
        self.setup()

    def setup(self):
        # Set up the blocks
        self.random_wall_list = arcade.SpriteList()

        # for each row generate random blocks 
        for row in range(128, constants.SCREEN_HEIGHT - 64, 64):
            block = arcade.Sprite("assets/images/brickTextureWhite.png", constants.SPRITE_SCALING)
            block.bottom = row
            block.left = random.randrange(128, constants.SCREEN_WIDTH - 128, 64)
            self.random_wall_list.append(block)



