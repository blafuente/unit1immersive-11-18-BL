import pygame.font

class Start_Button():
    def __init__(self,screen):
        #print "start Button"
        #get the screen and save it to this object
        self.screen = screen
        #how big is the screen? we need a rect
        self.screen_rect = self.screen.get_rect()

        #set the width of the button image
        self.width =250
        #set the height
        self.height = 100
        #set some colors
        self.button_color = 0,200,150
        self.text_color = 255,255,255
        #get font from pygame
        self.font = pygame.font.Font(None,52)
        #set the rect of the buttons
        self.rect = pygame.Rect(0,0,self.width,self.height)
        #set the location of the rect
        self.rect.center = self.screen_rect.center

    def setup_message(self):
        #set up message
        self.image_message = self.font.render("Play",True, self.text_color)
        self.image_message_rect = self.image_message.get_rect()
        self.image_message_rect.center = self.rect.center

    def draw_button(self):
        #fill in the button
        self.screen.fill(self.button_color,self.rect)
        #actually draw the button
        self.screen.blit(self.image_message,self.image_message_rect)

