class BinaryTreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

def treeInput():
    rootData = int(input())
    #Base Case 
    if(rootData == -1):
        return None 

    root = BinaryTreeNode(rootData)
    leftTree = treeInput()
    rightTree = treeInput()

    root.left = leftTree 
    root.right = rightTree 

    return root 


def nodeToRootPath(root,s):
    if(root == None):
        return None 
    if(root.data == s):
        l = []            
        l.append(root.data)
        return l 

    leftTree = nodeToRootPath(root.left,s)        
    rightTree = nodeToRootPath(root.right,s)

    if(leftTree != None):
        leftTree.append(root.data)
        return leftTree 

    if(rightTree != None):
        rightTree.append(root.data)        
        return rightTree 

    else:
        return None 


root = treeInput()
# printTree(root)
ans = nodeToRootPath(root,5)
print(ans)

