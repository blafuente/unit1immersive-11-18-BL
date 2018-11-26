class Car(object):
    def __init__(self,make,model,mpg):
        self.make = make
        self.model = model
        self.mpg = mpg 
    def startCar(self):
        print "%s goes Vroom" % self.model

myCar = Car('Ford',"Focus",40)
myCar.startCar()

class ElectricCar(Car):
    # call this object's constructor
    def __init__(self,make,model,batteryLife):
        # call super class constructor
        super(ElectricCar,self).__init__(make, model, None)
        self.batteryLife = batteryLife 
    def startCar(self):
        print "%s goes ..." % self.model
    
  
car1 = Car("Totyata", "Camry", 35)
car2 = ElectricCar("Tesla", "S", "100kn")
print car1.model
print car1.mpg
print car2.mpg
print car2.batteryLife
car2.startCar()