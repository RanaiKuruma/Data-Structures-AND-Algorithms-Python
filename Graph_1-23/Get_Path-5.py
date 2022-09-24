class Graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices 
        self.adjMatrix = [[0 for i in range(self.nVertices)] for j in range(self.nVertices)]

    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2] = 1 
        self.adjMatrix[v2][v1] = 1

    def getPathHelper(self,v1,v2,visited,list):
        if(self.adjMatrix[v1][v2] > 0):
            list.append(v2)
            list.append(v1)
            return list 

        visited[v1] = True 
        for i in range(self.nVertices):
            if(self.adjMatrix[v1][i] > 0 and visited[i] is False):
                if(self.getPathHelper(i,v2,visited,list)):
                    list.append(v1)                        

                    return list 

        return False 

    def getPath(self,v1,v2):
        visited = [False for j in range(self.nVertices)]                            
        return self.getPathHelper(v1,v2,visited,[])

    def __str__(self):
        return str(self.adjMatrix)            

v,e = [int(i) for i in input().split()][:2]
g = Graph(v)
for i in range(e):
    a,b = [int(x) for x  in input().split()][:2]
    g.addEdge(a,b)

v1,v2 = [int(y) for y in input().split()][:2]
list = g.getPath(v1,v2)
if (list):
    for i in list:
        print(i,end=' ')


