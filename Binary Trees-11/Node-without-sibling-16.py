class BinaryTreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None

def printNodesWithoutSibling(root):
    #Base Case 
    if(root is None): 
        return 

    #Induction Hypothesis 
    #If the binary tree has both the children
    elif(root.left != None and root.right != None):
        printNodesWithoutSibling(root.left)
        printNodesWithoutSibling(root.right)

    #If the right child is None and left child is not none
    elif(root.left != None):
        print(root.left.data,end=" ")
        printNodesWithoutSibling(root.left)    
        
    #If the left child is None and right child is not none 
    elif(root.right != None):
        print(root.right.data)
        printNodesWithoutSibling(root.right)


#Top-Down Fashion 
# Print from left to right order 
def printTree(root):
    if(root is None):
        return 

    printTree(root.left)
    printTree(root.right)        

    return root 

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
printNodesWithoutSibling(root)
printTree(root)
