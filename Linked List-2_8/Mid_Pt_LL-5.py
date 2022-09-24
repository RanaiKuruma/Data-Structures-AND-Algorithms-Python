class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def printLL(head):
    while(head is not None):
        print(head.data,end=" ")
        head = head.next
    print()

def midPoint(head):
    if(head is None):
        return None 

    slow = head 
    fast = head 
    # fast.next.next is for odd lenght and fast.next is for even lenght
    # If lenght is odd then fast.next.next will reach the last node or tail
    # If lenght is even then fast.next will reach the second last node 

    # Iteration Condition which satisfies both the lenght of the node i.e odd or even 
    while(fast.next != None and fast.next.next != None):
        if(fast.data == -1):
            break 

        slow = slow.next 
        fast = fast.next.next  
    return slow.data 

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
head = midPoint(head)
print(head)

