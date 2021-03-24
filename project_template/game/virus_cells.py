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
        

        # Horizontal enemies
        # for each iteration create an enemy 
        virus_bottom_position = [128, 256, 320, 448]
        for i in range(4): # 3 enemies in this case
            cell = arcade.Sprite("assets/images/saw.png", constants.SPRITE_SCALING)
            cell.bottom = virus_bottom_position[i]
            cell.left = constants.SCREEN_WIDTH - 128
            cell.change_x = random.randrange(-1,-3,-1)
            cell.change_y = 0
            self.virus_cells.append(cell)

        # Vertical enemies
        # for each iteration create an enemy 
        virus_left_position = [192, 320, 448, 576]
        for i in range(4): # 3 enemies in this case
            cell = arcade.Sprite("assets/images/saw.png", constants.SPRITE_SCALING)
            cell.bottom = constants.SCREEN_HEIGHT - 128
            cell.left = virus_left_position[i]
            cell.change_x = 0 # x, y
            cell.change_y = random.randrange(-1,-3,-1)
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



    
