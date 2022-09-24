
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

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

def numNodes(root):
    if(root is None):
        return 0 

    leftNode = numNodes(root.left)    
    rightNode = numNodes(root.right)

    return  1 + leftNode + rightNode
    
root = treeInput()
print(numNodes(root))
