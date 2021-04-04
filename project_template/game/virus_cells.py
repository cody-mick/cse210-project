import arcade
from arcade.sprite import Sprite
from arcade.sprite_list import SpriteList
import constants
import random
from  destroyable_blocks import Destroyable_blocks
import math
from solid_blocks import Solid_blocks
class Virus_cells(arcade.Sprite):
    """ 
    In charge of making COVID-19 Virus cells
    """
    def __init__(self):
        super().__init__()
        self.virus_cells = None
        self.setup()

    def setup(self):
        # Set up the cells
        self.virus_cells = arcade.SpriteList()

        # --- Load in a map from the tiled editor ---

        # Name of map file to load
        map_name = "assets/tmx_maps/map1.tmx"
        # Name of the layer in the file that has our enemies
        enemies_layer_name = 'Enemies'

        # Read in the tiled map
        my_map = arcade.tilemap.read_tmx(map_name)

        # -- Platforms
        self.virus_cells = arcade.tilemap.process_layer(map_object=my_map,
                                                      layer_name=enemies_layer_name,
                                                      scaling=constants.TILE_SCALING,
                                                      use_spatial_hash=True)

        for cell in self.virus_cells:
            cell.health = 4
            cell.color = (0, 204, 0) # Green


    
