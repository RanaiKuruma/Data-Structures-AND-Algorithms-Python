# Parent Class
class Vehicle():
    current_year = 2022
    base_price = 1000

    def __init__(self, make, model, fuel):
        self.make = make
        # Private attr
        self.__model = model 
        self.__fuel = fuel

    # Polymorphism
    # default function to get value of car
    def get_value(self):
        age = Vehicle.current_year - self.__model
        return Vehicle.base_price * (1 / age)


# Child Class
class Car(Vehicle):
    def __init__(self, make, model, fuel, air_conditioning, sunroof):

        super(Car,self).__init__(make, model, fuel)

        self.air_conditioning = air_conditioning
        self.sunroof = sunroof


    # Overriding method - replaces the parent default method
    def get_value(self):
        Vehicle.base_price = 5000
        age = Vehicle.current_year - self._Vehicle__model
        print("This is child override method")
        return Vehicle.base_price * (1 / age)


# Driver Program
# myobj = Car("Tesla", 2019, "Electric", True, True)
# print(myobj.get_value())

myparentobj = Vehicle("Ford", 2018, "petrol")
print(myparentobj.get_value())