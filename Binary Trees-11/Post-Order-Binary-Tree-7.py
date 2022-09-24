class BinaryTreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

def postOrder(root):
    #Base Case
    if(root is None):
        return None 

    #Induction Hypothesis 
    postOrder(root.left)
    postOrder(root.right)
    print(root.data,end=" ")    

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
postOrder(root)
