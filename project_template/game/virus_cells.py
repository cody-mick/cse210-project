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

        virus_left_position = [192, 320, 448, 576]
        solid_blocks_position = []
        for sprite in Solid_blocks().wall_list:
            solid_blocks_position.append(sprite.center_x)
            
        for i in range(4):
            # Create the coin instance
            # Coin image from kenney.nl
            cell = arcade.Sprite("assets/images/saw.png", constants.SPRITE_SCALING)

            # Position the coin
            cell.bottom = constants.SCREEN_HEIGHT - 128
            cell.left = virus_left_position[i]
            cell.health = 4
            cell.color = (0, 204, 0) # Green

            # Add the coin to the lists
            
            if cell.position not in solid_blocks_position:
                self.virus_cells.append(cell)
        
        virus_bottom_position = [128, 256, 320, 448]
        for i in range(4):
            # Create the coin instance
            # Coin image from kenney.nl
            cell = arcade.Sprite("assets/images/saw.png", constants.SPRITE_SCALING)

            # Position the coin
            cell.center_y = virus_bottom_position[i]
            cell.center_x = constants.SCREEN_WIDTH - 128
            cell.health = 4
            cell.color = (0, 204, 0) # Green

            # Add the coin to the lists
            if cell.position not in solid_blocks_position:
                self.virus_cells.append(cell)






    


# class FlyingSprite(arcade.Sprite):
#     """Base class for all flying sprites
#     Flying sprites include enemies and clouds
#     """

#     def update(self):
#         """Update the position of the sprite
#         When it moves off screen to the left, remove it
#         """

#         # Move the sprite
#         super().update()



    
