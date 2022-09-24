class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

# Motive is to get the head of the linked list i.e if you know the head of the linked list you can take input

# If input is there return reference of the first node

# Head can't be changed in linked list
def takeInput():

    inputList = [int(ele) for ele in input().split()]
    head = None

    # Iterate to build connetions through the list
    for currData in inputList:
        if currData == -1:
            break
        
        # Create a node
        newNode = Node(currData)

        # No new node has been created
        if head is None:
            head = newNode

        else:
            curr = head
            while( curr.next is not None):
                curr = curr.next

            curr.next = newNode    
    return head

head = takeInput()