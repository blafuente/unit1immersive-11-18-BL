from random import randint
#This is a subclass of character. So go get Character
from Character import Character
class Vampire(Character):
    def __init__(self):
        # Call parent/super init method
        super(Vampire, self).__init__('Vampire', 15, 4)
        # randomPower = randint(4,7)
        # self.power = randomPower
    def make_girls_swoon(self):
        print ("The skin of the Cullens flashes like diamonds.")