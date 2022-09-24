
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

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

def minTree(root):
    if(root == None):
        return 100000

    leftMin = minTree(root.left)
    rightMin = minTree(root.right )    

    return min(leftMin,rightMin,root.data)

def maxTree(root):
    if(root == None):
        return -10000

    leftMax = maxTree(root.left)  
    rightMax = maxTree(root.right)  
    
    return max(leftMax,rightMax,root.data)

def isBST(root):
    if(root == None):
        return True 

    leftMax = maxTree(root.left)        
    rightMin = minTree(root.right)

    if(root.data > rightMin or root.data <= leftMax):
        return False 

    isLeftBst = isBST(root.left)        
    isRightBst = isBST(root.right)

    return isLeftBst and isRightBst

root = treeInput()
ans = isBST(root)
if(ans):
    print("true")

else:
    print("false")    
