class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def printIthNode(head,i):
    count = 0
    while head is not None:
        if count == i:
            print(head.data)
        head = head.next
        count += 1

def takeInput():
    inputList = [int(ele) for ele in input().split()]

    head = None
    tail = None

    for currData in inputList:
        if currData == -1:
            break

        newNode = Node(currData)

        if head == None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode

    return head

head = takeInput()                
printIthNode(head,5)

            