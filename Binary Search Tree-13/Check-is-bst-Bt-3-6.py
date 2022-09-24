
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

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

def isBST3(root,min_range,max_range):
    if root==None:
        return True
    if root.data<min_range or root.data>max_range:
        return False
    
    isLeftWithinConstraints=isBST3(root.left,min_range,root.data-1)
    isRightWithinConstraints=isBST3(root.right,root.data,max_range)
    
    return isLeftWithinConstraints and isRightWithinConstraints

root = treeInput()
ans = isBST3(root,-1000,1000)
print(ans)
