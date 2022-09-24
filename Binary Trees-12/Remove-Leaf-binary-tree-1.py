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

    if(root.left != None):
        print("R",root.right.data)
    print()

    printTree(root.left)
    printTree(root.right)

def removeLeaves(root):
    #Base Case 
    if(root is None):
        return 

    if(root.left == None and root.right ==  None):  
        return None 

    root.left = removeLeaves(root.left)  
    root.right = removeLeaves(root.right)            

    return root 

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


 
root = treeInput()
ans = removeLeaves(root)
printTree(ans)

