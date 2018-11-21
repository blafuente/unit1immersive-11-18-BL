from random import randint

class Goblin(object):
    def __init__(self):
        randomPower = randint(2,5)
        self.name = "Goblin"
        self.health = 6
        self.power = randomPower
    def take_damage(self, amount_of_damage):
        self.health -= amount_of_damage
    def is_alive(self):
        return self.health > 0