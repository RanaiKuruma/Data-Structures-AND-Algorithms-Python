
class NegativeZeroModelYear(Exception):

    def __init__(self, value, message = "Model year can't be equal or greater than 2021"):
        self.value = value 
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message} --> {self.value}'


class CarModelYearAsString(Exception):

    def __init__(self, value, message = "Model year cannot be strings. Try passing in values"):
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
        self.value = None

    def get_value(self):
        # Write code which might give an error 
        try:
            if type(self.model) == str:
                status = 'custom'
                raise CarModelYearAsString(self.model)    

            elif(self.model >= self.current_year):
                status = 'custom'    
                raise NegativeZeroModelYear

            else:
                self.age = self.current_year - self.model
                self.value = 1000 * (1/self.age)    
                status = 'Success'

        except TypeError:
                self.age = self.current_year - int(self.model)
                self.value = 1000 * (1/self.age)    
                status = 'inbuilt'  

        # else is a block in which logic will be executed  if no exception occurs
        else:
            print("Code ran without any exception")

        # finally gets excecuted no matter what 
        finally:
            if status == 'custom':
                print("Code has custom exceptions, please rectify that")    

            elif status == 'inbuilt':
                print("Code has inbuilt exceptions, please rectify that") 

            else:
                print("The value without any exception -", self.value)


if __name__ == '__main__':
    myobj = Vehicle('Tesla', 2023, 'electric')
    myobj.get_value()
