def fibb(n,dp):
    if(n == 0 or n == 1):
        return n 

    #Call recursion and store the value of n-1
    if(dp[n-1] == -1):
        ans1 = fibb(n-1,dp)
        dp[n-1] = ans1
    #If answer is already there then store it it in n-1     
    else:
        ans1 = dp[n-1]

    #Call recursion and store the value of n-2
    if(dp[n-2] == -1):
        ans2 = fibb(n-2,dp)
        dp[n-2] = ans2 
    #If answer is already there then store it it in n-2
    else:
        ans2 = dp[n-2]   

    series = ans1 + ans2 
    return series 

n = int(input()) 
dp = [-1 for i in range(n+1)]
ans = fibb(n,dp)
print(ans)
 