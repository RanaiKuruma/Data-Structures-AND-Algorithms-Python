class TreeNode:
    def __init__(self,data):
        self.data = data 
        self.children = []
 
def printTree(root):
    if(root == None):
        return 

    print(root.data,":",end=" ")
    for child in root.children:
        print(child.data,",",end=" ") 

    print( )

    for child in root.children:
        printTree(child)        

def treeInput():
    print("Enter root data:")
    rootData = int(input())
    if(rootData == -1):
        return 

    root = TreeNode(rootData)        

    print("Enter number of children for ", rootData)
    childrenCount= int(input())
    for i in range(childrenCount):
        child = treeInput()
        root.children.append(child)
    return root 

root = treeInput()            
printTree(root)


