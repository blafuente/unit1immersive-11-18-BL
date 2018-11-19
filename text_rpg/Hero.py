class Hero(object):
    def __init__(self,name, power = 5):
        self.name = name
        self.health = 10
        self.power = power

theHero = Hero('Link', 8)
print theHero.power


