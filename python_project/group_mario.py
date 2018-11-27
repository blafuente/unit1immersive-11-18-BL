import pygame
import math,random,sys
from pygame.locals import *


pygame.init()
screen_size = (640,480)

screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption("Khank, Brandon, Brian Project")

walkRight = [pygame.image.load('110858_05.png'),pygame.image.load('110858_03.png')]
walkLeft = [pygame.image.load('110858_44.png'),pygame.image.load('110858_38.png')]
char = pygame.image.load('110858_02.png')
bg = pygame.image.load('world1_1.png')
clock = pygame.time.Clock()

x = 50
y = 380
width =  64
height  = 64
vel = 5
isJump = 10
jumpCount = 10
left = False
right = False
walkCount = 0

bgX = 0
bgY = 0



def draw_screen():
   global walkCount
   screen.blit(bg, (bgX,bgY))

   if walkCount + 1 >= 10:
       walkCount = 0

   if left:
       screen.blit(walkLeft[walkCount // 10],(x,y))
       walkCount += 1

   elif right:
       screen.blit(walkRight[walkCount // 10],(x,y))
       walkCount += 1
   else:
       screen.blit(char,(x,y))



   pygame.display.update()




run = True
while run:


   clock.tick(60)
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           run = False
   keys = pygame.key.get_pressed()

   if keys[pygame.K_LEFT]:
       if bgX < 0:
           bgX += vel
       else:
           x -= vel
       

   elif keys[pygame.K_RIGHT]:
       if x < 640 / 2:
           x += vel
       else:
           bgX -= vel
       right = True
       left = False
   else:
       right = False
       left = False
       walkCount = 0

   if not(isJump):
       if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
            bg_music = pygame.mixer.Sound('minijump.wav')
            bg_music.play()

   else:
       if jumpCount >= -10:
           neg = 1
           if jumpCount < 0:
               neg = -1

           y -= (jumpCount ** 2) * 0.5 *neg
           jumpCount -= 1
       else:
           isJump = False
           jumpCount = 10



   draw_screen()


pygame.quit()