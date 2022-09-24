from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def get_interest(self):
        pass

class HDFC(Bank):
    def get_interest(self):
        return 8.9


myobj = HDFC()            
print(myobj.get_interest())
