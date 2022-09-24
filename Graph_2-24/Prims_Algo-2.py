import sys
class Graph:
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjMatrix=[[0 for i in range(nVertices)]for j in range(nVertices)]
        
    def addEdge(self,v1,v2,wt):
        self.adjMatrix[v1][v2]=wt
        self.adjMatrix[v2][v1]=wt

    def __str__(self):
        return str(self.adjMatrix)

    def __getMinVertex(self,visited,weight):
        min_vertex=-1
        for i in range(self.nVertices):
            if(visited[i] is False and (min_vertex==-1 or weight[min_vertex]>weight[i])):
                min_vertex=i
        return min_vertex

    def prims(self):
        visited=[False for i in range(self.nVertices)]
        parent=[-1 for i in range(self.nVertices)]
        weight=[sys.maxsize for i in range(self.nVertices)]
        weight[0]=0

        for i in range(self.nVertices-1):
            min_vertex=self.__getMinVertex(visited,weight)
            visited[min_vertex]=True

            #Explore the neighbors of minVertex which is not visited and update the weight corresponding to them if required
            for j in range(self.nVertices):
                if self.adjMatrix[min_vertex][j]>0 and visited[j] is False:
                    if(weight[j]>self.adjMatrix[min_vertex][j]):
                        weight[j]=self.adjMatrix[min_vertex][j]
                        parent[j]=min_vertex

        #To print the over all  changes 
        for i in range(1,self.nVertices):
            if i<parent[i]:
                print(str(i)+" "+str(parent[i])+" "+str(weight[i]))
            else:
                print(str(parent[i])+" "+str(i)+" "+str(weight[i]))
                
li=[int(ele) for ele in input().split()]
n=li[0]
E=li[1]

g=Graph(n)
for i in range(E):
    curr_input=[int(ele) for ele in input().split()]
    g.addEdge(curr_input[0],curr_input[1],curr_input[2])
print(" ")    
g.prims()