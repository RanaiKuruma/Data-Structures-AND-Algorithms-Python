class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

class Stack:
    def __init__(self):
        self.__head = None
        self.__count = 0

    def push(self,element):
        newNode = Node(element) 
        newNode.next = self.__head 
        self.__head = newNode
        self.__count += 1

    def pop(self):
        if(self.isEmpty() is True):
            print("Empty Stack")
            return 

        data = self.__head.data    
        self.__head = self.__head.next  
        self.__count -= 1  

        return data 

    def top(self):
        if(self.isEmpty() is True):
            print("Empty Stack")
            return 
        data = self.__head.data   
        return data 
        
    def size(self):
        return self.__count 

    def isEmpty(self):
        return self.size() == 0

    def displayStack(self):
        curr = self.__head
        if self.isEmpty():
            print("Stack Underflow")
        else:
            while(curr != None):
                print(curr.data,end = " ")
                curr = curr.next
            return    

s = Stack()
s.push(11)
s.push(23)
s.push(45)
s.push(67)


s.displayStack()
# print(s.top())
# print(s.size())