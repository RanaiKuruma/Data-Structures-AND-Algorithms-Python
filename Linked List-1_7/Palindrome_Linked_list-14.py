class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def take_input():
    input_list = [int(ele) for ele in input().split()]
    head = None 
    tail = None 

    for curr_data in input_list:
        if(curr_data == -1):
            break 

        new_node = Node(curr_data)
        if(head is None):
            head = new_node 
            tail = new_node 
        else:
            tail.next = new_node
            tail = new_node 

    return head 

def reverse_LL(head):
    prev = None 
    curr = head 

    while(curr is not None):
        temp = curr.next 
        curr.next = prev 
        prev = curr 
        curr = temp 

    return prev 

def isPalindrome(head):
    slow = head 
    fast = head 

    while(fast and fast.next):
        slow = slow.next 
        fast = fast.next.next 
    
    if(fast):
        slow = slow.next 
    
    tail = reverse_LL(slow)
    while(tail):
        if(tail.data != head.data):
            return False 
        head = head.next 
        tail = tail.next 
    return True 

head = take_input()
ans = isPalindrome(head)
if(ans):
    print('true')
else:
    print('false')

