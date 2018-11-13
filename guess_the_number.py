#Guessing game for numbers between 1 to 10
print "Welcome to the number guessing game"
print "I am thinking of a number between 1 and 10"

number = raw_input("Number?: ")
secretNumber = 5

while (number <= 10):
    if (number == secretNumber):
        print "You guessed the right correct number!" + str(number)
    else:
        print "Wrong number, try again."


