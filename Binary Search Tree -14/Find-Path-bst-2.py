
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

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

def findPathBST(root,data):
    #Base 
    if(root == None):
        return None 
    if(root.data == data):
        l = []        
        l.append(root.data)
        return l 

    #Induction Hypothesis 
    leftTree = findPathBST(root.left,data)        
    rightTree = findPathBST(root.right,data)

    #Traversing on the left side 
    if(root.data >= data and root.left != None):
        leftTree.append(root.data)
        return leftTree  

    #Traversing on the right side 
    if(root.data < data and root.right != None):
        rightTree.append(root.data)        
        return rightTree  

    #Returning an empty list if k is not found on root,leftTree or rightTree
    if(root.data != k):
        return None 

root = treeInput()
k = int(input("k:"))
ans = findPathBST(root,k)
print(ans)