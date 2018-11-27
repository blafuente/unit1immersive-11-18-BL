import pygame
from pygame.locals import *
import os
import sys
import math
from vegeta import Vegeta

pygame.init()

theHero = Vegeta()

screen_size = (800,600)
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Space Shooter")

background_image = pygame.image.load('starfield.png')
dbz_image = pygame.image.load('vegeta.png')


bgW, bgH = background_image.get_rect().size 
bgx = 0
bgx2 = background_image.get_width()
clock = pygame.time.Clock()
speed = 30

game_on = True
while game_on:
    pygame_screen.blit(background_image,[bgx,0])
    pygame_screen.blit(background_image,[bgx2,0])
    
    pygame.display.update()
    clock.tick(speed)
    bgx -= 1.4  
    bgx2 -= 1.4
    if bgx < background_image.get_width() * -1:
        bgx = background_image.get_width()
        # This resets the image when it reaches it end
    # Brings back the game so it runs at the end of the first image    
    if bgx2 < background_image.get_width() * -1:
        bgx2 = background_image.get_width()
    pygame_screen.blit(dbz_image,[theHero.x,theHero.y])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # THE USER CLICKED THE RED DOT!
            #These aren't the droids were lookin for. quit
            game_on = False

        elif event.type == pygame.KEYDOWN:
            # print (event.key)
            if event.key == 275:
                theHero.shouldMove('right')
            elif event.key == 276: #Left Arrow
                theHero.shouldMove('left')
            if event.key == 273: # Up Arrow
                theHero.shouldMove('up')
            elif event.key == 274: # Down Arrow
                theHero.shouldMove('down')

            # elif event.key == 32:
            #     # Space Bar ... FIRE!!
            #     new_arrow = Arrow(theHero)
            #     arrows.add(new_arrow)
            #     bg_music = pygame.mixer.Sound('shoot.wav')
            #     bg_music.play()

        elif event.type == pygame.KEYUP: # The user RELEASED a key
            # print (event.key)
            if event.key == 275: #Up Arrow
                theHero.shouldMove('right',False)
            elif event.key == 276: #Left Arrow
                theHero.shouldMove('left',False)
            if event.key == 273: # Up Arrow
                theHero.shouldMove('up',False)
            elif event.key == 274: # Down Arrow
                theHero.shouldMove('down',False)    
