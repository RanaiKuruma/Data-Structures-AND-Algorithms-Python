class BinaryTreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

def printAtDepthK(root,k):
    #Base Case 
    if(root is None):
        return 
    if(k == 0):
        print(root.data)
        return 

    #Induction Hypothesis 
    printAtDepthK(root.left,k-1)
    printAtDepthK(root.right,k-1)                    

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
ans = printAtDepthK(root,k)
print(ans)
