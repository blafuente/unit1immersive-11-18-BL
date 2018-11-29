from pygame.sprite import Sprite
import pygame

class fireball(Sprite):
    def __init__(self,char):
        super(fireball,self).__init__()
        self.x = x
        self.y = y
        self.speed = 10
        self.rect = pygame.Rect(0,0,32,32)
        self.rect.centerx = self.x
        self.rect.centery = self.y
        self.fireballs = []
        self.fireballs.append(pygame.image.load('110858_28.png'))
        self.fireballs.append(pygame.image.load('110858_32.png'))
        self.fireballs.append(pygame.image.load('110858_40.png'))
        self.fireballs.append(pygame.image.load('110858_41.png'))
        self.img = self.fireballs[0]
        self.cur_fireball = 0

    def update_me(self):
        self.cur_fireball += 1
        if self.cur_fireball == 4:
            self.cur_fireball = 0
        self.img = self.fireballs[self.cur_fireball]
        self.x += self.speed
        self.rect.x = self.x
        self.rect.y = self.y

x = 325
y = 400
width =  64
height  = 30