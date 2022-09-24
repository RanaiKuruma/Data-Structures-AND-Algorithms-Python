import math,sys 
def minSquare(n,dp):
    if(n == 0):
        return 0 

    ans = sys.maxsize 
    root = int(math.sqrt(n))
    for i in range(1, root + 1):

        newCheckValue = n - (i**2)
        if(dp[newCheckValue] == -1):
            smallAns = minSquare(newCheckValue,dp)
            dp[newCheckValue] = smallAns 
            currAns = 1 + smallAns 

        else:
            currAns = 1 + dp[newCheckValue]

        ans = min(ans,currAns)

    return ans 

n = int(input())
dp = [-1 for i in range(n+1)]
ans = minSquare(n,dp)
print(ans)
