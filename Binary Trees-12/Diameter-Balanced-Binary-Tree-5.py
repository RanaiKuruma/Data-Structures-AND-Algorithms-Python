class BinaryTreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

def height(root):
    #Base Case 
    if(root == None):
        return 0 

    #Induction Hypothesis 
    leftHeight = height(root.left)
    rightHeight = height(root.right)

    h = leftHeight 
    if(rightHeight > h):
        h = rightHeight 

    heightTree = 1 + h 
    return heightTree 

def diameterOfBinaryTree(root):
    #Base Case
    if(root == None):
        return 0

    #Induction Hypothesis 
    d1 = 0 
    d2 = 0 
    d3 = 0
    
    #Nodes on both the sides of the tree 
    lh = height(root.left)
    rh = height(root.right)
    d1 = 1 + lh + rh 

    #Nodes on the left side of the tree 
    if(root.left != None):
        ld = diameterOfBinaryTree(root.left)
        d2 = 1 + ld
    #Nodes on the right side of the tree 
    if(root.right != None):
        rd = diameterOfBinaryTree(root.right)
        d3 = 1 + rd 
 
    diameter  = d1 
    if(d2 > diameter):
        diameter  = d2 

    if(d3 > diameter):
        diameter  = d3 

    return diameter 
                    
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
ans = diameterOfBinaryTree(root)
print(ans)
