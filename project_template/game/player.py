import arcade 

class Player(arcade.Sprite):
    
    def __init__(self):

        super().__init__()
        self.player_list = None
        self.player_sprite = None
        self.setup()
    
    def setup(self):
        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite("assets/images/idle_robot.png", 0.1)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 108
        self.player_health = 1
        self.player_sprite.hurt_sound = arcade.Sound("assets/sounds/hurt2.wav")
        self.player_sprite.game_over_sound = arcade.Sound("assets/sounds/gameover4.wav")
        self.player_list.append(self.player_sprite)
        print(self.player_sprite.get_hit_box())

