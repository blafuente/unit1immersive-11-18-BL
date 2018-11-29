for i in range(1,11):
     print i

for i in range(1,11,2):
     print i



# n = int(raw_input("how big is the square? "))
# for i in range(n):
#     print("*" * n)


w = int(raw_input("width? "))
h = int(raw_input("height? "))
print ("*" * w)
for h in range(h - 2):
         print ("*" + " " * (w-2) + "*")
print ("*" * w)

# print "******"
# print "*    *"
# print "*    *"
# print "******"

# n = int(raw_input('Enter a number of lines: '))

# for i in range(1, n+1):
#     print ((n-i) * ' ' + i * '* ')

j = int(raw_input('What is the number? '))
j = j+1

for i in range(1, j, 1):
     print(' ' * j + i * '* ')
     j = j - 1

# a = int(raw_input("Enter # of layers: "))
# for i in range (1, a*2, 2):
#     # print i
#     print (' ' * (a+1) * '' + i * '* ')
#     a = a - 1

n = int(raw_input('What is your number? '))
for i in range(1, 11):
    print ("%i x %i =") %(n, i), (n*i)






w = int(raw_input("width? "))
h = int(raw_input("height? "))
print ("*" * w)
for h in range(h - 2):
         print ("*" + "Welcome to Digital Crafts" + "*")
print ("*" * w)

