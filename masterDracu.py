"""
As per requirement in Game Development
DEVELOPER - DINA M. FAJARDO
fajardod91@yahoo.co.ph
"""
 
import pygame
import time
 
import constants
import levels
 
from player import Player

def display_text(color, text, font_size, x, y, w, h):
    font = pygame.font.Font("freesansbold.ttf", font_size)
    textSurface = font.render(text, True, color)
    textRect = textSurface.get_rect()
    textRect.center = ((x+(w/2)), (y+(h/2)))
    return textSurface, textRect
    
def main():
    """ Main Program """
    pygame.init()
 
    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    icon = pygame.image.load("includes/img/icon.png")
    logo= pygame.image.load("includes/img/dracu-logo.png")
 
    pygame.display.set_caption("DRACU-ESCAPE")
    pygame.display.set_icon(icon)
    
    # Create the player
    player = Player()
 
    # Create all the levels
    level_list = []
    level_list.append(levels.Level_01(player))
    level_list.append(levels.Level_02(player))
    level_list.append(levels.Level_03(player))
 
    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]
 
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
 
    player.rect.x = 340
    player.rect.y = 400#constants.SCREEN_HEIGHT - player.rect.height 
    active_sprite_list.add(player)
 
    # Loop until the user clicks the close button.
    done = False
    play = False
    menu = False

    # font color of PLAY to be interactive
    play_color = constants.GREEN
    quit_color = constants.RED
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    notif= "GAME OVER"
    music = True
    score = 0
 
    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

            # if the game doesn't display menu
            if not menu:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                        player.jump()

                if player.hit_flag == True:
                    # play sound effect
                    pygame.mixer.Sound('includes/sounds/Over.wav').play()
                    menu = True

        # Update the player.
        active_sprite_list.update()
 
        # Update items in the level
        current_level.update()
 
        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right >= 300:
            diff = player.rect.right - 300
            player.rect.right = 300
            current_level.shift_world(-diff)

        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
            else:
                menu = True
                notif = "YOU WIN!"
                # play sound effect
                pygame.mixer.Sound('includes/sounds/Win.wav').play()
 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        if not play:
            #pygame.draw.rect(screen, (40, 40, 40), (300, 100, 250, 100))
            textSurface, textRect = display_text(play_color, "PLAY", 100, 300, 100, 250, 100)
            screen.blit(textSurface, textRect)
            score = 0

            # ALL CODE FOR PLAY BUTTON INTERACTION GOES BELOW THIS COMMENT  
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            
            if 300+250 > mouse[0] > 300 and 100+100 > mouse[1] > 100:
                play_color = constants.B_GREEN
                if click[0] == 1:
                    play = True
                    player.go_right()
            else:
                play_color = constants.GREEN
            # ALL CODE FOR PLAY BUTTON INTERACTION GOES ABOVE THIS COMMENT

        if menu:
            # ALL CODE FOR MENU GOES BELOW THIS COMMENT
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
                else:
                    quit_color = constants.RED
            # ALL CODE FOR MENU GOES ABOVE THIS COMMENT
                  
        if music:
            pygame.mixer.Sound('includes/sounds/GameMusic.wav').play()
            music = False
            
        textSurface, textRect = display_text(constants.WHITE,"Score: "+str(score), 20, 550, 550, 150, 50,)
        screen.blit(textSurface, textRect)

        screen.blit(logo,(5,545))

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
