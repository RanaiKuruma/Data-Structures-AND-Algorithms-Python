class Graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices 
        self.adjMatrix = [[0 for i in range(self.nVertices)] for j in range(self.nVertices)]

    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2] = 1 
        self.adjMatrix[v2][v1] = 1

    def isConnectedHelper(self,v1,visited):
        visited[v1] = True 
        for i in range(self.nVertices):
            if(self.adjMatrix[v1][i] > 0 and visited[i] is False):
                self.isConnectedHelper(i,visited)

        return visited 
    
    def isConnected(self,v1):        
        visited = [False for j in range(self.nVertices)]
        return self.isConnectedHelper(v1,visited)

    def __str__(self):
        return str(self.adjMatrix)            

v,e = [int(i) for i in input().split()][:2]
g = Graph(v)
for i in range(e):
    a,b = [int(x) for x  in input().split()][:2]
    g.addEdge(a,b)

status = g.isConnected(0)
flag = True 
for j in status:
    if(j is False):
        flag = False 

if(flag):
    print('true')
else:
    print('false')       
