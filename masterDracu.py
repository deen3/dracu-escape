
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
    pygame.init()
    pygame.font.init()
 
    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    # load images to use
    icon = pygame.image.load("includes/img/icon.png")
    logo = pygame.image.load("includes/img/dracu-logo.png")
    btm = pygame.image.load("includes/img/back-to-menu.png")
    btmH = pygame.image.load("includes/img/back-to-menuH.png")
    back_to_menu = btm # set btn as the initial image of menu button
 
    pygame.display.set_caption("DRACU-ESCAPE")
    pygame.display.set_icon(icon)
    
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
    done = False
    play = False
    menu = False
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
    music = True
    score = 0
 
    # -------- Main Program Loop -----------
    while not done or not over:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop
                over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    dracu.jump()
                        
        # if the game doesn't display menu
        if not menu:
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
                
                menu = True
                over = True
                
        # -------- Menu -----------            
        if menu:
            score = score
            textSurface, textRect = display_text(constants.B_GREEN, notif, 100, 300, 100, 250, 100)
            screen.blit(textSurface, textRect)
            textSurface, textRect = display_text(constants.WHITE, str(score), 50, 350, 200, 250, 100)
            screen.blit(textSurface, textRect)

            textSurface, textRect = display_text(play_color, "Play Again", 50, 100, 400, 200, 100)
            screen.blit(textSurface, textRect)
            textSurface, textRect = display_text(quit_color, "Quit", 50, 500, 400, 200, 100)
            screen.blit(textSurface, textRect)

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            
            if 100+200 > mouse[0] > 100 and 400+100 > mouse[1] > 400:
                play_color = constants.B_GREEN
                if click[0] == 1:
                    main()
                else:
                    play_color = constants.GREEN
                    
            if 500+200 > mouse[0] > 500 and 400+100 > mouse[1] > 400:
                quit_color = constants.B_RED
                if click[0] == 1:
                    pygame.quit()
                    break
                else:
                    quit_color = constants.RED
        # -------- End of Menu -----------  

        if not over:
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
 
            # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
            current_level.draw(screen)
            active_sprite_list.draw(screen)

            # -------- Prompt to Start Game -----------  
            if not play:
                # display interactive buttons // display_text(color, text, font_size, x, y, w, h):
                textSurface, textRect = display_text(play_color, "", 100, 300, 100, 250, 100)
                screen.blit(textSurface, textRect)

                #pygame.draw.rect(screen, constants.GREEN, (580, 550, 200, 50))
                
                score = 0

                # ALL CODE FOR BUTTON INTERACTIONS GOES BELOW THIS COMMENT  
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                
                # if mouse hovered the play button
                if 300+250 > mouse[0] > 300 and 100+100 > mouse[1] > 100:
                    play_color = constants.B_GREEN
                    if click[0] == 1:
                        play = True
                        dracu.go_right()
                else:
                    play_color = constants.GREEN

                # if mouse hovered the back to menu button
                if 580+188 > mouse[0] > 580 and 550+42 > mouse[1] > 550:
                    back_to_menu = btmH # changed the back to menu button to hovered button
                else:
                    back_to_menu = btm
                    
                # ALL CODE FOR PLAY BUTTON INTERACTION GOES ABOVE THIS COMMENT

            # -------- End of Prompt to Start Game -----------
             
            if music and play:
                conn = sqlite3.connect("dracuDb.s3db")
                cur = conn.execute("SELECT * FROM dracuOption")
                first_row = next(cur)
                for row in chain((first_row,),cur):
                    # if music is on
                    if str(row[0]) == "ON": 
                        pygame.mixer.music.play(10)
                        music = False
                
        textSurface, textRect = display_text(constants.WHITE,"Score: "+str(score), 20,600,0,150,50,)
        screen.blit(textSurface, textRect)

        screen.blit(logo,(5,545))
        screen.blit(back_to_menu,(580,550))

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        if not menu:
            # scoring depends on time
            score += 1
     
        # Limit to 120 frames per second
        clock.tick(480) 
     
        # Updating the screen...
        pygame.display.flip()

 
if __name__ == "__main__":
    main()
