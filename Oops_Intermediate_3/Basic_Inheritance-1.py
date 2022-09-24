# Parent Class
class Vehicle():
    # Global Attributes
    def __init__(self, make, model, fuel):
        self.make = make
        self.model = model 
        self.fuel = fuel

# Child Class
class Car(Vehicle):
    def __init__(self, make, model, fuel, air_conditioning, sunroof):
        # Parent Attributes
        # To access parent attr 
        # parentclass.attr of parent = parent attr
        Vehicle.make = make
        Vehicle.model = model
        Vehicle.fuel = fuel

        self.air_conditioning = air_conditioning
        self.sunroof = sunroof

    def show_parent_attribute(self):
        print(Vehicle.make, " ", Vehicle.model, " ", Vehicle.fuel) 


#  Used for the direct execution of the code i.e interpreter directly runs the code 
myobj = Car('Tesla', 2019, "Electric", True, True)
        
print(myobj.__dict__) # Only shows the child attr
# myobj.show_parent_attribute()

