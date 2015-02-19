
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

def menu():
    # load images to use
    bg = pygame.image.load("includes/img/bg.png")
    bg_sub = pygame.image.load("includes/img/bg-sub.png")
    btn_menu = pygame.image.load("includes/img/btn-menu.png")
    btn_menuH = pygame.image.load("includes/img/btn-menuH.png")
    p = pygame.image.load("includes/img/btn-play.png")
    pH = pygame.image.load("includes/img/btn-playH.png")
    btn_score = pygame.image.load("includes/img/btn-score.png")
    btn_scoreH = pygame.image.load("includes/img/btn-scoreH.png")
    btn_option= pygame.image.load("includes/img/btn-option.png")
    btn_optionH= pygame.image.load("includes/img/btn-optionH.png")

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # initialize button images
    btn_play = p

    loop_menu = True
    while loop_menu:
        # ALL CODE FOR BUTTON INTERACTIONS GO BELOW THIS COMMENT
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 555+188 > mouse[0] > 555 and 150+42 > mouse[1] > 150:
            btn_play = pH
            print("over")
        else:
            btn_play = p
        # ALL CODE FOR BUTTON INTERACTOINS GO ABOVE THIS COMMENT

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT    
        screen.blit(bg,(0,0))
        screen.blit(btn_play, (555,150))
        screen.blit(btn_score, (555,235))
        screen.blit(btn_option, (555,315))
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        clock.tick(480)
        
        # updating the screen
        pygame.display.flip()

 
if __name__ == "__menu__":
    pygame.init()
    pygame.font.init()

    # load images to use
    icon = pygame.image.load("includes/img/icon.png")
    logo = pygame.image.load("includes/img/dracu-logo.png")
    
    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("DRACU-ESCAPE")
    pygame.display.set_icon(icon)
    
    # display logo
    screen.blit(logo,(5,545))

    menu()
