from arcade.application import Window
from arcade.particle import Particle
from arcade.sprite import Sprite
from arcade.sprite_list import SpriteList
import arcade
import os
import constants 
from destroyable_blocks import Destroyable_blocks
from virus_cells import Virus_cells
from solid_blocks import Solid_blocks
import math
import random
from menu import Menu
from particle import Particle
from smoke import Smoke


class MyGame(arcade.View):
    """ Main application class. """

    def __init__(self):
        """
        Initializer
        """
        super().__init__()

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
    
        # Sprite lists
        self.coin_list = None
        self.wall_list = Solid_blocks().wall_list
        self.player_list = None
        self.brick_list = Destroyable_blocks().random_wall_list
        self.virus = Virus_cells()
        self.enemies = Virus_cells().virus_cells
        self.walls_and_bricks = None
        self.bullet_list = None
        self.explosions_list = None
        self.score = 0 
        
        self.player_sprite = None
        self.physics_engine = None

        self.background = None
        self.width = constants.SCREEN_WIDTH
        self.height = constants.SCREEN_HEIGHT

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.walls_and_bricks = arcade.SpriteList()
        self.destroyable_objects = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.explosions_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", constants.SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64
        self.player_sprite.hurt_sound = arcade.Sound("assets/sounds/hurt2.wav")
        self.player_sprite.game_over_sound = arcade.Sound("assets/sounds/gameover4.wav")
        self.player_list.append(self.player_sprite)

        # Add all of the obstacles 
        self.walls_and_bricks.extend(self.wall_list)
        self.walls_and_bricks.extend(self.brick_list)
        # self.walls_and_bricks.extend(self.enemies)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.walls_and_bricks)

        # Set the background color/image
        self.background = arcade.load_texture("assets/images/Covidman_background_lvl1.jpeg")

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
        self.explosions_list.draw()

        # Draw the Score
        arcade.draw_text(f"Score: {self.score}", int((constants.SCREEN_WIDTH / 2) - 64), constants.SCREEN_HEIGHT - 50, arcade.color.BLACK, 25)
    
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = constants.MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -constants.MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -constants.MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = constants.MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if (key == arcade.key.UP) or (key == arcade.key.W) or (key == arcade.key.S) or (key == arcade.key.DOWN):
            self.player_sprite.change_y = 0
        elif (key == arcade.key.LEFT) or (key == arcade.key.RIGHT) or (key == arcade.key.D) or (key == arcade.key.A):
            self.player_sprite.change_x = 0

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        "Called when the user presses the mouse"

        # Create a bullet/laser 
        bullet = arcade.Sprite("assets/images/laserRed01 copy.png", constants.BULLET_SCALING)
        bullet.sound = arcade.Sound("assets/sounds/laser2.wav")
        bullet.sound.play()

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

        # Call update on all sprites 
        self.physics_engine.update() 
        self.bullet_list.update()
        self.explosions_list.update()
        self.enemies.update()
        self.bullet_list.update()
        
        for bullet in self.bullet_list:

            # Check for all the collisions that the bullet will have
            has_hit_bricks = arcade.check_for_collision_with_list(bullet, self.brick_list)
            has_hit_obstacles = arcade.check_for_collision_with_list(bullet, self.walls_and_bricks)
            has_hit_solid_blocks = arcade.check_for_collision_with_list(bullet, self.wall_list)
            has_hit_enemies = arcade.check_for_collision_with_list(bullet, self.enemies)

            for brick_hit in has_hit_bricks:
                brick_hit.explosion_sound = arcade.Sound("assets/sounds/explosion2.wav")
                brick_hit.explosion_sound.play()
                brick_hit.health -= 1

                if brick_hit.health == 3:
                    brick_hit.texture = (arcade.load_texture("assets/images/brickTextureWhite Hit1.png"))
    
                if brick_hit.health == 2:
                    brick_hit.texture = (arcade.load_texture("assets/images/brickTextureWhite Hit2.png"))

                if brick_hit.health == 1:
                    brick_hit.texture = (arcade.load_texture("assets/images/brickTextureWhite Hit3.png"))
                    
                if brick_hit.health == 0:
                    for i in range(constants.PARTICLE_COUNT):
                        particle = Particle(self.explosions_list)
                        particle.position = brick_hit.position
                        self.explosions_list.append(particle)
                    smoke = Smoke(50)
                    smoke.position = brick_hit.position
                    self.explosions_list.append(smoke)
                    
                    brick_hit.remove_from_sprite_lists()

            for hit in has_hit_solid_blocks:
                hit.sound = arcade.Sound("assets/sounds/hurt2.wav")
                hit.sound.play()

            for enemie in has_hit_enemies:
                enemie.health -= 1

                if enemie.health == 3:
                    enemie.color = (255,255,0)   #Yellow    
                    enemie.change_x = enemie.change_x * 1.5 
                    enemie.change_y = enemie.change_y * 1.5 

                if enemie.health == 2:
                    enemie.color = (255,153,51)  #Orange
                    enemie.change_x = enemie.change_x * 1.5 
                    enemie.change_y = enemie.change_y * 1.5 

                if enemie.health == 1:
                    enemie.color = (255,0,0)   #Red
                    enemie.change_x = enemie.change_x * 1.5 
                    enemie.change_y = enemie.change_y * 1.5 

                if enemie.health == 0:
                    self.score += random.randint(2,5)
                    enemie.remove_from_sprite_lists()
            
            if (len(has_hit_bricks) > 0) or (len(has_hit_obstacles) > 0) or (len(has_hit_enemies) > 0):
                bullet.remove_from_sprite_lists()
                
            # if bullet is off screen, remove it.
            if bullet.bottom > self.width or bullet.top < 0 or bullet.right < 0 or bullet.left > self.width:
                bullet.remove_from_sprite_lists()

        for player in self.player_list:
            virus_player_collision = arcade.check_for_collision_with_list(player, self.enemies)
            # wall_collision = arcade.check_for_collision_with_list(player, self.walls_and_bricks) #Come back to this later if time

            if (len(virus_player_collision) > 0):
                player.game_over_sound.play()
                player.remove_from_sprite_lists()
                self.write_score_file(self.score)
                game_over_view = GameOver()
                self.window.show_view(game_over_view)
 
        #Check to see if a enemie hits an obstacle (walls, other enemie, destroyable_block)
        for enemy in self.enemies:
            # if len(arcade.check_for_collision_with_list(enemy, self.walls_and_bricks)) > 0:
            #     enemy.change_x *= -1
            #     enemy.change_y *= -1
            enemies_physics_engine = arcade.PhysicsEngineSimple(enemy, self.walls_and_bricks)  #Create basic physics engine with enemy and all walls and bricks    
            enemies_physics_engine.update()   
            self.follow_sprite(enemy, self.player_sprite)
           
    def follow_sprite(self, current, player_sprite):
        """ This method will move the current sprite to the player sprite
        Based off of the example given at https://arcade.academy/examples/sprite_follow_simple_2.html
        """
    
        current.center_x += current.change_x
        current.center_y += current.change_y

        # Random 1 in 100 chance that we'll change from our old direction and
        # then re-aim toward the player
        if random.randrange(0,100) == 0:

            # Get the position of the enemy in this case
            start_x = current.center_x
            start_y = current.center_y

            # Get the destination of the enemy (the player_sprite's position)
            dest_x = player_sprite.center_x
            dest_y = player_sprite.center_y

            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            # Calculate changes
            current.change_x = math.cos(angle)# * random.randrange(1,2)
            current.change_y = math.sin(angle)# * random.randrange(1,2)
    
    def write_score_file(self, score):
        file = open("game_scores.txt", "a")
        file.write(f"{str(score)}\n")
        file.close()

