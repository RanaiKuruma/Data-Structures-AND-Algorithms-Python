
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 


def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()
    


def lenght(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count 


def insertAtI(head,i,data):
    if i < 0 or i > lenght(head):
        return head

    prev = None
    curr = head
    count = 0
    while(count < i):
        prev = curr
        curr = curr.next
        count += 1    

    newNode = Node(data)
    if(prev is  None):
        head = newNode

    else:
        prev.next = newNode
    newNode.next = curr

    return head


def takeInput():

    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None

    for currData in inputList:
        if currData == -1:
            break
        
        newNode = Node(currData)

        if head is None:
            head = newNode
            tail = newNode
            
        else:
            tail.next = newNode
            tail = newNode 

    return head

head = takeInput()
head = insertAtI(head,2,6)
printLL(head)


