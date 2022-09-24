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

def sumOfAllNodes(root):
    if(root == None):
        return 
    
    sum = 0 
    for child in root.children:
        sum += sumOfAllNodes(child)

    finalSum = root.data + sum 
    return finalSum 

root = treeInput()
ans = sumOfAllNodes(root)
print(ans)




