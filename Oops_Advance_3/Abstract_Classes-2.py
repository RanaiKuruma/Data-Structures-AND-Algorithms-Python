from abc import ABC, abstractmethod

class TextReaderAbstract(ABC):
    def __init__(self, path, filename):
        self.path = path
        self.filename = filename

    @abstractmethod     # This is just an interface or 'RULE'
    def get_path(self):
        pass


class TextReader(TextReaderAbstract):    
    # Even if you don't give the init it will be fine cuz you have already defined it in the abstract class
    # You can overwrite the init if you want

    def get_path(self):
        return self.path

    def get_filename(self):
        return self.filename


myobj = TextReader('/user/download', 'sample.txt')
# print(myobj.get_path())

# print(myobj.get_filename())


