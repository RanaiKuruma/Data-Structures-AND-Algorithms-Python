import math,sys 
def minSquare(n):
    if(n == 0):
        return 0 

    ans = sys.maxsize 
    root = int(math.sqrt(n))
    for i in range(1, root + 1):
        currAns = 1 + minSquare(n - (i ** 2))
        ans = min(ans,currAns)
    return ans 

n = int(input())
ans = minSquare(n)
print(ans)
