class Stack:
    def __init__(self):
        self.__array = []

    def push(self,ele):
        self.__array.append(ele) 

    def pop(self):
        ele = self.__array.pop() 
        return ele 

    def top(self):
        return  self.__array[len(self.__array) - 1] 

    def size(self):
        return len(self.__array) 

    def isEmpty(self):
        if(self.size == 0):
            return 'true'
        else:
            return 'false'


s = Stack()
s.push(12)
s.push(56)
s.push(78)
s.push(90)
s.push(345)

while(s.size() != 0):
    print(s.pop(),end=" ")
# print(s.isEmpty())





