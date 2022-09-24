# mro = method resolution order

# Parent Class - 1
class Car():
    def __init__(self, make, model, fuel):
        self.make = make
        self.model = model  
        self.fuel = fuel 

    def get_car_details(self):
        return 'the make of the car is ', self.make, 'from car class' 

# Parent Class - 2           
class ElectricCar():        
    def __init__(self, make, model, fuel):
        self.make = make
        self.model = model  
        self.fuel = fuel 


    def get_car_details(self):
        return 'the make of the car is ', self.make, 'from Electric car class'   

# Multiple Inheritance follows the order you give in defining the child class

# class Taxi(Car, ElectricCar): # Multiple Inheritance
#         def __init__(self, make, model, fuel): 
#             # Keep super() func empty in  multiple inheritance
#             super().__init__(make, model, fuel)


class Taxi(ElectricCar, Car): # Multiple Inheritance
        def __init__(self, make, model, fuel): 
            # Keep super() func empty in  multiple inheritance
            super().__init__(make, model, fuel)


myobj = Taxi('Tesla', 2021, 'electric')            
print(myobj.get_car_details())

# Old Order
# print(Taxi.__mro__) # Gives the execution order of the class acc. to your definition
# mro deals with complex inheritance
# or
# print(Taxi.mro())

# New Order
# print(Taxi.mro())
