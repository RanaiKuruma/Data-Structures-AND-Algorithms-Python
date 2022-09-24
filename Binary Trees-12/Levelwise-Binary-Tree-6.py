import queue 
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

def printTree(root):
    if(root == None):
        return 
       
    print(root.data,end=":")
    if(root.left != None):
        print("L",root.left.data,end=",")

    if(root.right != None):
        print("R",root.right.data)
    print()

    printTree(root.left)
    printTree(root.right)
 
def takeLevelWiseTreeInput():
    rootData = int(input(f"Enter Root :"))
    if(rootData == -1):
        return None 
    root = BinaryTreeNode(rootData)
            
    q = queue.Queue()
    q.put(root)
    while(not(q.empty())):
        current_node = q.get()

        #Taking input for the left child 
        leftChildData = int(input(f"Enter Left child of {current_node.data} : "))
        
        #Creating the left child 
        if(leftChildData != -1):
            leftChild = BinaryTreeNode(leftChildData)
            current_node.left = leftChild
            q.put(leftChild)

        #Taking input for the right child 
        rightChildData = int(input(f"Enter Right child of {current_node.data} : "))
        
        #Creating the right child 
        if(rightChildData != -1):
            rightChild = BinaryTreeNode(rightChildData)
            current_node.right = rightChild
            q.put(rightChild)

    return root 

root = takeLevelWiseTreeInput()
print( )
printTree(root)
