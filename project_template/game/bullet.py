import arcade
import math
import constants
from player import Player
import time

class Bullet(arcade.Sprite):
    "Class in charge of the bullets"
    def __init__(self, start_x, start_y, end_x, end_y):
        super().__init__()
        self.bullet_list = arcade.SpriteList()
        self.setup(start_x, start_y, end_x, end_y)

    def setup(self, start_x, start_y, end_x, end_y):
        ""
        bullet = arcade.Sprite("assets/images/laserBlue01.png", constants.BULLET_SCALING)
        bullet.sound = arcade.Sound("assets/sounds/laser2.wav")
        bullet.sound.play(volume= .04)

        bullet.center_x = start_x
        bullet.center_y = start_y
        
        dest_y = end_y
        dest_x = end_x

        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff) # retruns the arc tangent of a number (x) between -pi/2 and pi/2 (think back to pre-calculus)

        # Angle the bullet/laser
        bullet.angle = math.degrees(angle)

        bullet.change_x = math.cos(angle) * constants.BULLET_SPEED 
        bullet.change_y = math.sin(angle) * constants.BULLET_SPEED 
        self.bullet_list.append(bullet)

        
            
            
        
        