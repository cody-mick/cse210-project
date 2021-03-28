import arcade
import constants

class Smoke(arcade.SpriteCircle):
    """This will represent a puff of smoke

    Based off of example given at https://arcade.academy/examples/sprite_explosion_particles.html
    """


    def __init__(self, size):
        super().__init__(size, arcade.color.SMOKY_BLACK, soft = True)
        self.change_y = constants.SMOKE_RISE_RATE
        self.scale = constants.SMOKE_START_SCALE

    def update(self):
        if self.alpha <= constants.PARTICLE_FADE_RATE:
            # Remove faded out particles
            self.remove_from_sprite_lists()
        else:
            # Update values
            self.alpha -= constants.SMOKE_FADE_RATE
            self.center_x += self.change_x
            self.center_y += self.change_y
            self.scale += constants.SMOKE_EXPANSION_RATE

