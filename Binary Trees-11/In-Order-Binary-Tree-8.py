class BinaryTreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

def inOrder(root):
    #intse Case
    if(root is None):
        return None 

    #Induction Hypothesis 
    inOrder(root.left)
    print(root.data,end=" ")    
    inOrder(root.right)

    return root 

def treeInput():
    rootData = int(input())
    if(rootData == -1):
        return None 
    root = BinaryTreeNode(rootData)        
    leftRoot = treeInput()
    rightRoot = treeInput()

    root.left = leftRoot 
    root.right = rightRoot 

    return root 

root = treeInput()
inOrder(root)
