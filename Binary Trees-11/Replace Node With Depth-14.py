class BinaryTreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

def changeToDepthTree(root,depth=0):
    if(root is None):
        return 

    root.data = depth 
    changeToDepthTree(root.left,depth+ 1)   
    changeToDepthTree(root.right,depth+ 1)

#In order fashion
def printTree(root):
    if(root is None):
        return 

    printTree(root.left)
    print(root.data,end=" ") 
    printTree(root.right)       

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
changeToDepthTree(root)
printTree(root)
