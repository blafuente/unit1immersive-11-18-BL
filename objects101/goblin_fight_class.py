import os
# from [NAMEOFFILE] import [CLASS]
from Hero import Hero
from Goblin import Goblin
from Vampire import Vampire
from random import randint

hero_name = raw_input('What is your name Hero? ')
# There is only one hero
theHero = Hero(hero_name, 8)
theHero.cheer_hero()


while(theHero.is_alive()):
    # There are many, many goblins.
    randMonster = randint(1,2)
    if randMonster == 1:
        monster = Goblin()
    else:
        monster = Vampire()
    print ('A %s approaches!') % monster.name

    while(theHero.is_alive() and monster.is_alive()):

        print """
        You have %d health and %d power.
        The %s has %d health and %d power.
        What do you want to do? 
        """ % (theHero.health, theHero.power,monster.name, monster.health, monster.power )
        #Get the user's choice
        # user_input = raw_input("> ")

        print """
        What do you want to do? 
        1. Fight
        2. Dance
        3. Flee """
        userInput = raw_input(">")

        if userInput == '1':
        # The hero has decided to attack
        # Subtract monster's health by hero power
            monster.take_damage(theHero.power)
            print "You have done %d damage to the %s" % (theHero.power, monster.name)
        elif userInput == "2":
            theHero.gainHealth()
            print """
            The %s stares at you in disbelieft of your stupidity. 
            His jaw drops as your wounds heal. """ % monster.name
            print "Your health is now %d" % theHero.health
        elif userInput == '3':
            print "Goodbye, cowardly %s" % hero_name
            # The break statement will end the loop IMMEDIATELY!!
            break;
        else:
            # User entered something that we didn't offer
            print "Thou fool. You hast stumbled (invalid health)"
            theHero.health -= monster.power
            print "You have %d health." % theHero.health

        # Now, it's the monster's turn
        # Unless he just died from the hero attack
        if monster.is_alive():
            theHero.take_damage(monster.power)
            print "The %s hits you for %d damage" % (monster.name,monster.power)
            print "You have %d health." % theHero.health
            if theHero.is_alive() == 0:
                print "Thou hast been slain."
                break;
        else: 
            print "You have slain the %s!" % monster.name

        if theHero.health < 5:
            print "%s has gone into a rage as death approaches. Power increased!" % hero_name
            theHero.power += 5
            print "Your power is now %d" % theHero.power    
        raw_input("Hit any key to continue. ")
        os.system("clear")
    fight_again = raw_input("Fight another fiend, brave hero [Y/N] ")
    if fight_again == "N":
        break;    