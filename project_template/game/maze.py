from arcade.sprite import Sprite
from arcade.sprite_list import SpriteList
import arcade
import os
import constants 
from destroyable_blocks import Destroyable_blocks
from virus_cells import Virus_cells
import math

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.destroyable_blocks = Destroyable_blocks()
        self.virus_cells = Virus_cells()

        # Sprite lists
        self.coin_list = None
        self.wall_list = None
        self.player_list = None
        self.brick_list = self.destroyable_blocks.random_wall_list
        self.enemies = self.virus_cells.virus_cells
        self.all_obstacles = None
        self.destroyable_objects = None
        self.bullet_list = None
        
        self.player_sprite = None
        self.physics_engine = None

        self.background = None

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.all_obstacles = arcade.SpriteList()
        self.destroyable_objects = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        for enemy in self.enemies:
            enemy.physics_engine = arcade.PhysicsEngineSimple(enemy, self.brick_list) 

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png",
                                           constants.SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)

        # -- Set up the walls
        # Create the bottom wall
        for x in range(0, constants.SCREEN_WIDTH, 64): #We can change 64 by something like (img_width/2 * SCALING)
            wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png", constants.SPRITE_SCALING)
            wall.left = x
            wall.bottom = 0 
            self.wall_list.append(wall)

        # Create the top wall
        for x in range(0, constants.SCREEN_WIDTH, 64): #We can change 64 by something like (img_width/2 * SCALING)
            wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png", constants.SPRITE_SCALING)
            wall.left = x
            wall.top = constants.SCREEN_HEIGHT
            self.wall_list.append(wall)

        # Create a left wall
        for y in range(0, constants.SCREEN_HEIGHT, 64):
            wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png", constants.SPRITE_SCALING)
            wall.left = 0
            wall.bottom = y
            self.wall_list.append(wall)

        # Create a right wall
        for y in range(0, constants.SCREEN_HEIGHT, 64):
            wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png", constants.SPRITE_SCALING)
            wall.right = constants.SCREEN_WIDTH
            wall.bottom = y
            self.wall_list.append(wall)

        #Create solid blocks
        for x in range(128, constants.SCREEN_WIDTH-128, 128): 
            wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png", constants.SPRITE_SCALING)
            wall.left = x
            wall.bottom = 192 #Change this to a constant later haha
            self.wall_list.append(wall)

        #Create solid blocks
        for x in range(128, constants.SCREEN_WIDTH-128, 128): 
            wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png", constants.SPRITE_SCALING)
            wall.left = x
            wall.bottom = 384 #Change this to a constant later haha
            self.wall_list.append(wall)

        # Add all of the obstacles 
        self.all_obstacles.extend(self.wall_list)
        self.all_obstacles.extend(self.brick_list)
        self.all_obstacles.extend(self.enemies)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.all_obstacles)  

        # Combine destroyable materials together - don't know where to put this 
        self.destroyable_objects.extend(self.brick_list)
        self.destroyable_objects.extend(self.enemies)

        # Set the background color
        self.background = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, self.background)

        # Draw all the sprites.
     
        self.enemies.draw()
        self.brick_list.draw()
        self.wall_list.draw()
        self.player_list.draw()
        self.bullet_list.draw()
 


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = constants.MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -constants.MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -constants.MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = constants.MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        "Called when the user presses the mouse"

        # Create a bullet/lazer 
        bullet = arcade.Sprite("assets/images/laserRed01 copy.png", constants.BULLET_SCALING)
        # Position the bullet at the players location
        start_x = self.player_sprite.center_x
        start_y = self.player_sprite.center_y
        bullet.center_x = start_x
        bullet.center_y = start_y

        # get from the mouse the destination location (x and y)
        dest_x = x
        dest_y = y

        # get the bullet to the destination
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff) # retruns the arc tangent of a number (x) between -pi/2 and pi/2 (think back to pre-calculus)

        # Angle the bullet/laser
        bullet.angle = math.degrees(angle)

        # Now with the angle, calculate our change_x and change_y 
        bullet.change_x = math.cos(angle) * constants.BULLET_SPEED 
        bullet.change_y = math.sin(angle) * constants.BULLET_SPEED 

        # Add bullet to list 
        self.bullet_list.append(bullet)


    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        self.bullet_list.update()
        for bullet in self.bullet_list:

            # Check to see if the bullet hit any destroyable blocks
            has_hit_list = arcade.check_for_collision_with_list(bullet, self.destroyable_objects)

            # if so, get rid of the bullet
            if len(has_hit_list) > 0:
                bullet.remove_from_sprite_lists()
            
            for block in has_hit_list:
                block.remove_from_sprite_lists()
                
            # if bullet is off screen, remove it.
            if bullet.bottom > self.width or bullet.top < 0 or bullet.right < 0 or bullet.left > self.width:
                bullet.remove_from_sprite_lists()

        for enemy in self.enemies:
            # updates each enemy
            enemy.physics_engine.update()






def main():
    """ Main method """
    window = MyGame(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main() 