class BinaryTreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

def binaryTreeSum(root):
    if(root == None):
        return 0 

    lSum = 0
    rSum = 0 

    if(root.left != None):
        lSum += binaryTreeSum(root.left) 

    if(root.right != None):
        rSum += binaryTreeSum(root.right)               

    sum = root.data + lSum + rSum 

    return sum 

def treeInput():
    rootData = int(input())
    if(rootData == -1):
        return None 
    root = BinaryTreeNode(rootData)        
    leftRoot = treeInput()
    rightRoot = treeInput()

    root.left = leftRoot 
    root.right = rightRoot 

    return root         

root = treeInput()
ans = binaryTreeSum(root)
print(ans)
