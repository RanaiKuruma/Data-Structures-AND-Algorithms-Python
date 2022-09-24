class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def reverse(head):
    if(head is None):
        return 
    reverse(head.next)
    print(head.data,end=" ")    

def isPalindrome(head) :
    # use two-pointers to locate the mid-point of linked list
		
        slow, fast = head, head
        
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
		
		# skip central node if length of linked list is odd number.
        if fast:
            slow = slow.next
        
        # Reverse the linkage of right half of linked list
        tail = reverse( slow )
        
        
        # Accept if left half sequence == right half sequence
        # Reject, otherwise
        while tail:
            
            if tail.data != head.data:
                return 'false'
            
            head, tail = head.next, tail.next
        
        return 'true'

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
print(isPalindrome(linkedList)) 

