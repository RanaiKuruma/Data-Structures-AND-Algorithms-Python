class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def printLL(head):
    while(head is not None):
        print(head.data,end=" ")
        head = head.next
    print()    

def mergeTwoSortedLinkedList(head1, head2):
    #Creating a dummy node and intialising finalHead with finalTail
    finalHead = Node(0)               
    finalTail = finalHead   

    # Comparing and Iterating through the linked lists to compare elements of the 2 linked lists
    while head1 != None and head2 != None:  
        if head1.data < head2.data:
            finalTail.next = head1
            finalTail = finalTail.next
            head1 = head1.next

        else:
            finalTail.next = head2
            finalTail = finalTail.next
            head2 = head2.next

    # Making connections for linked list - 1        
    while head1 is not None:
        finalTail.next = head1
        finalTail = finalTail.next
        head1 = head1.next
        
    # Making connections for linked list - 2
    while head2 is not None:
        finalTail.next = head2
        finalTail = finalTail.next    
        head2 = head2.next
    
    return finalHead.next  # Because you need to ignore the dummy node 

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

head1 = takeInput()
head2 = takeInput()
a = mergeTwoSortedLinkedList(head1,head2)
printLL(a)
