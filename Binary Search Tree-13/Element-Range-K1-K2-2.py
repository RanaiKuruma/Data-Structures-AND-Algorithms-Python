
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

def printTree(root):
    if(root == None):
        return 

    print(root.data,end=" ")        
    printTree(root.left)
    printTree(root.right)

    return root 

def elementsInRangeK1K2(root,k1,k2):
    #Base Case 
    if(root == None):
        return 

    #Induction Hypothesis
    if(root.data > k2):
        elementsInRangeK1K2(root.left,k1,k2)        

    if(root.data < k1):
        elementsInRangeK1K2(root.right,k1,k2)        

    if(root.data >= k1 and root.data <= k2):
        elementsInRangeK1K2(root.left,k1,k2)
        print(root.data,end=" ")        
        elementsInRangeK1K2(root.right,k1,k2)


root = treeInput()
k1 = int(input("K1:"))
k2 = int(input("K2:"))
ans = elementsInRangeK1K2(root,k1,k2)
printTree(ans)

