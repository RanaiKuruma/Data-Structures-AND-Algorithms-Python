#Recursion bottom-up approach
# def minArray(n):
#     if(len(n) == 1):
#         return n[0]

#     minSmallArray = minArray(n[1:])
#     overallMin = min(minSmallArray,n[0])

#     return overallMin 

#Recursion top-down approach
def printMin(l,minSoFar = 100000):
    if(len(l) == 0):
        print(minSoFar)
        return 

    newMin = min(minSoFar,l[0])        
    printMin(l[1:],newMin)

arr = [int(i) for i in input().split()]    
ans = printMin(arr,100000)
