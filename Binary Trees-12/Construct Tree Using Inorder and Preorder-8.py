class BinaryTree:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

def printTree(root):
    if(root is None):
        return 

    print(root.data,end=":")        
    if(root.left is not None):
        print("L",root.left.data,end=",")

    if(root.right is not None):
        print("R",root.right.data)        
    print()
    
    printTree(root.left)        
    printTree(root.right)

def buildTree(preOrder,inOrder):
    if(len(preOrder) == 0):
        return None 

    rootData = preOrder[0]        
    root = BinaryTree(rootData)

    #Finding index of root in inOrder 
    rootIndex = -1 
    for i in range(len(inOrder)):
        if(inOrder[i] == root.data):
            rootIndex = i 
            break 

    #Finding left and right subtree of inOrder 
    leftInOrderSubTree = inOrder[0:rootIndex]            
    rightInOrderSubTree = inOrder[rootIndex:]

    #Finding lenght of a small section of left subtree (in order) to get preorder's left and right 
    n = len(leftInOrderSubTree)

    #Finding left and right subtree of preOrder 
    leftPreOrderSubTree = preOrder[1:n+1]
    rightPreOrderSubTree = preOrder[n+1:]

    #Finding the left and right subtree of the whole tree 
    leftTree = buildTree(leftPreOrderSubTree,leftInOrderSubTree)
    rightTree = buildTree(rightPreOrderSubTree,rightInOrderSubTree)

    root.left = leftTree 
    root.right = rightTree 

    return root 

preOrder = [int(i) for i in input().split()]
inOrder = [int(j) for j in input().split()]
print(" ")
root = buildTree(preOrder,inOrder)
printTree(root)
