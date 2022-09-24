class Graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices 
        self.adjMatrix = [[0 for i in range(self.nVertices)] for j in range(self.nVertices)]

    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2] = 1 
        self.adjMatrix[v2][v1] = 1

    def __connectedCompHelper(self,v1,visited,final_List):
        final_List.append(v1)
        visited[v1] = True 

        for i in range(self.nVertices):
            if(self.adjMatrix[v1][i] > 0 and visited[i] is False):
                self.__connectedCompHelper(i,visited,final_List)

        return final_List 

    def connectedComp(self):
        visited = [False for i in range(self.nVertices)]
        final_list = []
        for i in range(self.nVertices):
            if(visited[i] is False):
                comp = self.__connectedCompHelper(i,visited,[])
                final_list.append(comp)

        return final_list 

    def __str__(self):
        return str(self.adjMatrix)

v,e = [int(i) for i in input().split()][:2]
g = Graph(v)
for i in range(e):
    a,b = [int(x) for x  in input().split()][:2]
    g.addEdge(a,b)

comp = g.connectedComp()


for i in comp:
    print(i)
