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

        # --- Load in a map from the tiled editor ---

        # Name of map file to load
        map_name = "assets/tmx_maps/map1.tmx"
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

            


