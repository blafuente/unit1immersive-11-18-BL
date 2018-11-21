from random import randint

class Hero(object):
    def __init__(self,name, power):
        self.name = name
        self.health = 10
        self.power = 5
    def cheer_hero(self):
        print "Welcome, brave %s" % (self.name)
    def take_damage(self, amount_of_damage):
        self.health -= amount_of_damage
    def is_alive(self):
        return self.health > 0
    def gainHealth(self):
        self.health += randint(3,6)

