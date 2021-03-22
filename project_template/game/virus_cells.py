import arcade
from arcade.sprite import Sprite
import constants
import random

class Virus_cells:
    """ 
    In charge of making COVID-19 Virus cells
    """
    def __init__(self):
        super().__init__
        self.virus_cells = None
        self.setup()

    def setup(self):
        # Set up the cells
        self.virus_cells = arcade.SpriteList()

        # for each row generate random blocks 
        for row in range(64, constants.SCREEN_HEIGHT - 64, 64):
            cell = arcade.Sprite("/Users/samuelcummings/Desktop/School/programming_with_classes/Projects/Final/cse210-project/project_template/game/assets/images/saw.png", constants.SPRITE_SCALING)
            cell.bottom = row
            cell.left = random.randrange(64, constants.SCREEN_WIDTH - 64, 64)
            # cell.velocity = (random.randint(-200, -50), 0) # x, y
            self.virus_cells.append(cell)

class FlyingSprite(arcade.Sprite):
    """Base class for all flying sprites
    Flying sprites include enemies and clouds
    """

    def update(self):
        """Update the position of the sprite
        When it moves off screen to the left, remove it
        """

        # Move the sprite
        super().update()



    
