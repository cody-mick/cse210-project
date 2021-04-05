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
    

        # --- Load in a map from the tiled editor ---

        # Name of map file to load
        map_name = "assets/tmx_maps/map1.tmx"
        # Name of the layer in the file that has our platforms/walls
        platforms_layer_name = 'SolidBlocks'

        # Read in the tiled map
        my_map = arcade.tilemap.read_tmx(map_name)

        # -- Platforms
        self.wall_list = arcade.tilemap.process_layer(map_object=my_map,
                                                      layer_name=platforms_layer_name,
                                                      scaling=constants.TILE_SCALING,
                                                      use_spatial_hash=True)