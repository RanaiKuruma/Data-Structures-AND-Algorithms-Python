def safeDirection(row,col,board,n):
    #Vertical dirn
    i = row-1
    while(i >= 0):
        #A Queen already exists 
        if(board[i][col] == 1):
            return False 
        i -= 1     

    #Upper-left diagonal dirn 
    i = row-1
    j = col-1

    while(i >= 0 and j >= 0):
        #A Queen already exists
        if(board[i][j] == 1):
            return False 
        i -= 1
        j -= 1 

    #Upper-right diagonal dirn 
    i = row -1 
    j = col + 1

    #j <= n because col is inc and it cannot exceed the dimension of the chessboard 
    while(i >= 0 and j < n):
        #A Queen already exists
        if(board[i][j] == 1):
            return False 
        i -= 1 
        j += 1 

    return True 

def printPathHelper(row,n,board):
    if(row == n):
        for i in range(n):
            for j in range(n):
                print(board[i][j],end= ' ')                
        print()                
        return 

    for col in range(n):
        if(safeDirection(row,col,board,n)):
            #Entry point in chessboard 
            board[row][col] = 1
            printPathHelper(row+1,n,board) 
            #0 as I need to backtrack because I already explored the path                     
            board[row][col] = 0
    return    

def printPath(n):
    board = [[0 for j in range(n)] for i in range(n)]
    printPathHelper(0,n,board)

n = int(input())
printPath(n)
