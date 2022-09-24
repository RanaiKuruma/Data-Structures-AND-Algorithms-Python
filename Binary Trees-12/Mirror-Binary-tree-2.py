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
        print(root.left.data,end=",")

    if(root.left != None):
        print(root.right.data)
    print()

    printTree(root.left)
    printTree(root.right)

def mirrorBinaryTree(root):
    #Base Case 
    if(root == None):
        return 

    #Induction Hypothesis 
    mirrorBinaryTree(root.left)
    mirrorBinaryTree(root.right)

    temp = root.left 
    root.left = root.right 
    root.right = temp 

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
print("Original Tree:")
printTree(root)
print()
print("Mirror Tree:")
mirrorBinaryTree(root)
printTree(root)
