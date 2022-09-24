
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

def isBST2(root):
    #Base Case
    if(root == None):
        return 10000,-10000,True

    #Induction Hypothesis 
    leftMin,leftMax,isLeftBst = isBST2(root.left)        
    rightMin,rightMax,isRightBst = isBST2(root.right)

    #Determining the max and min  of the left and the right tree 
    overallMin = min(leftMin,rightMin,root.data)
    overallMax = max(leftMax,rightMax,root.data)

    #Creating a flag to determine whether the overall tree is bst or not 
    isTreeBst = True 

    #If condition is False 
    if(root.data <= leftMax or root.data > rightMin):
        isTreeBst = False 

    if(not(isLeftBst) or not(isRightBst)):
        isTreeBst = False 

    #Returning the overall min and max with whether the bt is bst or not 
    return overallMin,overallMax,isTreeBst 



root = treeInput()
ans = isBST2(root)
print(ans)
