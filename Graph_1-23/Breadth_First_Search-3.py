import queue
class Graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices 
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]

    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    #Source Vertex(sv)
    def __bfsHelper(self,sv,visited):
        q = queue.Queue()
        q.put(sv)
        visited[sv] = True 

        while(q.empty() is False):
            u = q.get()
            print(u)
            for i in range(self.nVertices):
                if(self.adjMatrix[u][i] > 0 and visited[i] is False):
                    q.put(i)
                    visited[i] = True 

    def bfs(self):
        visited = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if(visited[i] is False):
                self.__bfsHelper(i,visited)

    def __str__(self):
        return str(self.adjMatrix)

#Add vertex according to vertex
g=Graph(7)
g.addEdge(0,1)
g.addEdge(0,3)
g.addEdge(2,4)
g.addEdge(2,5)
g.addEdge(4,6)
g.bfs()



