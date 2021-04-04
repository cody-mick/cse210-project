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
        # # Set up the blocks
        self.random_wall_list = arcade.SpriteList()

        # # for each row generate random blocks 
        # virus_left_position = [192, 320, 448, 576]
        # virus_bottom_position = [128, 256, 320, 448]

        # for i in range(0, 30):
        #     block = arcade.Sprite("assets/images/brickTextureWhite.png", constants.SPRITE_SCALING)
        #     block.bottom = random.randrange(64, constants.SCREEN_HEIGHT - 64, 64)
        #     block.left = random.randrange(128, constants.SCREEN_WIDTH - 128, 64)
        #     block.health = random.randrange(3,5)
        #     if (block.left not in virus_left_position) or (block.bottom not in virus_bottom_position):
        #         self.random_wall_list.append(block)

                # --- Load in a map from the tiled editor ---

        # Name of map file to load
        map_name = ":resources:tmx_maps/map.tmx"
        # Name of the layer in the file that has our platforms/walls
        destroyable_layer_name = 'DestroyableBlocks'

        # Read in the tiled map
        my_map = arcade.tilemap.read_tmx(map_name)

        # -- Platforms
        self.random_wall_list = arcade.tilemap.process_layer(map_object=my_map,
                                                      layer_name=destroyable_layer_name,
                                                      scaling=constants.TILE_SCALING,
                                                      use_spatial_hash=True)

        for i in self.random_wall_list:
            i.health = random.randrange(3,5)

            


