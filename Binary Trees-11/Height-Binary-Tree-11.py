class BinaryTreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

def height(root):
    #Base Case
    if(root is None):
        return 0 

    #Induction Hypothesis 
    leftHeight = height(root.left)
    rightHeight = height(root.right)

    maxHeight = leftHeight 
    if(rightHeight > maxHeight):
        maxHeight = rightHeight 

    finalHeight = 1 + maxHeight 

    return finalHeight     
def treeInput():
    rootData = int(input())
    if(rootData == -1):
        return 

    root = BinaryTreeNode(rootData)        
    leftTree = treeInput()
    rightTree = treeInput()

    root.left = leftTree
    root.right = rightTree

    return root 

root = treeInput()
ans = height(root)
print(ans)

