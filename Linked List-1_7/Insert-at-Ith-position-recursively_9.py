class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def printLL(head):
    while(head is not None):
        print(head.data,end=" ")
        head = head.next
    print()
        
def lenght(head):

    if (head is None):
        return 0
    return 1 + lenght(head.next)    

def insertAtI(head,i,data):

    if(i < 0 or i > lenght(head)):
        return head

    # Base Case
    if(i == 0):
        newNode = Node(data)                 
        newNode.next = head
        return newNode

    if(head is None):
        return None

    # Induction Hypothesis
    smallHead = insertAtI(head.next,i-1,data)
    head.next = smallHead

    return head 


def takeInput():
    linkedList = [int(ele) for ele in input().split()]    
    head = None 
    tail = None

    for currData in linkedList:
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


head = takeInput()
head = insertAtI(head,3,7)
printLL(head)

