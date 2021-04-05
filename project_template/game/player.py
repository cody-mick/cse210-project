import arcade
import constants

def load_texture_pair(filename):
    """
    Load a texture pair, with the second being a mirror image.
    """
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, flipped_horizontally=True)
    ]

class PlayerCharacter(arcade.Sprite):
    """ Player Sprite """
    def __init__(self):
        
        # Set up parent class
        super().__init__()

        # Default to face right
        self.character_face_direction = constants.TEXTURE_RIGHT
        
        # Used for flipping between image sequences
        self.cur_texture = 0
        self.scale = constants.SPRITE_SCALING
        
        main_path = "assets/robot animations"

        self.idle_texture_pair = load_texture_pair(f"{main_path}/Idle1.png")

        # Load textures for walking
        self.walk_textures = []
        for i in range(8):
            texture = load_texture_pair(f"{main_path}/Run ({i+1}).png")
            self.walk_textures.append(texture)
            
        self.texture = self.idle_texture_pair[0]
            
        # Load a left facing texture and a right facing texture.
        # flipped_horizontally=True will mirror the image we load.
        texture = arcade.load_texture("assets/robot animations/Idle1.png")
        self.textures.append(texture)
        texture = arcade.load_texture("assets/robot animations/Idle1.png",
                                      flipped_horizontally=True)
        self.textures.append(texture)

        # By default, face right.
        self.texture = texture

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Figure out if we should face left or right
        if self.change_x < 0:
            self.texture = self.textures[constants.TEXTURE_RIGHT]
        elif self.change_x > 0:
            self.texture = self.textures[constants.TEXTURE_LEFT]

        # Idle animation
        if self.change_x == 0:
            self.texture = self.idle_texture_pair[self.character_face_direction]
            return

        # Walking animation
        self.cur_texture += 1
        if self.cur_texture >= 8:
            self.cur_texture = 0
        self.texture = self.walk_textures[self.cur_texture][self.character_face_direction]