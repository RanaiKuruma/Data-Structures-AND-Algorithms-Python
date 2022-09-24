class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

class Queue:
    def __init__(self):
        self.__head = None 
        self.__tail = None
        self.__count = 0

    def enqueue(self,ele):
        newNode = Node(ele)
        if(self.__head is None):
            self.__head = newNode 
            self.__tail = newNode 

        else:
            self.__tail.next = newNode 
            self.__tail = newNode  

        self.__count += 1
        
    def dequeue(self):
       if(self.__head == None):
           print("Queue is Empty")
           return

       data = self.__head.data 
       self.__head = self.__head.next 
       self.__count -= 1

       return data 

    def front(self):
        if(self.__head == None):
           print("Queue is Empty")
           return 
        data = self.__head.data 
        return data  

    def size(self):
        return self.__count 
        
    def isEmpty(self):
        return self.size() == 0 

q = Queue()
q.enqueue(30)
q.enqueue(15)
q.enqueue(40)
q.enqueue(60)

while(q.isEmpty() is False):
    print(q.dequeue())


