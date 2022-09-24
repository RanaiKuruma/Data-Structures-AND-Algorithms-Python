# Whenever writing code on codezen write it with comments
from queue import Queue 
def reverseQueue(inputqueue:Queue):
    #Base Case 
    if(inputqueue.empty()):
        return 

    #Induction Hypothesis 
    item = inputqueue.queue[0]
    inputqueue.get()         

    reverseQueue(inputqueue)
    inputqueue.put(item)

def printQueue(queue:Queue):
    while(not queue.empty()):
        print(queue.queue[0],end=" ")
        queue.get()
    print()        

q = Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)
q.put(10)

reverseQueue(q)
printQueue(q)



