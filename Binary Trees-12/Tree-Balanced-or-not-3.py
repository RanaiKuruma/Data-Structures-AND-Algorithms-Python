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

def height(root):
    if(root == None):
        return 0 

    return 1 + max(height(root.left),height(root.right))

def isBalanced(root):
    #Base Case 
    if(root == None):
        return True 

    lh = height(root.left)
    rh = height(root.right)

    if(lh - rh > 1 or rh - lh > 1):
        return False 

    isLeftBalanced = isBalanced(root.left) 

    isRightBalanced = isBalanced(root.right)   

    if(isLeftBalanced and isRightBalanced):
        return True 

    else:
        return False       
          
root = treeInput()
print(isBalanced(root))
