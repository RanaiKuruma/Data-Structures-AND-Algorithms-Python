
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def printLL(head):
    count = 0

    while(head is not None):
        head = head.next
        count += 1

    return count 


def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None 

    for currData in inputList:
        if(currData == -1):
            break

        newNode = Node(currData)

        if (head is None):
            head = newNode 
            tail = newNode

        else:
            # curr = head
            # while(curr.next is not None):
            #     curr = curr.next
                
            # curr.next = newNode
            tail.next = newNode
            tail = newNode

    return head




head = takeInput()
print(printLL(head))
