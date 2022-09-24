# Parent Class
class Vehicle():
    def __init__(self, make, model, fuel):
        self.make = make
        self.model = model 
        self.fuel = fuel


# Child Class
class Car(Vehicle):
    def __init__(self, make, model, fuel, air_conditioning, sunroof):

        super(Car,self).__init__(make, model, fuel)

        self.air_conditioning = air_conditioning
        self.sunroof = sunroof

class ElectricVehicle(Car):
    def __init__(self, make, model, fuel, air_conditioning, sunroof, distance):

        super(ElectricVehicle,self).__init__(make, model, fuel, air_conditioning, sunroof)

        self.distance = distance

myobj = ElectricVehicle('tesla', 2022, 'Electric', True, True, 500)        
print(myobj.__dict__)