class Menu(arcade.View):
     """ Class that manages the 'menu' view. """

     def on_show(self):
        """ Called when switching to this view"""
        # arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")
        arcade.set_background_color(arcade.color.WHITE)

     def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        arcade.draw_text("Welcome to COVIDman! - Click to start >>>", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2, arcade.color.BLUE, font_size=30, anchor_x="center")
        arcade.draw_lrwh_rectangle_textured(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, arcade.load_texture("assets/images/3839350.jpg"))

     def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ Use a mouse press to advance to the 'game' view. """
        game_view = MyGame()
        game_view.setup()
        self.window.show_view(game_view)

class GameOver(arcade.View):
     """ Class that manages the 'menu' view. """

     def on_show(self):
        """ Called when switching to this view"""
        # arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")
        arcade.set_background_color(arcade.color.WHITE)

     def on_draw(self):
        """ Draw the menu """

        file = open("game_scores.txt", "r")
        lines = file.readlines()
        
        scores_list = []
        
        for i in lines:
            clear = i.rstrip("\n")
            score = int(clear)
            scores_list.append(score)

        last_score = scores_list[-1]
        high_score = max(scores_list)

        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, arcade.load_texture("assets/images/game_over.jpg"))
        arcade.draw_text(f"Score: {last_score}", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/3, arcade.color.WHITE, font_size=30, anchor_x="center")
        arcade.draw_text(f"High score: {high_score}", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/3 - 40, arcade.color.WHITE, font_size=30, anchor_x="center")        

     def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ Use a mouse press to advance to the 'game' view. """
        game_view = MyGame()
        game_view.setup()
        self.window.show_view(game_view)

def main():
    """ Main method """
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    menu_view = Menu()
    window.show_view(menu_view)
    arcade.run()

if __name__ == "__main__":
    main() 
