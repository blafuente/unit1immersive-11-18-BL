# 1. Include pygame
import pygame

# 2. Init pygame
# In order to use pygame we have to run the init method
pygame.init()

# 3. Create a screen with a size
# the screen size MUST be a tuple
screen_size = (512,480)
# Actually tell pygame to set the screen up and store it
# so pygame can use it
pygame_screen = pygame.display.set_mode(screen_size)

# Set the title of the window
pygame.display.set_caption('Goblin Chase')

# ========VARIABLES FOR OUR GAME========
background_image = pygame.image.load('background.png')
hero_image = pygame.image.load('hero.png')
goblin_image = pygame.image.load('goblin.png')
monster_image = pygame.image.load('monster.png')

# 4. Create the game loop (while 1)
# create a boolean for whether the game should run or not
game_on = True
while game_on:
    # we aer inside the main game loop.
    # it will keep running as long as our bool is true

    # 5. Add a quit event (requires sys)
    # Pygame comes with an event loop (like JS!)
    for event in pygame.event.get():
        # print event
        if(event.type == pygame.QUIT):
            # we need to give pygame a way out.
            # if we dont.. Python is going to FREAK out
            # because it's inside of an infinite loop
            game_on = False

# 6. Screen.fill (pass bg_color)
    # We want to draw on the screen
    # we are going to use blit (block image transfer)
    # blit is a function and takes 2 arguments:
    # 1. What do you want to draw?
    # 2. Where do you want to draw it?
    pygame_screen.blit(background_image,[0,0])
    pygame_screen.blit(hero_image,[0,0])

    # 7. Flip the screen and start over
    pygame.display.flip()