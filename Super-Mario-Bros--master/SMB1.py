import pygame 
from Mario import Mario
from pygame.sprite import Group, groupcollide
from enemy import Enemy 



pygame.init()

screenSize = (600,460)

pygame_screen = pygame.display.set_mode(screenSize)

pygame.display.set_caption('Super Mario Brothers')

backgroundImage = pygame.image.load('marioworld.png')
monster_image = pygame.image.load('goblin.png') # Added by Brian

#Added by Brian
monster = Enemy()
monsters = Group()
monsters.add(monster)


clock = pygame.time.Clock()
mario = Mario()
marios = Group()
marios.add(mario)
gameOn = True
x = mario.x
y = mario.y
print (x) 
print (y) 
bgX = 0
bgY = 0
vel = 5
jumpCount = 10
isJump = 10
tick = 0

bg_music = pygame.mixer.Sound('YaketySax.wav')
bg_music.play()

while gameOn:
    tick += 3
    if(tick % 90 == 0 ):
        monsters.add(Enemy())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                mario.shouldMove('right')
            if event.key == pygame.K_LEFT:
                mario.shouldMove('left')
            # if event.key == pygame.K_SPACE:

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                mario.shouldMove('right', False)
            elif event.key == pygame.K_LEFT:
                mario.shouldMove('left', False)
            # if event.key == pygame.K_SPACE:
                
                # jsJump = True
                # if jumpCount >= -10:
                #     neg = 1
                #     if jumpCount < 0:
                #         neg = -1

                #         y -= (jumpCount ** 2) * 0.5 *neg
                #         jumpCount -= 1
                #     else:
                #         isJump = False

        
                

    pygame_screen.blit(backgroundImage, [bgX,bgY])
    

    for mario in marios:
        mario.draw_me()
        pygame_screen.blit(mario.image, [mario.x, mario.y])
    
    for monster in monsters:
        monster.update_me()
        pygame_screen.blit(monster_image, [monster.x, monster.y])

    pygame.display.update()

    # clock.tick(16)