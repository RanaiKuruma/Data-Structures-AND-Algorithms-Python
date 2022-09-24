class Queue:
    def __init__(self):
        self.__arr = []
        self.__front = 0 #For deque
        self.__count = 0 #For determining size 

    def enqueue(self,ele):
        self.__arr.append(ele)         
        self.__count += 1

    def dequeue(self):
        if(self.__count == 0):
            return -1

        element = self.__arr[self.__front] 
        self.__front += 1
        self.__count -= 1
        return element 

    def front(self):
        if(self.__count == 0):
            return -1
        return self.__arr[self.__front]

    def size(self):
        return self.__count  

    def isEmpty(self):
        return self.size() == 0 

q = Queue()            
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

while(q.isEmpty() is False):
   print(q.front(),end=" ")
   q.dequeue()

# print(q.size())  
# print(q.front())




