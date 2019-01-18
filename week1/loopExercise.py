# Multiplication Table
for n in range(1,11):
    for i in range(1,11):
        print n, "x", i, "=", n*i

# # Message within an * banner
# message = raw_input("Enter a word or phrase: ")
# print ('**' + '*' * len(message) + '**')
# print ('* ' + message + ' *')
# print ('**' + '*' * len(message) + '**')

# # Printing a Triangle
# p = int(raw_input("Enter height of triangle: "))
# p += 1
# for i in range(1,p,2):
#     print " " * p + i * '*'
#     p -= 1

# # Ian's triangle code
# height = int(raw_input('Height: '));
# for i in range (0, height):
#     print ('*' * (2 * i + 1)).center(2 * height - 1, ' ')