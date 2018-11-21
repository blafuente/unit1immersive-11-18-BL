import pygame

class Hero(object):
    # Classes always contain two parts:
    # 1. the __init__ = runs only once
    # 2. the methods = run whenever you call them
    def __init__(self):
        self.x = 100
        self.y = 100
        self.speed = 10
        self.should_move_right = False
        self.should_move_left = False
        self.should_move_up = False
        self.should_move_down = False
    def shouldMove(self,direction,start = True):
        if direction == 'right':
            self.should_move_right = start
        if direction == 'left':
            self.should_move_left = start
        if direction == 'up':
            self.should_move_up = start
        if direction == 'down':
            self.should_move_down = start
    def draw_me(self):
        if self.should_move_right:
            self.x += self.speed
        elif self.should_move_left:
            self.x -= self.speed
        if self.should_move_up:
            self.y -= self.speed
        elif self.should_move_down:
            self.y += self.speed
