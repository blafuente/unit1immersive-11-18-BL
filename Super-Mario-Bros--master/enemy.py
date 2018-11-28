import pygame
from pygame.sprite import Sprite
from random import randint

class Enemy(Sprite):
    def __init__(self):
        super(Enemy,self).__init__()
        self.x = randint(100,550)
        self.y = 50
        self.speed = randint(1,10)
    def update_me(self):
        self.y += self.speed
         