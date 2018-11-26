import pygame
from pygame.locals import *
import os
import sys
import math 

pygame.init()

screen_size = (960, 480)
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Testing Background")

background_image = pygame.image.load('world1_1.png')
bgx = 0
bgx2 = background_image.get_width()
clock = pygame.time.Clock()

speed = 30 
game_on = True
while game_on:
    #This draws the background image onto the screen
    pygame_screen.blit(background_image,[bgx, 0])
    pygame_screen.blit(background_image,[bgx2, 0])
    # pygame.display.flip()
    pygame.display.update()

    clock.tick(speed) #FPS
    # Moving background image back
    
    bgx -= 3  
    bgx2 -= 3

    #Conditional
    # First background image will start at (0,0) and start to move backwards
    #
    if bgx < background_image.get_width() * -1:
        bgx = background_image.get_width()
        # This resets the image when it reaches it end
    # Brings back the game so it runs at the end of the first image    
    if bgx2 < background_image.get_width() * -1:
        bgx2 = background_image.get_width()  

    #To be able to exit out the game 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # THE USER CLICKED THE RED DOT!
            #These aren't the droids were lookin for. quit
            game_on = False
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == 275:
        #         bgx -= 1  
        #         bgx2 -= 1
        #     if event.key == 276:
        #         bgx += 1  
        #         bgx2 += 1    
    
    