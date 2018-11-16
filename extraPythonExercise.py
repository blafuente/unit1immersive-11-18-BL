#Python Part 1 Exercises
# 1. Prompt the user for his name using the input function
name = raw_input('What is your name? ')
print 'Hello %s !' % name

# 2 Same as the first exercise, but this time print the user's name
# in ALL CAPS
print 'Hello %s !' % name.upper()
print

# 3 Madlib. Promp the user for the missing words to a Madlib sentence.
name2 = raw_input('Enter your name: ')
fave_subject = raw_input('Enter your favorite subject: ')
message = """Please fill in the blanks below: %s's favorite 
subject in school is %s.""" % (name2, fave_subject)
print message
print

# 4 Day of the week.
day = int(input('Enter a numner for a Day (0-6)? '))
days = ({
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
})
dayWeek = days[day]

print dayWeek

# 5 Work or Sleep In?
#day = int(input('Is it a workday or sleep-in Day (0-6)? '))
days = ({
    0: 'Sleep-In',
    1: 'Go to work',
    2: 'Go to work',
    3: 'Go to work',
    4: 'Go to work',
    5: 'Go to work',
    6: 'Sleep-In',
})
dayWeek = days[day]

print dayWeek
print

# 6 Celsius to Fahrenheit
c = float(raw_input("Enter a Temperature to convert C to F: "))
f = (c * 1.8 + 32)
print f
print

# 7 Tip Calculator
cost = float(raw_input("Enter bill amount: "))
service = raw_input("Enter level of service: good/fair/bad: ")
if(service == 'good'):
    cost = (cost * 1.20)
elif(service == 'fair'):
    cost = (cost * 1.15)
elif(service == 'bad'):
    cost = (cost * 1.10)
print '$' + str(float(cost))
# 8 Tip Calculator 2
people = int(raw_input('Enter amount of people to split the bill: '))
print '$' + str(float(cost/people))
print

# 9. 1 to 10
for i in range(1,11):
    print i

#10
coin = 0
print 'You have %i coin(s)' % coin
answer = raw_input('Do you want a coin? ')
while(answer != 'no'):
    print 'You have %i coin(s)' % coin
    answer = raw_input('Do you want another coin? [yes/no] ')
    if(answer == 'yes'):
        coin += 1
    # elif(answer == 'Yes'):
    #     coin += 1
    else:
        print 'Okay, good bye. You have %i coins' % coin
        break