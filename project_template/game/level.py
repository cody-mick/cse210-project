import arcade
from solid_blocks import Solid_blocks
class Level:
    """Class in charge of creating levels"""

    def __init__(self, size, num_of_enemies, difficulty):

        self.num_of_enemies = num_of_enemies
        self.solid_blocks = Solid_blocks()
        self.wall_list = self.solid_blocks.wall_list

    def create_boundries(self):
        # Setup the boundries of the level
        



