class BinaryTreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

def isNodePresent(root,x):
    #Base Case 
    if(root is None):
        return 

    if(root.data == x):
        return root.data 

    #Induction Hypothesis 
    leftTree = isNodePresent(root.left,x)
    rightTree = isNodePresent(root.right,x) 
    
    if(leftTree):
        return True 

    if(rightTree):
        return rightTree 

    else:
        return False     


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
x = int(input("x:"))
ans = isNodePresent(root,x)

if(ans):
    print('true')
else:
    print('false')    

