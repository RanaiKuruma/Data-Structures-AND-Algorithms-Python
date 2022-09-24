
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

def treeInput():
    rootData = int(input())
    if(rootData == -1):
        return 

    root = BinaryTreeNode(rootData)        
    rootLeft = treeInput()
    rootRight = treeInput()
    
    root.left = rootLeft 
    root.right = rootRight 

    return root 
                        
class Height:
    def __init__(self):
        self.h = 0

def diameterOpt(root, height):
 
    # to store height of left and right subtree
    lh = Height()
    rh = Height()
 
    # base condition- when binary tree is empty
    if root is None:
        height.h = 0
        return 0
 
     
    # ldiameter --> diameter of left subtree
    # rdiameter  --> diameter of right subtree
     
    # height of left subtree and right subtree is obtained from lh and rh
    # and returned value of function is stored in ldiameter and rdiameter
     
    ldiameter = diameterOpt(root.left, lh)
    rdiameter = diameterOpt(root.right, rh)
 
    # height of tree will be max of left subtree
    # height and right subtree height plus1
 
    height.h = max(lh.h, rh.h) + 1
 
    # return maximum of the following
    # 1)left diameter
    # 2)right diameter
    # 3)left height + right height + 1
    return max(lh.h + rh.h + 1, max(ldiameter, rdiameter))
 
# function to calculate diameter of binary tree
def diameter(root):
    height = Height()
    return diameterOpt(root, height)

root = treeInput()
print(diameter(root)) 
