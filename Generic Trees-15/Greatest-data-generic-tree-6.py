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

def maxDataNode(root):
    if(root == None):
        return 

    largestData = root.data
    for child in root.children:
        if(largestData < maxDataNode(child)):
            largestData = maxDataNode(child)                
    return largestData 

root = treeInput()
ans = maxDataNode(root)
print(ans)
