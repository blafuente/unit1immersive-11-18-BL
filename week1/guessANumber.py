#Following along with teacher code.
 
import random
userName = raw_input("What is your name? ")

# Set up the (not-so) secret number as 5.
# secret_number = 5

#Generate random number.
secret_number = random.randint(1,10)
print secret_number

# Init the bool gameOn to True
gameOn = True

#Init a number of guesses
allowedGuesses = 5
#Init userGuesses
userGuesses = 0

#init keep playing to True
keepPlaying = True

while(keepPlaying):    
    # Run a loop until gameOn = False
    while(gameOn):
        # Get user's input and set it to userGuess
        userGuess = int(raw_input("Guess a number between 1 and 10: "))
        
        userGuesses += 1
        print "You have %d guesses left" % (allowedGuesses-userGuesses)


        # if the userGuess = secret_number, change gameOn = False
        if (userGuess == secret_number):
            gameOn = False
            print "Great job, %s. Game over." % userName
        # if you userGuess don't match secret number.  
        else:
            if(userGuesses == allowedGuesses):
                gameOn = False
                print "You are out of guesses! The number was %d" % secret_number

            # if user's guess is too high.
            elif (userGuess > secret_number):
                print "%i is too high." % userGuess
                print "You have %d guesses left" % (allowedGuesses-userGuesses)
            # if user's guess is too low. 
            else:
                print "%s, %i is too low." % (userName, userGuess)    
                print "Guess again...You have %d guesses left" % (allowedGuesses-userGuesses)

    playAgain = raw_input("Would you like to play again? [y/n]")
    if (playAgain == "n"):
        keepPlaying = False
        print ("Thanks for playing, %s") % userName
    elif(playAgain == 'y'):
        # Reset all the vars
        secret_number = random.randint(1,10)
        gameOn = True
        userGuesses = 0
    else:
        print ("Huh?")
        playAgain