class BinaryTreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

def countNodesGreaterThanX(root,x):
    if(root is None):
        return  0

    leftTree = countNodesGreaterThanX(root.left,x)
    rightTree = countNodesGreaterThanX(root.right,x)

    if(root.data > x):
        return 1 + leftTree + rightTree 

    return leftTree + rightTree 
            
def treeInput():
    rootData = int(input())
    if(rootData == -1):
        return 

    root = BinaryTreeNode(rootData)        
    leftTree = treeInput()
    rightTree = treeInput()

    root.left = leftTree
    root.right = rightTree

    return root 

root = treeInput()
x = int(input("x:"))
ans = countNodesGreaterThanX(root,x)
print(ans)
