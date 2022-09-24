class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def printLL(head):
    while(head is not None):
        print(head.data,end=" ")
        head = head.next
    print()
    
def reverse2(head):
    if(head is None or head.next is None):
        return head,head 
        
    smallHead,smallTail = reverse2(head.next)
    smallTail.next = head 
    head.next = None 
    return smallHead,head 

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
head,tail = reverse2(head)
printLL(head)