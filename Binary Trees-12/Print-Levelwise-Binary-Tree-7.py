import queue    
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

def levelWisePrintTree(root):
    if(root == None):
        return None 

    #Creating a queue 
    q = queue.Queue() 
    q.put(root)        

    #Iterating through the queue 
    while(not(q.empty())):
        current_node = q.get()
        print(current_node.data,end=":")

        if(current_node.left != None):
            print("L",current_node.left.data,end=",")
            q.put(current_node.left)

        if(current_node.right != None):
            print("R",current_node.right.data)
            q.put(current_node.right)
        print()
 

    #Or  
    
    # if(root == None):
    #     return None 
    
    # #Creating the queue 
    # q = queue.Queue()
    # q.put(root)
    
    # while(not(q.empty())):
    #     curr_node = q.get()
    #     print(curr_node.data,end=":")
        
    #     #Printing the left side of the binary tree 
    #     if(curr_node.left != None):
    #         print("L:",end="")
    #         print(curr_node.left.data,end=",")
    #         q.put(curr_node.left)
            
    #     else:
    #         print("L:-1",end=",")
            
    #     #Printing the right side of the binary tree 
    #     if(curr_node.right != None):
    #         print("R:",end="")
    #         print(curr_node.right.data,end="")
    #         q.put(curr_node.right)
            
    #     else:
    #         print("R:-1",end="")
            
    #     print() 

def takeLevelWiseTreeInput():
    q = queue.Queue()
    print("Enter Root")
    rootData = int(input())
    if(rootData == -1):
        return None 
    root = BinaryTreeNode(rootData)        

    q.put(root)
    while(not(q.empty())):
        current_node = q.get()
        print("Enter Left child of :",current_node.data)
        leftChildData = int(input())
        if(leftChildData != -1):
            leftChild = BinaryTreeNode(leftChildData)
            current_node.left = leftChild
            q.put(leftChild)

        print("Enter Right child of :",current_node.data)
        rightChildData = int(input())
        if(rightChildData != -1):
            rightChild = BinaryTreeNode(rightChildData)
            current_node.right = rightChild
            q.put(rightChild)

    return root 

root = takeLevelWiseTreeInput()
levelWisePrintTree(root)

    