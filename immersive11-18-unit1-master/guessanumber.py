import random

name = raw_input("Hello what is your name? ")
print name + " " + "I am thinking of number from 1 to 10, what number am I thinking?"

attempts = 1
secret_number = random.randint(1,10)
guess = int(raw_input("Enter your guess: "))


playAgain = True

while(playAgain):

        while secret_number != guess and attempts < 6:

            if guess < secret_number:
                print "no loser!, too low"
            elif guess > secret_number:
                print "uggghhh no loser!, too high"           
            guess = int(raw_input("Enter your guess: "))
            attempts  += 1


        if attempts == 6:
            print "sorry " + name + " you're out of attempts"
            print "the secret number was" + " " + str(secret_number)

        else:
            print "Great job " + name + "," " you won! the number was" + " " + str(secret_number)

        break    

playAgain = raw_input("Would you like to play again? y or n ")
if(playAgain == "n"):
    playAgain = False
    print "Why don't you want to play again " + name + " ?"
elif(playAgain == "y"):
    secret_number = random.randint(1,10)
    attempts = 1
    guess = int(raw_input("Enter your guess: "))
    playAgain = True
    
    pass 




