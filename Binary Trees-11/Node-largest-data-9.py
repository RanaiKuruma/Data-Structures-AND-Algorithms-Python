class BinaryTreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

def largestData(root):
    #Base Case
    if(root is None):
        return -1 # Ideally return - infinity 

    #Induction Hypothesis    
    leftLargest = largestData(root.left)   
    rightLargest = largestData(root.right)

    # largest = max(leftLargest,rightLargest,root.data)
    largest = root.data 
    if(leftLargest > largest):
        largest = leftLargest 

    if(rightLargest > largest):
        largest = rightLargest 

    return largest                     

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
ans = largestData(root)
print(ans)