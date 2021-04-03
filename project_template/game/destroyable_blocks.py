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
        virus_left_position = [192, 320, 448, 576]
        virus_bottom_position = [128, 256, 320, 448]

        for i in range(0, 30):
            block = arcade.Sprite("assets/images/brickTextureWhite.png", constants.SPRITE_SCALING)
            block.bottom = random.randrange(64, constants.SCREEN_HEIGHT - 64, 64)
            block.left = random.randrange(128, constants.SCREEN_WIDTH - 128, 64)
            block.health = random.randrange(3,5)
            if (block.left not in virus_left_position) or (block.bottom not in virus_bottom_position) or (block.center_x != 100) or (block.center_y != 80):
                self.random_wall_list.append(block)
    
    def update(self):
        self.append_texture("assets/images/mask.png")
            


