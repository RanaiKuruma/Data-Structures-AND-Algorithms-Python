class BinaryTreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

def printAtDepthK(root,k,d=0):
    #Base Case 
    if(root is None):
        return 
    if(k == d):
         print(root.data)
         return 

    #Induction Hypothesis 
    printAtDepthK(root.left,k,d+1)        
    printAtDepthK(root.right,k,d+1)

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
k = int(input("k:"))
d = int(input("d:"))
ans = printAtDepthK(root,k)
print(ans)
