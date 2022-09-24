class Graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices 
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]

    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2] = 1 
        self.adjMatrix[v2][v1] = 1

    def __hasPathHelper(self,v1,v2,visited):
        if(self.adjMatrix[v1][v2] > 0):
            return True 

        else:
            visited[v1] = True 
            for i in range(self.nVertices):
                if(self.adjMatrix[v1][i]  and visited[i] == False):
                    if(self.__hasPathHelper(i,v2,visited)):
                        return True 

            return False
             
    def hasPath(self,v1,v2):
        visited = [False for i in range(self.nVertices)]
        return self.__hasPathHelper(v1,v2,visited)

    def __str__(self):
        return str(self.adjMatrix)        

g = Graph(4)
g.addEdge(0,1)
g.addEdge(0,3)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(1,3)

print(g.hasPath(0,1))

# g = Graph(5)
# g.addEdge(0,1)
# g.addEdge(1,3)
# g.addEdge(3,2)
# g.addEdge(2,4)
# print(g.hasPath(3,5))
