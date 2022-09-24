class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def findNode(head,n):
    curr = head 
    count = 0
    while(head is not None):
        if(curr.data == n):
            return count 
        count += 1
        curr = curr.next    
    return -1

def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currData in inputList:
        if(currData == - 1):
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
print(findNode(linkedList,5))