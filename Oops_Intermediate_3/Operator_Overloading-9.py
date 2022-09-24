class Vehicle:
    def __init__(self, make, model, fare):
        self.make = make
        self.model = model 
        self.fare = fare

    def __str__(self):
     return f'The make of the car is {self.make} and the model is {self.model} with a fare of {self.fare}'


    # def __add__(self,no of objects)                                                                 
    def __add__(self, other):
        return self.fare + other.fare

myobj1 = Vehicle('Tesla', 2022, 40) 
myobj2 = Vehicle('Ford', 2021, 80) 

# print(myobj1)

print(myobj1 + myobj2)
