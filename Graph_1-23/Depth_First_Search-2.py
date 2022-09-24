class Graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices 
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]

    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    #Starting vertex(sv)
    #Starting vertex(sv) is considered to be 0
    def __dfsHelper(self,sv,visited):
        print(sv)
        visited[sv] = True 
        for i in range(self.nVertices):
            #Vertex needs to be explored first
            if(self.adjMatrix[sv][i] > 0 and 
            visited[i] is False):
                self.__dfsHelper(i,visited)

    def dfs(self):
        visited = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if(visited[i] == False):
                self.__dfsHelper(i,visited)

    def __str__(self):
        return str(self.adjMatrix)

#Add vertex according to vertex
g = Graph(7)
g.addEdge(0,1)
g.addEdge(1,3)
g.addEdge(2,4)
g.addEdge(4,6)
g.addEdge(2,5)
g.dfs()

