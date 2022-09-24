import queue
class Tree:
    def __init__(self,data):
        self.data = data  
        self.children = []

def printTreeLevelWise(root):
    if(root == None):
        return 

    q = queue.Queue()        
    q.put(root)

    while(not(q.empty())):
        currNode = q.get()
        print(currNode.data,':',end=" ")
        
        for child in currNode.children:
            q.put(child)
            print(child.data,',',end=" ")
        print( )

    return root 

def takeTreeInputLevelWise():
    q = queue.Queue() 
    print("Enter root : ")
    rootData = int(input())
    #Edge Case
    if(rootData == -1):
        return 

    root = Tree(rootData)
    q.put(root)

    while(not(q.empty())):
        currNode = q.get()
        print("Enter no of children for :",currNode.data)
        numChildren = int(input())

        for i in range(numChildren):
            print("Enter next child for ",currNode.data)
            childData = int(input())
            child = Tree(childData)
            currNode.children.append(child)
            q.put(child)

    return root 
    
root = takeTreeInputLevelWise()
printTreeLevelWise(root)


