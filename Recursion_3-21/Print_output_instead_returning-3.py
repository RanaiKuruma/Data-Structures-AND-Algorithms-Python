#Factorial 

# def factHelper(n):
#     if(n == 0):
#         return 1 

#     smallerOutput =  factHelper(n-1)        
#     output = n * smallerOutput
#     return output  

# def fact(n):
#     output = factHelper(n)
#     print(output)

def printFact(n,ans):
    if(n == 0):
        print(ans)
        return 
    ans = ans* n 
    printFact(n-1,ans)        

    return ans 

n = 5 
printFact(n,1)
