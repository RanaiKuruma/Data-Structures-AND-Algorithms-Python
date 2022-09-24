class TreeNode:
    def __init__(self,data):
        self.data = data 
        self.children = []
 
def treeInput():
    print("Enter root data:")
    rootData = int(input())
    if(rootData == -1):
        return 

    root = TreeNode(rootData)        

    print("Enter number of children for:", rootData)
    childrenCount= int(input())
    for i in range(childrenCount):
        child = treeInput()
        root.children.append(child)
    return root

def heightOfGenericTree(root):
    h = 0 
    for child in root.children:
        if(h < heightOfGenericTree(child)):
            h = heightOfGenericTree(child)
    height = 1 + h 
    return height 

root = treeInput()    
ans = heightOfGenericTree(root)
print(ans)
