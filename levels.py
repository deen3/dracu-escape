import pygame
 
import constants
import fire
 
class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """
 
    fire_list = None
    
    # Background image
    background = None
 
    # How far this world has been scrolled left/right
    world_shift = 0
    level_limit = -1000
 
    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving fire
            collide with the player. """
        self.fire_list = pygame.sprite.Group()
        self.player = player
 
    # Update everything on this level
    def update(self):
        """ Update everything in this level."""
        self.fire_list.update()
 
    def draw(self, screen):
        """ Draw everything on this level. """
 
        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(constants.BLACK)
        screen.blit(self.background,(self.world_shift // 3,0))
 
        # Draw all the sprite lists that we have
        self.fire_list.draw(screen)
 
    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """
 
        # Keep track of the shift amount
        self.world_shift += shift_x
 
        # Go through all the sprite lists and shift
        for fire in self.fire_list:
            fire.rect.x += shift_x
 
# Create fire for the level
class Level_01(Level):
    """ Definition for level 1. """
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        self.background = pygame.image.load("includes/img/background_01.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -17000
 
        # Array with type of fire, and x, y location of the fire.
        level = []
        i = 1000
        while i < 17000:
            level.append([fire.FIRE_RIGHT, i, 415])
            i = i+500
            
        # Go through the array above and add fires
        for f in level:
            block = fire.Fire(f[0])
            block.rect.x = f[1]
            block.rect.y = f[2]
            block.player = self.player
            self.fire_list.add(block)
 
# Create firebox for the level
class Level_02(Level):
    """ Definition for level 2. """
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        self.background = pygame.image.load("includes/img/background_02.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -17000
 
        # Array with type of fire, and x, y location of the fire.
        level = []
        i = 1000
        while i < 17000:
            level.append([fire.FIRE_BOX, i, 415])
            i = i+350
            
        # Go through the array above and add fires
        for f in level:
            block = fire.Fire(f[0])
            block.rect.x = f[1]
            block.rect.y = f[2]
            block.player = self.player
            self.fire_list.add(block)

# Create firebox for the level
class Level_03(Level):
    """ Definition for level 3. """
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        self.background = pygame.image.load("includes/img/background_03.jpg").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -10000
 
        # Array with type of fire, and x, y location of the fire.
        level = []
        i = 1000
        while i < 10000:
            level.append([fire.FIRE_BOX, i, 415])
            i = i+300
            level.append([fire.FIRE_RIGHT, i, 415])
            i = i+250
            
        # Go through the array above and add fires
        for f in level:
            block = fire.Fire(f[0])
            block.rect.x = f[1]
            block.rect.y = f[2]
            block.player = self.player
            self.fire_list.add(block)
