# This is a procedural approach to a text based rpg game
# The hero is fighting the goblin
# The hero has the option to:
# 1. Fight 2. Dance 3. Flee

# Go get the os module from python
import os 
# os.system() will take any linux command and if python run it, it will. 

# Get hero name from player
hero_name = raw_input("What is thy name, brave adventurer? ")

def fight():
    print "Welcome, %s. Thou art brave!" % hero_name
    # declare some variables
    # These variables are in the function scope
    hero_health = 10
    hero_power = 5
    goblin_health = 6
    goblin_power = 2

    # run the game as long as BOTH characters have health > 0
    while hero_health > 0 and goblin_health > 0:
        print """You have %d health and %d power.
        The goblin has %d health and %d power. 
        What do you want to do?
        1. fight goblin
        2. dance
        3. flee """ % (hero_health, hero_power,goblin_health, goblin_power)
        #Get the user's choice
        user_input = raw_input("What is your choice?> ")

        if user_input == '1':
            # The hero has decided to attack
            # Subtract goblin's health by hero power
            goblin_health -= hero_power
            print "You have done %d damage to the goblin" % hero_power
        elif user_input == "2":
            hero_health += 10
            print """The goblin stares at you in disbelieft of your stupidity. 
            His jaw drops as your wounds heal. """
            print "Your health is now %d" % hero_health
        elif user_input == '3':
            print "Goodbye, cowardly %s" % hero_name
            # The break statement will end the loop IMMEDIATELY!!
            break;
        else:
            # User entered something that we didn't offer
            print "Thou fool. You hast stumbled (invalid health)"
            hero_health -= goblin_power
            print "You have %d health." % hero_health

        # Now, it's the goblin's turn
        # Unless he just died from the hero attack
        if goblin_health > 0:
            hero_health -= goblin_power
            print "The goblin hits you for %d damage" % goblin_power
            print "You have %d health." % hero_health
            if hero_health <= 0:
                print "Thou hast been slain."
        else: 
            print "You have slain the goblin!"

        if hero_health < 5:
            print "%s has gone into a rage as death approaches. Power increased!" % hero_name
            hero_power += 5
            print "Your power is now %d" % hero_power    
        raw_input("Hit any key to continue. ")
        os.system("clear")




fight()