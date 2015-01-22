"""
This module is for Dracu's moving customes
"""
import pygame
import sqlite3

import constants

from itertools import chain
from spritesheet_functions import SpriteSheet
 
class Dracu(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """
 
    # -- Attributes
    # Set speed vector of player
    change_x = 0
    change_y = 0
    hit_flag = False
 
    # This holds all the images of running dracu
    running_dracu = []
 
    # List of sprites we can bump against
    level = None
 
    # -- Methods
    def __init__(self):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        sprite_sheet = SpriteSheet("includes/img/dracu.png")
        # Load Dracu's Images
        image = sprite_sheet.get_image(0, 0, 45, 85)
        self.running_dracu.append(image)
        image = sprite_sheet.get_image(45, 0, 45, 85)
        self.running_dracu.append(image)
        image = sprite_sheet.get_image(90, 0, 45, 85)
        self.running_dracu.append(image)
 
        self.image = self.running_dracu[0]
 
        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

        self.burningDracu = sprite_sheet.get_image(134, 0, 61, 85)
 
    def update(self):
        
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.fire_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left

            self.hit_flag = True
            self.image = self.burningDracu
            break;
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.fire_list, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            self.hit_flag = True
            self.image = self.burningDracu
            break;

        """ Move dracu. """
        # Gravity
        self.calc_grav()
 
        # Move to the right
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift

        if not self.hit_flag:
            frame = (pos // 30) % len(self.running_dracu)
            self.image = self.running_dracu[frame]
        
    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .5
 
        # See if we are on the ground.
        if self.rect.y >= 400 and self.change_y >= 0: 
            self.change_y = 0
            self.rect.y = 400 
            
    def jump(self):
        """ Called when user hits 'jump' button. """
        # play sound effect
        conn = sqlite3.connect("dracuDb.s3db")
        cur = conn.execute("SELECT * FROM dracuOption")
        first_row = next(cur)
        for row in chain((first_row,),cur):
            # if music is on
            if str(row[1]) == "ON": 
                pygame.mixer.Sound('includes/sound/jump.wav').play()
            
        # move down a bit and see if there is a platform below us.
        self.rect.y += 1
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.fire_list, False)
        self.rect.y -= 1
 
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= 450: #constants.SCREEN_HEIGHT:
            self.change_y = -10

    # Player-controlled movement:
    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
