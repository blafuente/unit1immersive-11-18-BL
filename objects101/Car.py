# # a class is a recipe
# # an object is the food you made with the recipe
# # the recipe can be used lots, and lost of times

# # Our blueprint for making cars is called Car
# class Car(object):
#     # whenever we start making a new car, __init__ will run
#     # we ALWAYS pass self first
#     def __init__(self):
#         # self is special.
#         # self refers to THIS object
#         self.make = "Honda"
#         self.model = "Accord"
#         self.year = 2007
# myCar = Car()
# print myCar.make
# yourCar = Car()
# print yourCar.make
# yourCar.make = "Toyota"
# print myCar.make
# print yourCar.make

# myCar = {
#     "make": "Honda",
#     "model": "Accord",
#     "year": 2007
# }

# print myCar ['make']

# myCar = [
#     "Honda",
#     "Accord",
#     2007
# ]
# print myCar[0]

class Car(object):
    def __init__(self,make,model):
        self.make = make
        self.model = model
    def  changeModel(self, newModel):
        self.model = newModel

zachsCar = Car('Ford', "F150")
chrisCar = Car('Chevy', "Silverado")
zachsCar.isCool = "Awesome!"
zachsCar.changeModel("Fiesta")
print zachsCar.make
print chrisCar.make
print zachsCar.model
print chrisCar.model
print zachsCar.isCool
zachsCar.model = "Focus"
# ZACHS CAR: DON'T MESS WITH ME!
print zachsCar.model