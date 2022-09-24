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

def getHeightAndBalanced(root):
    #Base Case 
    if(root == None):
        return 0,True 

    #Induction Hypothesis 
    lh,isLeftBalanced = getHeightAndBalanced(root.left)
    rh,isRightBalanced = getHeightAndBalanced(root.right)

    h = 1 + max(lh,rh)          

    if(lh - rh > 1 or rh - lh > 1):
        return h,False 

    if(isLeftBalanced and isRightBalanced):
        return h,True 
    else:
        return h,False 


#If you want to display whether the tree is balanced or not 
def isBalanced(root):
    h,isTreeBalanced = getHeightAndBalanced(root)
    return isTreeBalanced

root = treeInput()
# print(getHeightAndBalanced(root))
print(isBalanced(root))

