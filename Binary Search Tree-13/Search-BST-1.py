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

def searchInBst(root,x):
    #Base Case
    if(root == None):
        return False 

    #Induction Hypothesis
    if(root.data == x):
        return True

    if(root.data > x):
        return searchInBst(root.left,x)                

    if(root.data < x):
        return searchInBst(root.right,x)        

root = treeInput()
x = int(input("X:"))
ans = searchInBst(root,x)
if(ans):
    print('true')
else:
    print('false')    

