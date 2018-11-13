# #Guessing game for numbers between 1 to 10
print "Welcome to the number guessing game"
print "I am thinking of a number between 1 and 10"

# import random
# n = 5 #random.randint(1, 11)
# guess = int(raw_input("Guess the number: "))
# while n != "guess":
#     print
#     if guess < n:
#         print "guess is low"
#         guess = int(raw_input("Guess again: "))
#     elif guess > n:
#         print "guess is high"
#         guess = int(raw_input("Guess again: "))
#     else:
#         print "you guessed it!"
#         break
#     print

secret_number = 5
guess = int(raw_input("What's the number? "))
while secret_number != "guess":
    if guess < secret_number:
        print "%d is too low. Guess again." % guess
        guess = int(raw_input("What's the number? "))
    elif guess > secret_number:
        print "%d is too high. Guess again." % guess
        guess = int(raw_input("What's the number? "))
    else:
        print "Yes! You win!"
        break
