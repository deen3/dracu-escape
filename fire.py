"""
Module for managing platforms.
"""
import pygame
 
from spritesheet_functions import SpriteSheet
 
# These constants define our platform types:
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite

FIRE_RIGHT  =   (90, 140, 30, 70)
FIRE_LEFT   =   (90, 213, 30, 70)
FIRE_BOX    =   ( 0, 360, 70, 70)
 
class Fire(pygame.sprite.Sprite):
    """ Platform the user can jump on """
 
    def __init__(self, sprite_sheet_data):
        """ Fire constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        super().__init__()
 
        sprite_sheet = SpriteSheet("includes/img/tiles_spritesheet.png")
        # Grab the image for this platform
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])
 
        self.rect = self.image.get_rect()
