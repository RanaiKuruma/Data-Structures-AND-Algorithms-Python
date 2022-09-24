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

    def compressionCode(self,hc):
        return (abs(hc) % self.bucketSize)

    def insert(self,key,value):
        hc = hash(key)
        index = self.compressionCode(hc)
        head = self.bucket[index]

        #For collision handling
        while(head != None):
            if(head.key == key):
                head.value = value 
                return 
            head = head.next 

        newNode = MapNode(key,value)                
        newNode.next = head 
        self.bucket[index] = newNode 

        self.count += 1 

    def remove(self,key):
        hc = hash(key) 
        index = self.compressionCode(hc)
        head = self.bucket[index]
        prev = None 

        while(head != None):
            if(head.key == key):
                if(prev == None):
                    self.bucket[index] = head.next 
                else:
                    prev.next = head.next 
            prev = head 
            head = head.next 
        return None 

    def search(self,key):
        hc = hash(key) 
        index =self.compressionCode(hc)
        head = self.bucket[index]

        while(head != None):
            if(head.key == key):
                return head.value 
            head = head.next 

        return None                 

m = Map()
m.insert('Ranai',1)
m.insert('Ianar',2)

print("Before Collision Handling value of Ranai: ",end=' ')
print(m.search('Ranai'))
# print(m.search('Ianar'))

#Making the collision handling happen
print("After Collision Handling value of Ranai: ",end=' ')
m.insert('Ranai',7)
print(m.search('Ranai'))
# print(m.search('Ianar'))
# print(m.size())




