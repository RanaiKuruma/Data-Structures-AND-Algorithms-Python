class MapNode:
    def __init__(self,key,value):
        self.key = key 
        self.value = value 
        self.next = None 

class Map:
    def __init__(self):
        self.bucketSize = 10 
        self.bucket = [None for i in range(self.bucketSize)]
        self.count = 0 

    def size(self):
        return self.count 

    def getBucketIndex(self,key):
        return (abs(key) % self.bucketSize)                

    def insert(self,key,value):
        hc = hash(key)        
        index = self.getBucketIndex(hc)
        head = self.bucket[index]

        #Iterating through the linked list to insert a newNode 
        while(head != None):
            #If the values of the head's key and the key in the bucket are same then move on :)
            if(head.key == key):
                head.value = value 
                return 
            head = head.next

        #On reaching none insert a newNode 
        newNode = MapNode(key,value)                          
        newNode.next = head 
        self.bucket[index] = newNode  
        self.count += 1 

# The size of the map should remain the same 
# This is an indicator that you have successfuly implemented a hashmap 

m = Map()
m.insert('Ranai',1)
print(m.size())
m.insert('Bahubali',2)
print(m.size())

#Making the collision handling happen 
m.insert('Ranai',7)
print(m.size())
