import pygame
import math,random,sys
from pygame.locals import *
from pygame.sprite import Sprite


class enemy(Sprite):

    walkRight = [pygame.image.load('NES - Dragon Ball Z 5 Bootleg - Enemies & Bosses_.png'),pygame.image.load('NES - Dragon Ball Z 5 Bootleg - Enemies & Bosses_04.png')]
    walkLeft = [pygame.image.load('NES - Dragon Ball Z 5 Bootleg - Enemies & Bosses_05.png'),pygame.image.load('NES - Dragon Ball Z 5 Bootleg - Enemies & Bosses_07.png')]

    def __init__ (self, X, y, width, height, end):
        super(enemy,self).__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x,self.end]
        self.walkCount = 0
        self.vel = 3

    def draw(self,screen):
        self.move()
        if self.walkCount + 1 <= 100:
            self.walkCount = 0

        if self.vel > 0:
            screen.blit(self.walkRight[self.walkCount // 3], (self.x,self.y))
            self.walkCount += 1

        else:
            screen.blit(self.walkLeft[self.walkCount // 3], (self.x,self.y))
            self.walkCount += 1


        pass
    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel *-1
                self.walkCount = 0

    def update_me(self, char):
        dx = self.x - char.x
        dy = self.y - char.y
        dist = hypot(dx, dy)
        dx = dx / dist
        dy = dy /dist
        self.x -= dx * self.vel
        self.y -= dy * self.vel
        self.rect.x = self.x
        self.rect.y = self.y
    
x = 100
y = 280
width =  64
height  = 30

    