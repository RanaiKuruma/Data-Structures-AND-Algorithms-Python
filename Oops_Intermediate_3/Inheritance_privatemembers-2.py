# Parent Class
class Vehicle():
    def __init__(self, make, model, fuel):
        self.make = make
        # Private attr
        self.__model = model 
        self.__fuel = fuel

    def __private_method_parent(self):
        print("This is Private")    

# Child Class
class Car(Vehicle):
    def __init__(self, make, model, fuel, air_conditioning, sunroof):
        Vehicle.make = make
        Vehicle.__model = model
        Vehicle.__fuel = fuel

        self.air_conditioning = air_conditioning
        self.sunroof = sunroof

    def show_parent_attribute(self):
        print(Vehicle.make, " ", Vehicle.__model, " ", Vehicle.__fuel) 

    def show_privatemethod_ofparent(self):
        self._Vehicle__private_method_parent()

myobj = Car('Tesla', 2019, "Electric", True, True)
        
# print(myobj.__dict__)
# print(myobj.show_parent_attribute())
# print(myobj.make)

# Private attr and method
# print(myobj.__model)

# print(myobj.show_privatemethod_ofparent())

#or

# print(myobj._Vehicle__private_method_parent())
