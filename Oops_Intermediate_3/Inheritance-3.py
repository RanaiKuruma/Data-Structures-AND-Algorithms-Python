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

        # Syntax of super() function
        # The super() func is used to access the attr of parent class
        # super(child_class, self).__init__(parentattr1, parentattr2, parentattr3, ....)
        super(Car,self).__init__(make, model, fuel)

        self.air_conditioning = air_conditioning
        self.sunroof = sunroof

myobj = Car('Tesla', 2019, "Electric", True, True)
# print(myobj.make)

# Accessing pvt attr via super method
# Just call the parent class while accesing pvt attr instead of calling the child class
print(myobj._Vehicle__model)
print(myobj._Vehicle__fuel)

# Accessing pvt method via super method
# Just call the parent class while accesing mehtod attr instead of calling the child class
# print(myobj._Vehicle__private_method_parent())
