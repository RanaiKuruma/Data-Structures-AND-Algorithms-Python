
def minStepTo1(n,dp):
    if(n == 1):
        return 0 
        
    ans2 = pow(10,4)
    ans3 = pow(10,4)

    if(dp[n-1] == -1):
        ans1 = minStepTo1(n-1,dp)
        dp[n-1] = ans1 
    else:
        ans1 = dp[n-1]

    if(n % 2 == 0):
        if(dp[n//2] == -1):
            ans2 = minStepTo1(n//2,dp)
            dp[n//2] = ans2 
        else:
            ans2 = dp[n//2]

    if(n % 3 == 0): 
        if(dp[n//3] == -1):
            ans3 = minStepTo1(n//3,dp)
            dp[n//3] = ans2 
        else:
            ans3 = dp[n//3] 

    ans = 1 + min(ans1,ans2,ans3)                    

    return ans 


n = int(input())
dp = [-1 for i in range(n+1)]
ans = minStepTo1(n,dp)
print(ans)
