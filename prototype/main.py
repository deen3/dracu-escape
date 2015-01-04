##Notes:
##    CAMEL CASES = variables
##    POTHOLE CASES = functions
##Developer: DINA MARCAIDA FAJARDO

import pygame
import time

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

hero_width = 50
hero_height = 150

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Dracu Riot - (c)dinaFajardo')
clock = pygame.time.Clock()

bgImg = pygame.image.load('bg-game-play.png')
heroStill = pygame.image.load('hero-still.png')
heroWalk = pygame.image.load('hero-walk.png')
heroAttack = pygame.image.load('hero-attack.png')
#peopImg = pygame.image.load('vamp-male.png')

def hero(custome, x,y):
    gameDisplay.blit(custome,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
    
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    
    time.sleep(2)

    game_loop()
    
def game_loop():
    x = (display_width * 0.45) - 350
    y = (display_height * 0.45)

    x_change = 0
    y_change = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_UP:
                    y_change = -5
                if event.key == pygame.K_DOWN:
                    y_change  = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0


        x += x_change
        y += y_change
       
        gameDisplay.blit(bgImg, (0,0))
        hero(heroStill, x,y)
        gameDisplay.blit(bgImg, (0,0))
        hero(heroWalk, x,y)

        #boundaries 
        if x > display_width - hero_width or x < 0:
            x -= x_change
        
        if y > display_height - hero_height or y < 0:
            y -= y_change

        if x == 0 and y == 0:
            message_display("I got you!")
        
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
