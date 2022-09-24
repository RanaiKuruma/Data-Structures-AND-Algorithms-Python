class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def constructBST(lst):
    #Base Case
    n = len(lst)
    # if(n == 0):
    #     return None 

    if(not(lst)):
        return None 

    #Induction Hypothesis
    mid = (n) // 2
    root = BinaryTreeNode(lst[mid])        

    leftArr = lst[0:mid]
    rightArr = lst[mid+1:]

    leftTree = constructBST(leftArr)
    rightTree = constructBST(rightArr)

    root.left = leftTree 
    root.right = rightTree 

    return root 

def printTree(root):
    if root==None:
        return
    print(root.data, end=' ')
    printTree(root.left)
    printTree(root.right)

arr = [int(i) for i in input().split()]
# arr = [1,2,3,4,5,6,7]
root = constructBST(arr)
printTree(root)
