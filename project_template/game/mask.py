import arcade
from arcade.sprite import Sprite
from arcade.sprite_list import SpriteList
import constants
import random


class Mask(arcade.Sprite):
    """ 
    In charge of making destroyable blocks
    """
    def __init__(self):
        super().__init__
        self.mask_list = None
        self.setup()

    def setup(self):
        # # Set up the blocks
        self.mask_list = arcade.SpriteList()
        self.mask_count = 0

        # --- Load in a map from the tiled editor ---

        # Name of map file to load
        map_name = "assets/tmx_maps/map1.tmx"
        # Name of the layer in the file that has our platforms/walls
        mask_layer_name = 'Masks'

        # Read in the tiled map
        my_map = arcade.tilemap.read_tmx(map_name)

        # -- Platforms
        self.mask_list = arcade.tilemap.process_layer(map_object=my_map,
                                                      layer_name=mask_layer_name,
                                                      scaling=constants.TILE_SCALING,
                                                      use_spatial_hash=True)

        for i in self.mask_list:
            i.health = random.randrange(3,5)
            self.mask_count += 1

    def generate_powers(self):
        # This method is in charge of deciding which power ability the player will be able to use once it collects a mask
        powers = ["machine_gun", "extra_health"]
        return powers[random.randint(0,2)]
            
            