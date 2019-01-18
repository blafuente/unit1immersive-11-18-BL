# Hello, you!
# Prompt the user for their name and greet them.
name = raw_input("What is your name? ")
print("Hello " + name + "!")

# 2. HELLO, YOU!
# Same as the first exercise, but this time print the user's name in ALL CAPS, and also them the number of letters in their name. 
nameUp = name.upper()
print "Hello " + name.upper() + "! You have " ,len(name), " letters in your name."