# Error handling inc the robustness of your code 
# Prevents termination 


# Think of error handling like this
# Sample-1
# if():
#     <our logic>

# elif() Exception:
#     <Alternative Logic>


# Sample-2
# try:
#     a + b

# # Takes one exception at a time
# fail safe alternative
# except:
#     int(a) + int(b)

class Vehicle():
    def __init__(self, make, model, fuel):
        self.make = make 
        self.model = model 
        self.fuel = fuel 


    def get_value(self):
        try:
            age = 2021 - self.model
            return 1000 * (1/age)   
            
        except TypeError:
            age = 2021 - int(self.model)
            return 1000 * (1/age)  

        except ZeroDivisionError:
            age = 2021 - int(self.model)    
            return 1000 * (1)



myobj = Vehicle('Tesla', '2017', "Electric")        
print(myobj.get_value())

