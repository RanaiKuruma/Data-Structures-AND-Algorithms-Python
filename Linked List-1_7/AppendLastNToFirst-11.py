class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def printLL(head):
    while(head is not None):
        print(head.data,end=" ")
        head = head.next
    print()

def lenght(head):
    if(head is None):
        return 0
    return 1+lenght(head.next)

def appendLastNToFirst(head, n) :

    if(n > lenght(head)):
        return None 

    # Iterating through the Linked List to reach  the steps required to append last n elements to the front of the linked list 
    curr = head 
    count = 1
    m = lenght(head) - n
    while(count < m and curr != None):
        curr = curr.next 
        count += 1

    # Iterating after m positions to append elements at the front of the LL
    newNode = curr 
    while(curr.next != None):
        curr = curr.next 

    # As soon as we reach None we assign last element of the ll as head 
    curr.next = head 

    # Shift rest of the elemenst of the ll at the front of the ll
    head = newNode.next 

    #Making the tail point towards none as N elements have been appneded at the front of the ll
    newNode.next = None  

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
head = appendLastNToFirst(head,3)
printLL(head)

