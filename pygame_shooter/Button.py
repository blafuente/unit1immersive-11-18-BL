import pygame.font
import pygame

class Start_Button(object):
    def __init__(self,screen):
        # print "Start Button"
        # get the screen, and save it to this object
        self.screen = screen
        # How big is the screen? we need a rect
        self.screen_rect = self.screen.get_rect()

        # set the width of the button image 
        self.width = 250
        # set the height
        self.height = 100
        # set some colors. RGB
        self.button_color = 0,200,150
        self.text_color = 255,255,255
        # get font from pygame
        self.font = pygame.font.Font(None,52)
        # set the rect of the botton
        self.rect = pygame.Rect(0,0,self.width,self.height)
        # set the location of the rect
        self.rect.center = self.screen_rect.center

        # setup the message!
        self.image_message = self.font.render("Play", True, self.text_color)
        self.image_message_rect = self.image_message.get_rect()
        self.image_message_rect.center = self.rect.center
        

