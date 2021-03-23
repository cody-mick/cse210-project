import arcade
from arcade.sprite import Sprite
from arcade.sprite_list import SpriteList
import constants
import random
from  destroyable_blocks import Destroyable_blocks

class Virus_cells(arcade.Sprite):
    """ 
    In charge of making COVID-19 Virus cells
    """
    def __init__(self):
        super().__init__
        self.virus_cells = None
        # self.maze = MyGame(arcade.Window)
        # self.walls = self.maze.wall_list
        self.setup()

    def setup(self):
        # Set up the cells
        self.virus_cells = arcade.SpriteList()

        # for each iteration create an enemy 
        for i in range(3): # 3 enemies in this case
            cell = arcade.Sprite("assets/images/saw.png", constants.SPRITE_SCALING)
            cell.bottom = random.randrange(64, constants.SCREEN_HEIGHT - 64, 64)
            cell.left = random.randrange(64, constants.SCREEN_WIDTH - 64, 64)
            cell.velocity = (-2, 0) # x, y
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



    
