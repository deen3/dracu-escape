
"""
As per requirement in Game Development
DEVELOPER - DINA M. FAJARDO
fajardod91@yahoo.com.ph
"""
import pygame
import time
import sqlite3

import constants
import levels

from itertools import chain
from dracu import Dracu
 
def display_text(color, text, font_size, x, y, w, h):
    pygame.font.init()
    
    font = pygame.font.Font("freesansbold.ttf", font_size)
    textSurface = font.render(text, True, color)
    textRect = textSurface.get_rect()
    textRect.center = ((x+(w/2)), (y+(h/2)))
    return textSurface, textRect
 
def main():
    """ Main Program """
    
    # load images to use
    btn = pygame.image.load("includes/img/btn.png")
    p = pygame.image.load("includes/img/play.png")
    pH = pygame.image.load("includes/img/playH.png")
    pA = pygame.image.load("includes/img/playA.png")
    pAH = pygame.image.load("includes/img/playAH.png")
    m = pygame.image.load("includes/img/back-to-menu.png")
    mH = pygame.image.load("includes/img/back-to-menuH.png")
    logo = pygame.image.load("includes/img/dracu-logo.png")

    # set the initial image of the buttons
    btn_play = p
    btn_menu = m 
 
    # play music if ON
    conn = sqlite3.connect("dracuDb.s3db")
    cur = conn.execute("SELECT * FROM dracuOption")
    first_row = next(cur)
    for row in chain((first_row,),cur):
        if str(row[0]) == "ON": 
            pygame.mixer.music.play(10)
    
    # Create the player
    dracu = Dracu()
 
    # Create all the levels
    level_list = []
    level_list.append(levels.Level_01(dracu))
    level_list.append(levels.Level_02(dracu))
    level_list.append(levels.Level_03(dracu))
 
    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]
 
    active_sprite_list = pygame.sprite.Group()
    dracu.level = current_level
 
    dracu.rect.x = 340
    dracu.rect.y = 400
    active_sprite_list.add(dracu)
 
    # Loop until the user clicks the close button.
    play = False
    play_again = False
    over = False
    
    # font color of PLAY to be interactive
    play_color = constants.GREEN
    quit_color = constants.RED

    # initialize sounds/music
    burningSound = pygame.mixer.Sound('includes/sound/burning.wav')
    pygame.mixer.music.load('includes/music/dracu-level1.wav')
    
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    notif= "GAME OVER"
    score = 0
 
    # -------- Main Program Loop -----------
    while not over:
        # -------- Prompt to Start Game -----------  
        if not play and not play_again:
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            # if mouse hovered the play button
            if 248+287 > mouse[0] > 248 and 136+150 > mouse[1] > 136:
                btn_play = pH
                if click[0] == 1:
                    play = True
                    dracu.go_right()
            else:
                btn_play = p

            # if mouse hovered the back to menu button
            if 580+188 > mouse[0] > 580 and 550+42 > mouse[1] > 550:
                btn_menu = mH # changed the back to menu button to hovered button
            else:
                btn_menu = m
        # -------- End of Prompt to Start Game -----------
            
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                over = True # Flag that we are done so we exit this loop
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    dracu.jump()

        # -------- BELOW Game Playing... -----------                 
        if play:
            # Update the player.
            active_sprite_list.update()
 
            # Update items in the level
            current_level.update()
 
            # If the dracu gets near the right side, shift the world left (-x)
            if dracu.rect.right >= 300:
                diff = dracu.rect.right - 300
                dracu.rect.right = 300
                current_level.shift_world(-diff)

            # If the player gets to the end of the level, go to the next level
            current_position = dracu.rect.x + current_level.world_shift
            if current_position < current_level.level_limit:
                dracu.rect.x = 120
                if current_level_no < len(level_list)-1:
                    current_level_no += 1
                    current_level = level_list[current_level_no]
                    dracu.level = current_level
                else:
                    menu = True
                    notif = "YOU WIN!"
                    # play sound effect
                    pygame.mixer.Sound('includes/sounds/Win.wav').play()

            if dracu.hit_flag == True:
                #stop background music
                pygame.mixer.music.stop()
                # play sound effect dracu burning if sound is ON
                conn = sqlite3.connect("dracuDb.s3db")
                cur = conn.execute("SELECT * FROM dracuOption")
                first_row = next(cur)
                for row in chain((first_row,),cur):
                    # if music is on
                    if str(row[1]) == "ON": 
                        burningSound.play()
                        
                dracu.update()
                
                play = False
                play_again = True
        # -------- ABOVE Game Playing... -----------
        
        # -------- Prompt to Play Game Again -----------  
        if play_again:
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            # if mouse hovered the play button
            if 190+450 > mouse[0] > 190 and 136+150 > mouse[1] > 136:
                btn_play = pAH
                if click[0] == 1:
                    main()
            else:
                btn_play = pA

            # if mouse hovered the back to menu button
            if 580+188 > mouse[0] > 580 and 550+42 > mouse[1] > 550:
                btn_menu = mH # changed the back to menu button to hovered button
            else:
                btn_menu = m
        # -------- End of Prompt to Play Game Again -----------
 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        
        # display menu buttons if not play
        if not play:
            if play_again:
                x = 190
            else:
                x = 248
            screen.blit(btn_play,(x, 136))
            screen.blit(btn_menu,(580,550))
        # display the score otherwise :)
        else: 
            screen.blit(btn,(580,5))
            textSurface, textRect = display_text(constants.WHITE,"Score: "+str(score), 20,600,0,150,50,)
            screen.blit(textSurface, textRect)

        
        # display logo
        screen.blit(logo,(5,545))
            
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # scoring depends on time
        score += 1
     
        # Limit to 120 frames per second
        clock.tick(480) 
     
        # Updating the screen...
        pygame.display.flip()

    # closing the window after executing the while loop..
    pygame.quit()

 
if __name__ == "__main__":
    pygame.init()
    pygame.font.init()

    # load images to use
    icon = pygame.image.load("includes/img/icon.png")
    
    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("DRACU-ESCAPE")
    pygame.display.set_icon(icon)
    
    main()
