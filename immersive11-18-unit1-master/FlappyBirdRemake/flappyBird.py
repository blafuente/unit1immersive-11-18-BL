from itertools import cycle
import random
import sys
import pygame
from random import randint


pygame.init()

FPS = 30 #counter working that counts every frame
screen_size = (288,512)
pipe_gap_size = 100

pygame_screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()

gameover_image = pygame.image.load('gameover.png')

redbird_downflap_image = pygame.image.load('redbird-downflap.png')
#redbird_midflap_image = pygame.image.load('redbird-midflag.png')
#redbird_upflap_image = pygame.image.load('redbird-upflap.png')
#bluebird_upflap_image = pygame.image.load('bluebird-upflap.png')
#bluebird_midflap_image = pygame.image.load('bluebird-midflap.png')
#bluebird_downflap_image = pygame.image.load('bluebird-downflap.png')

#yellowbird_upflap_image = pygame.image.load('yellowbird-upflap.png')
#yellowbird_midflap_image = pygame.image.load('yellowbird-midflap.png')
#yellowbird_downflap_image = pygame.image.load('yellowbird-downflap.png')

#pipe_green_image = pygame.image.load('pipe-green.png')
#pipe_red_image = pygame.image.load('pipe-red.png')

background_day_image = pygame.image.load('background-day.png')
#background_night_image = pygame.image.load('background-night.png')

#def redbird_downflap(x,y):
    #pygame_screen.blit(redbird_downflap_image,[x,y])


def obstacle(xloc, yloc, xsize, ysize):
    pygame.draw.rect(pygame_screen.green, [xloc, yloc, xsize, ysize])
    pygame.draw.rect(pygame_screen.green, [xloc, int[yloc + xsize + space], xsize, 500])

def game_over():
    pygame_screen.blit(gameover_image, [50,100])

    


x = 350
y = 250
y_speed = 0
x_speed = 0
ground = 477
xloc = 288
yloc = 0
xsize = 70
ysize = randint(0,350)
space = 100
opspeed = 2.5

game_on = True

while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_speed = -20

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                y_speed = 5
    pygame_screen.blit(background_day_image,[0,0])
    pygame_screen.blit(redbird_downflap_image,[200,200]).convert_alpha(),

    
    

    y += y_speed

    if y > ground:
        game_over()
        y_speed = 0
        
    pygame.display.flip()
    clock.tick(60)

pygame.quit()