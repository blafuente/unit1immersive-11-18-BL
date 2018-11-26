# This is our super (parent) class. All other characters will be subclass of this class.
class Character(object):
    def __init__(self,name,health,power):
        self.name = name
        self.health = health
        self.power = power      
    def is_alive(self):
        return self.health > 0
    def take_damage(self, amount_of_damage):
        self.health -= amount_of_damage