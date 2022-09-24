class BinaryTreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None

btn1 = BinaryTreeNode(1)
btn2 = BinaryTreeNode(4)
btn3 = BinaryTreeNode(5)

#Connecting btn1 to btn2 
btn1.left = btn2
#Connecting btn1 to btn3
btn1.right = btn3

#Note - A tree will never have a cycle i.e connect btn1 to btn2 and btn1 to btn3