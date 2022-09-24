class BinaryTreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

def numLeafNode(root):
    if(root is None):
        return 0 
        
    if(root.left == None and root.right == None):
        return 1 

    leftLeaf = numLeafNode(root.left) 
    rightLeaf = numLeafNode(root.right)   

    leafNode = leftLeaf + rightLeaf 

    return leafNode 

def treeInput():
    rootData = int(input())        
    if(rootData == -1):
        return 

    root = BinaryTreeNode(rootData)        
    rootLeft = treeInput()
    rootRight = treeInput()

    root.left = rootLeft
    root.right = rootRight

    return root 

root = treeInput()
ans = numLeafNode(root)
print(ans)
