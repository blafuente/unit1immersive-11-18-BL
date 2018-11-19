class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = list()
        self.greet_counter = 0


    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
        self.greet_counter += 1
        print "%s has greeted %s %d time(s)" % (self.name, other_person.name, self.greet_counter)

    
    def print_contact_info(self):
        print "%s' email: %s, %s's phone number: %s" % (self.name, self.email, self.name, self.phone)
    
    def add_friend(self, other_person):
        self.friends.append(other_person)
        print len(self.friends)
    
    
# Instantiate an instance object of Person with name of 
# 'Sonny', email of 'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable sonny.
sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
# Instantiate another person with the name of 
# 'Jordan', email of 'jordan@aol.com', and phone of '495-586-3456', store it in the variable 'jordan'.
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
# Have sonny greet jordan using the greet method.
sonny.greet(jordan)
# Have jordan greet sonny using the greet method.
jordan.greet(sonny)
# Write a print statement to print the contact info (email and phone) of Sonny.
print sonny.email, sonny.phone
# Write another print statement to print the contact info of Jordan.
print jordan.email, jordan.phone

class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def print_info(self):
        print self.year, self.make, self.model

car = Vehicle('Nissan', 'Leaf', 2015)
car.print_info()

sonny.print_contact_info()

jordan.print_contact_info()

# jordan.friends.append(sonny)
sonny.friends.append(jordan)

jordan.add_friend(sonny)
jordan.greet(sonny)
print jordan.greet_counter
