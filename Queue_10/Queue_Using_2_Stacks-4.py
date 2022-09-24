class QueueUsingTwoStacks:
    def __init__(self):
        self.__s1 = []
        self.__s2 = []

    def enqueue(self,ele):
        while(len(self.__s1) != 0):
            ele1 = self.__s1.pop()
            self.__s2.append(ele1)
        self.__s1.append(ele)

        while(len(self.__s2) != 0):
            ele2 = self.__s2.pop()
            self.__s1.append(ele2)

        return 

    def dequeue(self):
        if(len(self.__s1) == 0):
            return -1
        return self.__s1.pop()                       

    def front(self):
        return self.__s1[-1]        

    def size(self):
        return len(self.__s1)

    def isEmpty(self):
        return self.size() == 0        

q = QueueUsingTwoStacks()
q.enqueue(1)
q.enqueue(5)
q.enqueue(6)
q.enqueue(8)
q.enqueue(7)

while(q.isEmpty() is False):
    print(q.front())
    q.dequeue()

