class BinaryTree:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

# Basic structure of BST class
class Bst:
    
    def __init__(self):
        self.root = None
        self.numNodes = 0
    
    def printTreeHelper(self, root):
        if root == None:
            return
        print(root.data, end = " ")
        print()
        self.printTreeHelper(root.left)  
        self.printTreeHelper(root.right) 
        
    
    def printTree(self):
        self.printTreeHelper(self.root)
            
    def isPresentHelper(self, root, data):
        if root == None:
            return False
        if root.data == data:
            return True
        
        if root.data > data:
            # Call on left
            return self.isPresentHelper(root.left, data)                                        
        
        else:
            # Call on right
            return self.isPresentHelper(root.right, data)
        
    
    def isPresent(self, data):
        return self.isPresentHelper(self.root, data)
        
    def insertHelper(self, root, data):
        if root == None:
            node = BinaryTree(data)
            return node
        
        if root.data > data:
            root.left = self.insertHelper(root.left, data)
            return root
        
        else:
            root.right = self.insertHelper(root.right, data)
            return root          
        
    
    def insert(self, data):
        self.numNodes += 1
        self.root = self.insertHelper(self.root, data)
    
    def deleteData(self, data):
        return False
    
    def count(self):
        return self.numNodes


b = Bst()
b.insert(2)
b.insert(3)
b.insert(4)
b.insert(5)
b.insert(6)
b.insert(7)

b.printTree()        