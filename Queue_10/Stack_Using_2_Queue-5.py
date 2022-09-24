from queue import Queue 
class Stack:
    def __init__(self):
        self.q1 = Queue() 
        self.q2 = Queue()
        self.count = 0

    def push(self,ele):
        self.q1.put(ele)
        self.count += 1

    def pop(self):
        while(self.q1.qsize() != 1):
            ele1 = self.q1.get()
            self.q2.put(ele1)

        lastEle = self.q1.get()  
        self.count -= 1

        while(self.q2.qsize() != 0):
            ele2 = self.q2.get()
            self.q1.put(ele2)

    def top(self):
        while(self.q1.qsize() != 1):
            ele1 = self.q1.get()
            self.q2.put(ele1)

        top = self.q1.queue[0]
        self.q2.put(ele1)

        while(self.q2.qsize() != 0):
            ele2 = self.q2.get()
            self.q1.put(ele2)

        return top 

    def size(self):
        return self.count 

    def isEmpty(self):
        return self.size() == 0


s = Stack()
n = int(input())
for i in range(1,n+1):
    s.push(i)

while(s.isEmpty() is False):
    print(s.top())
    s.pop()

# qsize - for calculating size of queue(inbuilt)