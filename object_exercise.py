class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)

# Instantiate an instance object of Person with name of 
# 'Sonny', email of 'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable sonny.
sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')

# Instantiate another person with the name of 
# 'Jordan', email of 'jordan@aol.com', and phone of '495-586-3456', store it in the variable 'jordan'.
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

# Have sonny greet jordan using the greet method.
sonny.greet(jordan)

# Have jordan greet sonny using the greet method.


# Write a print statement to print the contact info (email and phone) of Sonny.


# Write another print statement to print the contact info of Jordan.