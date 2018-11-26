# 1. Include pygame
# We needed pip to get this for us because Python doesn't ship with it 
import pygame
from Hero import Hero
from BadGuy import BadGuy
from Arrow import Arrow
# Get group and groupcollide from the sprite module
from pygame.sprite import Group, groupcollide

# 2. Initialize Pygame.
# Why do we need to do this? Because they told us to.
pygame.init()

# 3. Make a screen with a size. Thie size MUST be a tuple
screen_size = (512,480)
pygame_screen = pygame.display.set_mode(screen_size)
# set the title of the window that opens...
pygame.display.set_caption("HawkEye")

# Hero Object
theHero = Hero()
theHeros = Group()
theHeros.add(theHero)
# Bad guy object
bad_guy = BadGuy()
bad_guys = Group()
bad_guys.add(bad_guy)
# a list to hold our arrows (quiver)
# A Group is a special pygame "list" for Sprites
arrows = Group()

# ===============VARIABLES FOR OUR GAME===========================
background_image = pygame.image.load('background.png')
hero_image = pygame.image.load('hero.png')
goblin_image = pygame.image.load('goblin.png')
monster_image = pygame.image.load('monster.png')
arrow_image = pygame.image.load('arrow.png')
# heroLoc = {
#     'x' : 0,
#     'y' : 0
# }

bg_music = pygame.mixer.Sound('faf.wav')
bg_music.play()

#================MAIN GAME LOOP==============================
game_on = True
# The loop will run as long as our bool is True
while game_on: #short hand for game_on == True
    # We are in the game loop from here on out!
    # 5. Listen for events and quit if the user clicks the X
    #============EVENT CHECKER=================================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # THE USER CLICKED THE RED DOT!
            #These aren't the droids were lookin for. quit
            game_on = False
        elif event.type == pygame.KEYDOWN:
            # print (event.key)
            if event.key == 275:
                # The user pressed the right arrow! move our dude right
                # heroLoc['x'] += 10
                # theHero.x += 10
                theHero.shouldMove('right')
            elif event.key == 276: #Left Arrow
                theHero.shouldMove('left')
            if event.key == 273: # Up Arrow
                theHero.shouldMove('up')
            elif event.key == 274: # Down Arrow
                theHero.shouldMove('down')

            elif event.key == 32:
                # Space Bar ... FIRE!!
                new_arrow = Arrow(theHero)
                arrows.add(new_arrow)

        elif event.type == pygame.KEYUP: # The user RELEASED a key
            # print (event.key)
            if event.key == 275: #Up Arrow
                theHero.shouldMove('right',False)
            elif event.key == 276: #Left Arrow
                theHero.shouldMove('left',False)
            if event.key == 273: # Up Arrow
                theHero.shouldMove('up',False)
            elif event.key == 274: # Down Arrow
                theHero.shouldMove('down',False)   

    #=================DRAW STUFF===============================        
    # We use blit to draw on the screen. blit = block image transfer
    # blit is a method, that takes 2 arg:
    # 1. What to draw
    # 2. Where to draw it
    # in the docs... SURFACE = our "pygame_screen"
    pygame_screen.blit(background_image,[0,0])
    # Draw the hero
    for theHero in theHeros:
        theHero.draw_me()
        pygame_screen.blit(hero_image,[theHero.x,theHero.y])
    
    # Draw the arrow
    for arrow in arrows:
        arrow.update_me()
        pygame_screen.blit(arrow_image,[arrow.x,arrow.y])
    
    arrow_hit = groupcollide(arrows,bad_guys,True,True)
    if arrow_hit:
        bad_guys.add(BadGuy())

    #Draw the bad guys
    for bad_guy in bad_guys:
        bad_guy.update_me(theHero)
        pygame_screen.blit(monster_image, [bad_guy.x, bad_guy.y])

    badguy_hit = groupcollide(bad_guys, theHeros, True, True)
    if badguy_hit:
        theHero.add(Hero())
    pygame.display.flip()
