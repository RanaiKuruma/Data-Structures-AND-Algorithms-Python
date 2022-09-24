class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLL(head):
    while(head is not None):
        print(head.data,end=" ")
        head = head.next
    print()

def midPointLL(head):
    slow = head 
    fast = head 
    while(fast.next != None and fast.next.next != None):
        if(fast.data == -1):
            break 
        slow = slow.next 
        fast = fast.next.next 

    return slow 

def mergeLL(head1,head2):
    fh = Node(0)
    ft = fh

    while(head1 != None and head2 != None):
        if(head1.data < head2.data):
            ft.next = head1
            ft = ft.next 
            head1 = head1.next 

        else:
            ft.next = head2
            ft = ft.next 
            head2 = head2.next  

    while(head1 is not None):
        ft.next = head1
        ft = ft.next 
        head1 = head1.next 

    while(head2 is not None):
        ft.next = head2
        ft = ft.next 
        head2 = head2.next 

    return fh.next 

def mergeSort(head):
    if(head.next is  None):
        return head 

    #Splitting the linked list into 2 halves
    mid = midPointLL(head)
    h1 = head 
    temp = head 
    while(temp is not mid):
        temp = temp.next 
    h2 = temp.next 
    temp.next = None 

    #Making an recursive call to sort the 2 halves of the linked list 
    h1 = mergeSort(h1)        
    h2 = mergeSort(h2)

    return mergeLL(h1,h2)

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
head = mergeSort(head)
printLL(head)

