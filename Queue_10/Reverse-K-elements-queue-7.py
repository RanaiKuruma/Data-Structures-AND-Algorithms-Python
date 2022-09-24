from queue import Queue
def reverseKElements(inputQueue:Queue,k):
    if(inputQueue.empty()):
        return  

    #Put first k elements in a stack
    s = []        
    for i in range(k):
        s.append(inputQueue.queue[0])
        inputQueue.get()

    #enqueue contents of the stack at the back of queue
    while(len(s) != 0):
        inputQueue.put(s[-1])
        s.pop()    

    #Remove the remaining elements and enqueue them at the end of the queue 
    for i in range(inputQueue.qsize() - k):
        inputQueue.put(inputQueue.queue[0])
        inputQueue.get()        

def printQueue(queue:Queue):
    while(not queue.empty()):
        print(queue.queue[0],end=" ")
        queue.get()
    print()        

q = Queue()
q.put(11)
q.put(22)
q.put(33)
q.put(44)
q.put(55)
q.put(66)
q.put(77)

k = int(input())
reverseKElements(q,k)
printQueue(q)
