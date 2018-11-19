# print ('Hello World') ;
# print 'Hello, World'  ;

# print """
#     It was a dark and stormy night.
#     A murder happened. 
# """

# name = raw_input("Please enter your first name: ")
# print "Hello " + name

# # Variables
# # - strings, letters, numbers, or any other stuff 
# # you can make with a keyboard
# # a Variables is just a fasy way to refer to something else
# # variables do not make the program faster.
# # They make the program slower!
# # Variables make it easier for us to write programs. 

# theBestClass = "the 11-18 immersive"
# print theBestClass

# # Data types:
# #     - Programming languages see different types of variables differently 
# #     - string - English stuff. 
# #     - Number - any integer and for example 2.2e10
# #     - - Floats and integers
# #     - Floats = has a decimal within the value
# #     Booleans - true or false, on or off, 1 or 0, yes or no, right or left
# #     list - list of things
# #     dictionaries - variable of variables
# #     object - super dictionaries

# # Primitive Data types = string, number, boolean

# month = "November";
# print type(month);
# date = 13
# print type(date)
# dateAsFloat = 13.0
# print type(dateAsFloat)
# aBool = True
# print type(aBool)
# aList = []
# print type(aList)
# aDictionary = {}
# print type(aDictionary)

# # concatenate is progromming speak for add things together
# first = "Brian"
# last = "Lafuente"
# fullName = first + last;
# fullName = first + " " + last;
# print fullName

# fourteen = 10 + 4
# print fourteen
# fourteen = "10" + "4"
# print fourteen
# # fourteen = 10 + "4"
# # print fourteen

# # cast = change a variable to a new data type
# fourteen = int("10") + 4
# print fourteen

# Math = +, -, /, *, %
# print 2+2
# print 2-2
# print 2/2
# print 2*2
# % = Modulus, Modulus divides the number and gives you the remainder
# print 2%2
# print 2**3
# print 10**87
# A string and a * and a number = give me X strings
print "-" * 20

# Python does not have a simple incremementer
num = 1;
# num++
num += 1

#Input
# Python 2 = raw_input
# Python 3 = input

name = raw_input("What is your name? ")
print name

#contiditionals
# a single = sign, means set the left to whatever is on the right
# two "==" signs, means compare what's on the left to whatever is on the right

print 2==2
print 2==1
print 2== "2"

secret_number = 5;
if (secret_number ==3):
    print "Secret number is 3";
else:
    print "Secret number is not 3.";

game_on = True;
i = 0;
while(game_on):
    i += 1
    if (i == 10):
        game_on = False
    else:
        print "Game on!!"