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

def numNodes(root):
    if(root == None):
        return 0 
        
    count = 1 
    #The for loop is used for iterating through the sub-generic tree only 
    for child in root.children:
        count += numNodes(child)
    return count        

root = treeInput()            
ans = numNodes(root)
print(ans)



