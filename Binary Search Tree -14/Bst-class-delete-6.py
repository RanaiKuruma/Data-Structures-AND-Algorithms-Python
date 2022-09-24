class BinaryTreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

class BST:
    def __init__(self):
        self.root = None 
        self.numNode = 0 

    def printTreeHelper(self,root):
        if(root == None):
            return 

        print(root.data,end=' ')                
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)

    def printTree(self):
        self.printTreeHelper(self.root) 

    def isPresentHelper(self,root,data):
        if(root == None):
            return False 
        if(root.data == data):
            return True 
        if(root.data > data):
            return self.isPresentHelper(root.left,data) 
        if(root.data < data):
            return self.isPresentHelper(root.right,data)               

    def isPresent(self,data):
        return self.isPresentHelper(self.root,data)

    def insertHelper(self,root,data):
        if(root == None):
            node = BinaryTreeNode(data)
            return node 

        if(root.data > data):
            root.left = self.insertHelper(root.left,data) 
            return root 

        if(root.data < data):
            root.right = self.insertHelper(root.right,data)               
            return root 

    def insert(self,data):
        self.numNode += 1 
        self.root = self.insertHelper(self.root,data) 

    def min(self,root):
        if(root == None):
            return 100000
        if(root.left == None):
            return root.data 

        return self.min(root.left)                

    def deleteHelper(self,root,data):
        if(root == None):
            return False,None 

        if(root.data > data):
            deleted,newLeft = self.deleteHelper(root.left,data) 
            root.left = newLeft 
            return deleted,root 

        if(root.data < data):
            deleted,newRight = self.deleteHelper(root.right,data)
            root.right = newRight
            return deleted,root 

        if(root.left == None and root.right == None):
            return True,None 
        if(root.left == None):
            return True,root.right
        if(root.right == None):
            return True,root.left 

        min = self.min(root.right)                                                      
        root.data = min 
        deleted,newRight = self.deleteHelper(root.right,min) 
        root.data = newRight 
        return True,root 

    def delete(self,data):
        deleted,newRoot = self.deleteHelper(self.root,data)
        if(deleted):
            self.numNode -= 1
        self.root = newRoot 
        return deleted 

    def count(self):
        return self.numNode  

b = BST()
b.insert(1)
b.insert(2)
b.insert(3)
b.insert(4)
b.insert(5)

b.printTree()

# b.delete(3)
# b.printTree()


