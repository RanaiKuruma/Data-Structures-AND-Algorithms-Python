class BinaryTreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

def printTreeDetailed(root):
    if(root == None):
        return 
       
    print(root.data,end=":")
    if(root.left != None):
        print("L",root.left.data,end=",")

    if(root.left != None):
        print("R",root.right.data)
    print()

    printTreeDetailed(root.left)
    printTreeDetailed(root.right)

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


#For a leaf enter -1 as left and right 
root = treeInput()
printTreeDetailed(root)
