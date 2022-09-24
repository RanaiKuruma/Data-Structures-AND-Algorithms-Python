# Parent Class
class Vehicle():
    current_year = 2022
    base_price = 1000

    def __init__(self, make, model, fuel):
        self.make = make

        # Protected attr
        self._model = model 
        self._fuel = fuel

    # Protected Method
    def _get_value(self):
        age = Vehicle.current_year - self._model
        return Vehicle.base_price * (1 / age)


# Child Class
class Car(Vehicle):
    def __init__(self, make, model, fuel, air_conditioning, sunroof):

        super(Car,self).__init__(make, model, fuel)

        self._air_conditioning = air_conditioning
        self._sunroof = sunroof


    # Overriding method - replaces the parent default method
    # Protected method
    def _get_value(self):
        Vehicle.base_price = 5000
        age = Vehicle.current_year - self._model
        print("This is child override method")
        return Vehicle.base_price * (1 / age)


# Driver Program
myobj = Car("Tesla", 2019, "Electric", True, True)

# If a method/attr is private or protected then it should not be accessed 
# Putting an extra keyword  before an attr/method is called name mangling
# Accesing protected attributes
# objectname._attr
print(myobj._air_conditioning)
print(myobj._sunroof)

# Accesing protected methods
# objectname._mehtods
print(myobj._get_value())



