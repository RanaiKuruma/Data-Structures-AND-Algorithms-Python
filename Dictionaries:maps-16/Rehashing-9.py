class MapNode:
    def __init__(self,key,value):
        self.key = key 
        self.value = value 
        self.next = None 

class Map:
    def __init__(self):
        self.bucketSize = 5 
        self.bucket = [None for i in range(self.bucketSize)]
        self.count = 0 

    def size(self):
        return self.count 

    def getBucketIndex(self,key):
        return (abs(key) % self.bucketSize)                

    def getValue(self,key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.bucket[index]
        while(head != None):
            if(head.key == key):
                return head.value
            head = head.next 

        return None 

    def remove(self,key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.bucket[index]
        prev = None
        while head != None:
            if(head.key == key):
                if(prev is None):
                    self.bucket[index] = head.next
                else:
                    prev.next = head.next 
                self.count -= 1                     
                return head.value 

            prev = head 
            head = head.next 
        return None   

    def rehash(self):
        #Increasing the size of the bucket array to prevent the crossing of   load factor
        temp = self.bucket 
        self.bucket = [None for i in range(2*self.bucketSize)]
        self.bucketSize = 2 * self.bucketSize
        self.count = 0

        #Adding values of old bucket into the new bucket
        for head in temp:
            while head != None:
                self.insert(head.key,head.value)
                head = head.next 

    def loadFactor(self):
        return self.count / self.bucketSize

    def insert(self,key,value):
        hc = hash(key)        
        index = self.getBucketIndex(hc)
        head = self.bucket[index]

        while(head != None):
            
            if(head.key == key):
                head.value = value 
                return 
            head = head.next
        head = self.bucket[index]

        newNode = MapNode(key,value)                          
        newNode.next = head 
        self.bucket[index] = newNode  
        self.count += 1 
        loadFactor = self.count / self.bucketSize
        if(loadFactor >= 0.7):
            self.rehash()

m = Map()
for i in range(10):
    m.insert('abc'+str(i),i+1)
    print(m.loadFactor())

# print( )

# for i in range(10):
#     print('abc'+str(i)+':',m.getValue('abc'+str(i)))

