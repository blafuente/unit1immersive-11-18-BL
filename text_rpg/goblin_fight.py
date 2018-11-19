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
    monster_health = 9
    monster_power = 3
    

    # run the game as long as BOTH characters have health > 0
    while hero_health > 0 and goblin_health > 0 and monster_health >0:
        print """
        You have %d health and %d power.
        The goblin has %d health and %d power.
        The monster has %d health and %d power. 
        What do you want to do? 
        """ % (hero_health, hero_power,goblin_health, goblin_power, monster_health, monster_power)
        #Get the user's choice
        user_input = raw_input("Which enemy do you want to attack? [goblin/monster]> ")
        
        if user_input == 'goblin':
            print """    
    .-')          _
   (`_^ (    .----`/
    ` )  \_/`   __/     __,
    __{   |`  __/      /_/
   / _{    \__/ '--.  //
   \_> \_\  >__/    \((
        _/ /` _\_   |))
  jgs  /__(  /______/
            
            """
            print """
            What do you want to do? 
            1. Fight
            2. Dance
            3. Flee """
            userInput = raw_input(">")

            if userInput == '1':
                # The hero has decided to attack
                # Subtract goblin's health by hero power
                goblin_health -= hero_power
                print "You have done %d damage to the goblin" % hero_power
            elif userInput == "2":
                hero_health += 1
                print """The goblin stares at you in disbelieft of your stupidity. 
                His jaw drops as your wounds heal. """
                print "Your health is now %d" % hero_health
            elif userInput == '3':
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
        
        elif user_input == 'monster':
            print """
  <=======]}======
    --.   /|
   _\"/_.'/
 .'._._,.'
 :/ \{}/
(L  /--',----._
    |          \\
   : /-\ .'-'\ / |
snd \\, ||    \|
     \/ ||    ||
            """
            print """
            What do you want to do? 
            1. Fight
            2. Dance
            3. Flee """
            userInput = raw_input(">")

            if userInput == '1':
                # The hero has decided to attack
                # Subtract goblin's health by hero power
                monster_health -= hero_power
                print "You have done %d damage to the monster" % hero_power
            elif userInput == "2":
                hero_health += 1
                print """The monster stares at you in disbelieft of your stupidity. 
                His jaw drops as your wounds heal. """
                print "Your health is now %d" % hero_health
            elif userInput == '3':
                print "Goodbye, cowardly %s" % hero_name
                # The break statement will end the loop IMMEDIATELY!!
                break;
            else:
                # User entered something that we didn't offer
                print "Thou fool. You hast stumbled (invalid health)"
                hero_health -= monster_power
                print "You have %d health." % hero_health

            # Now, it's the goblin's turn
            # Unless he just died from the hero attack
            if monster_health > 0:
                hero_health -= monster_power
                print "The monster hits you for %d damage" % monster_power
                print "You have %d health." % hero_health
                if hero_health <= 0:
                    print "Thou hast been slain."
            else: 
                print "You have slain the monster!"

            if hero_health < 5:
                print "%s has gone into a rage as death approaches. Power increased!" % hero_name
                hero_power += 5
                print "Your power is now %d" % hero_power    
            raw_input("Hit any key to continue. ")
            os.system("clear")
        
        else:
            print "Invalid choice, pick goblin or monster."




fight()