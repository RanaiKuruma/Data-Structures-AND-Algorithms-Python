class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def printReverse(head):
    if(head  is None):
        return 

    printReverse(head.next)
    print(head.data,end=" ")    

def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None 
    tail = None 

    for currData in inputList:
        if(currData == -1):
            break

        newNode = Node(currData)

        if(head is None):
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode

    return head 

linkedList = takeInput()    
printReverse(linkedList)
