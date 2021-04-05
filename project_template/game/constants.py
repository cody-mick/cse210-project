from PIL import Image
import arcade
from arcade.color import YELLOW

stone_img = Image.open("assets/images/stoneCenter.png")
img_width, img_height = stone_img.size 
 
RIGHT_FACING = 0
LEFT_FACING = 1

SPRITE_SCALING = 0.18
BULLET_SCALING = 1
stone_img_width = int(img_width * SPRITE_SCALING)
stone_img_height = int(img_height * SPRITE_SCALING)

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 960
SCREEN_TITLE = "Sprite Move with Walls Example"
TILE_SCALING = 0.44

MOVEMENT_SPEED = 10 
BULLET_SPEED = 30

# Explosions

PARTICLE_GRAVITY = 0.05
PARTICLE_FADE_RATE = 8 # How fast to fade the particle
PARTICLE_MIN_SPEED = 2.5
PARTICLE_SPEED_RANGE = 2.5 
PARTICLE_COUNT = 20
PARTICLE_RADIUS = 3
PARTICLE_COLORS = [arcade.color.RED,
                   arcade.color.RED_BROWN,
                   arcade.color.LAVA,
                   arcade.color.ORANGE_PEEL,
                   arcade.color.YELLOW]
PARTICLE_SPARKLE_CHANCE = 1 # Chance we'll flip the texture to white and make it 'sparkle'

SMOKE_START_SCALE = 0.25
SMOKE_EXPANSION_RATE = 0.03

SMOKE_FADE_RATE = 7
SMOKE_RISE_RATE = 0.5

SMOKE_CHANCE = 0.25