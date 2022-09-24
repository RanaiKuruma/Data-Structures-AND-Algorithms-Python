from abc import ABC , abstractmethod

# Abstract Class
class Vehicle(ABC):
    @abstractmethod 
    def getValue(self):
        pass


class Car(Vehicle):
    def __init__(self, make, model, fare):
        self.make = make 
        self.model = model
        self.fare = fare

    def getValue(self):
        return 1000*self.fare


myobj = Car('Tesla', 2022, 40)
print(myobj.getValue())




