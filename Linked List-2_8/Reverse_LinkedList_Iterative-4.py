class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

def printLL(head):
    while(head is not None):
        print(head.data,end=" ")
        head = head.next
    print()

def reverseIterative(head):
    curr = head 
    prev = None 
    while(curr is not None):
        next = curr.next #Storing the present reference 
        curr.next = prev #Storing the previous reference 
        prev = curr # Reversing a linked list
        curr = next # Moving forward through the linked list without losing the references
        
    head = prev 
    return head
    
def takeInput():
    linkedList = [int(ele) for ele in input().split()]
    head = None 
    tail = None 
    for currData in linkedList:
        if(currData == -1):
            break
        newNode = Node(currData)
        
        if(head is None ):
            head = newNode 
            tail = newNode 

        else:
            tail.next = newNode 
            tail = newNode 

    return head             

head = takeInput()
head = reverseIterative(head)
printLL(head)

