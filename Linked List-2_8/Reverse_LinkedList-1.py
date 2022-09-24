class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def printLL(head):
    while(head is not None):
        print(head.data,end=" ")
        head = head.next
    print()
    
def reverse1(head) :

    #Base Case
    if(head is None or head.next is None):
        return head 

    # Induction Hypothesis
    smallHead = reverse1(head.next)
    curr = smallHead
    while(curr.next is not None):
        curr = curr.next
    curr.next = head 
    head.next = None

    return smallHead 

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
head = reverse1(head)
printLL(head)

