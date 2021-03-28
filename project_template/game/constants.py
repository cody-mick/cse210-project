from PIL import Image
stone_img = Image.open("assets/images/stoneCenter.png")
img_width, img_height = stone_img.size 


SPRITE_SCALING = 0.5
BULLET_SCALING = 1
stone_img_width = int(img_width * SPRITE_SCALING)
stone_img_height = int(img_height * SPRITE_SCALING)

SCREEN_WIDTH = 832
SCREEN_HEIGHT = 640
SCREEN_TITLE = "Sprite Move with Walls Example"


MOVEMENT_SPEED = 5 
BULLET_SPEED = 10