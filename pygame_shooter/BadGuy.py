from math import hypot
from pygame.sprite import Sprite
import pygame
from random import randint
class BadGuy(Sprite):
    def __init__(self):
        super(BadGuy,self).__init__()
        self.x = randint(250, 501)
        self.y = randint(250, 451)
        self.speed = randint(1,4)
        self.rect = pygame.Rect(0,0,32,32)
        self.rect.centerx = self.x
        self.rect.top = self.y 
    def update_me(self, theHero):
        dx = self.x - theHero.x
        dy = self.y - theHero.y
        dist = hypot(dx, dy)
        dx = dx / dist
        dy = dy / dist
        self.x -= dx * self.speed
        self.y -= dy * self.speed
        self.rect.x = self.x
        self.rect.y = self.y