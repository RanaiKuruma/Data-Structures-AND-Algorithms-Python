class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def printLL(head):
    while(head is not None):
        print(head.data,end=" ")
        head = head.next
    print()    

def removeDuplicate(head):
    temp = head 
    if(temp is None):
        return 

    while(temp.next != None):
        if(temp.data == temp.next.data):
            new = temp.next.next
            temp.next = None
            temp.next = new

        # To make connections when consecutive elements are not equal
        else:
            temp = temp.next

    return head 

def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None 
    tail = None 

    for currData in inputList:
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

linkedList = takeInput()
linkedList = removeDuplicate(linkedList)
printLL(linkedList)

