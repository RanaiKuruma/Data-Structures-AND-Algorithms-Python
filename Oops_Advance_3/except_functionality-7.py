
class NegativeCarValue(Exception):

    def __init__(self, value, message = "Car Value cannot be negative"):
        self.value = value 
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message} --> {self.value}'



class Vehicle:
    def __init__(self, make, model, fuel):
        self.make = make 
        self.model = model
        self.fuel = fuel
        self.current_year = 2021


    def get_value(self):
        age = self.current_year - self.model

        try:
            if age < 0:
                raise NegativeCarValue(age)    

            else:
                return 1000 * (1/age)  

        except NegativeCarValue as e:
            print('Error ***', e)        


myobj = Vehicle('Tesla', 2023, 'electric')
print(myobj.get_value())
