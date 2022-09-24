class TrieNode:
    def __init__(self): 
        self.children = [None for i in range(26)]
        self.Terminal = False 

class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        #Returns new trie node (initialized to nulls)
        return TrieNode()        

    def __charToIndex(self,ch):
        #Converts the key(current char) into index 
        #Using 'a' through 'z' and lower case 
        return ord(ch) - ord('a')

    def insertWord(self,key):
        #If not present insert key into trie 
        #If the key is prefix of trie node,
        #Just mark leaf node 
        root = self.root 
        lenght = len(key)
        for level in range(lenght):
            index = self.__charToIndex(key[level])

            #If the current char is not present 
            if(not(root.children[index])):
                root.children[index] = self.getNode()                                
            root = root.children[index]                

        #Mark last node as leaf 
        root.Terminal = True 

    def searchWord(self,key):
        #Return a boolean if the key is there 
        root = self.root 
        lenght = len(key)
        for level in range(lenght):
            index = self.__charToIndex(key[level])

            if(not(root.children[index])):
                return False 
            root = root.children[index] 
            
        return root.Terminal    

keys = ['the', 'a', 'there', 'answer', 'any','by', 'their']

output = ["Not present in trie","Present in trie"]
root = Trie()

for key in keys:
    root.insertWord(key)

print(root.searchWord('the'))
print(root.searchWord('thaw'))

