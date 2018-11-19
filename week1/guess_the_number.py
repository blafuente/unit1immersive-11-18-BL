def playOn():
    # #Guessing game for numbers between 1 to 10
    print "Welcome to the number guessing game."
    print "I am thinking of a number between 1 and 10"

    import random 
    secret_number = random.randint(1,10);
    print secret_number #printing out secret number to test out when guessed correctly.
    number_of_guesses = 5;
    guess = int(raw_input("What's the number? "))
    while secret_number != "guess":
        #When user runs out of guesses
        if number_of_guesses == 0:    
            print "You're out of guesses"
            #Asks if you want to continue the game
            answer = raw_input("Do you want to play again? [Y/N] ")
            if answer == "Y":
                return playOn()
            elif answer == "N":
                print "Good Bye"
                pass
            break
        #User's guess is low    
        if guess < secret_number:
            print "You have %d guesses left" % number_of_guesses
            number_of_guesses -= 1
            print "%d is too low. Guess again." % guess
            guess = int(raw_input("What's the number? "))
        #User's guess is high    
        elif guess > secret_number:
            print "You have %d guesses left" % number_of_guesses
            number_of_guesses -= 1
            print "%d is too high. Guess again." % guess
            guess = int(raw_input("What's the number? "))
        #User's guess is correct!
        elif guess == secret_number:
            print "Yes! You win!"
            #Asks user if you want to play again.
            answer = raw_input("Do you want to play again? [Y/N] ")
            if answer == "Y":
                return playOn()
            elif answer == "N":
                print "Good Bye"
                pass
            break

#  def gameOn(answer):
#      answer = raw_input("Do you want to play again? [Y/N] ")
#      if answer == "Y":
#          playOn()
#      elif answer == "N":
#          print "good bye"
#          break
  
playOn()   