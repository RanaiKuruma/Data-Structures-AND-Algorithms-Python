def printPathHelper(x,y,maze,n,solution):
    #It indicates the end of the maze 
    if(x == n-1 and y == n-1):
        solution[x][y] = 1
        print(solution)
        return 

    #Blocking points 
    #solution[x][y] = 1 is a blocking point cuz it's already included 
    if(x < 0 or y < 0 or x >=n or y >= n or maze[x][y] == 0 or solution[x][y] == 1):
        return 


    #Exploring all the directions by intialising the first point by 1 to enter the maze 
    solution[x][y] = 1 
    #Moving down 
    printPathHelper(x+1,y,maze,n,solution) 
    #Moving right
    printPathHelper(x,y+1,maze,n,solution)
    #Moving left 
    printPathHelper(x,y-1,maze,n,solution)
    #Moving Up 
    printPathHelper(x-1,y,maze,n,solution)

    #Solution[x][y] = 0 because 1 is already included in the path and you might need to explore another path 
    solution[x][y] = 0

def printPath(maze):
    n = len(maze)
    #Intialising a solution matrix so that it stores all the soln's 
    solution = [[0 for j in range(n)] for i in range(n)]
    printPathHelper(0,0,maze,n,solution)

#n is for matrix of dimension n 
n = int(input())
maze = []
#Matrix input
for i in range(n):
    row = [int(ele) for ele in input().split()]
    maze.append(row)

printPath(maze)
