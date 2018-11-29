from itertools import cycle
import random
import sys
import pygame
from random import randint
from button import Start_Button

black = (0,0,0)
#white = (255,255,255)
green = (0,100,0)
#red = (250,0,0)


pygame.init()

FPS = 30 #counter working that counts every frame
screen_size = (288,512)
pipe_gap_size = 100

pygame_screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()

start_button = Start_Button(pygame_screen)

pipe_green = pygame.image.load('pipe-green.png')
pipe_green_invert = pygame.image.load('pipe-green1.png')

gameover_image = pygame.image.load('gameover.png')

base = pygame.image.load('base.png')

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

background_day = pygame.image.load('background-day.png')
#background_night_image = pygame.image.load('background-night.png')

#def redbird_downflap(x,y):
    #pygamescreen.blit(redbird_downflap_image,[x,y])

def gameover():
    #font = pygame.font.SysFont(None,75)
    #text = font.render("Game Over", True, red)
    pygame_screen.blit(gameover_image,[60,250])


def obstacle(xloc, yloc, xsize, ysize):
    pygame.draw.rect(pygame_screen, green, [xloc, yloc, xsize, ysize])
    pygame.draw.rect(pygame_screen, green, [xloc, int(yloc+ysize+space), xsize, ysize+500])
    # pygame_screen.blit(pipe_green_invert, [xloc, -yloc])
    # pygame_screen.blit(pipe_green, [xloc, int(yloc + ysize + space)])
    
    



def ball(x,y):
    #pygame_screen.blit(gameover_image, [50,100])
    #pygame.draw.circle(pygame_screen,black,[x,y], 20)
    pygame_screen.blit(redbird_downflap_image,[x,y])

def Score(score):
    font = pygame.font.SysFont(None,30)
    text = font.render("Score: "+str(score), True, black)
    pygame_screen.blit(text,[0,0])




x = 100
y = 250
y_speed = 0
x_speed = 0
ground = 395
xloc = 300
yloc = 0
xsize = 52
ysize = randint(0,320)
yloc = 0
space = 125
obspeed = 3
score = 0


game_on = True
game_start = False

while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_speed = -6

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                y_speed = 5

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            #print mouse_x,mouse_y
            if start_button.rect.collidepoint(mouse_x, mouse_y):
                game_start = True
                #bg_music = pygame.mixer.Sound('faf.wav')
                #bg_music.play()


    pygame_screen.blit(background_day,[0,0])
    #pygame_screen.blit(redbird_downflap_image,[200,200])
    obstacle(xloc, yloc, xsize, ysize)
    ball(x,y)
    Score(score)
    pygame_screen.blit(base,[0,400])

    if game_start:
    

        y += y_speed
        xloc -= obspeed

        if y > ground:
            game_over()
            y_speed = 0
            obspeed = 0

        if x+20 > xloc and y-20 < ysize and x-15 < xsize+xloc:
            gameover()
            obspeed = 0
            yspeed = 0

        if x+20 > xloc and y+20 > ysize + space and x-15 < xsize+xloc:
            gameover()
            obspeed = 0
            y_speed = 0

        if xloc < -80:
            xloc = 300
            y_size = randint(0,350)

        if x > xloc and x < xloc+3:
            score = (score + 1)

    if game_start == False:
        start_button.setup_message()
        start_button.draw_button()
       
    pygame.display.flip()
    clock.tick(60)

    
pygame.quit()