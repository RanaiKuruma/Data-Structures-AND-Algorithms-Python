def lisI(str1,str2,i,j):
    n = len(str1)
    m = len(str2)

    dp = [[0 for j in range(m+1)] for i in range(n+1)]

    #-1 to ignore the last row 
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if(str1[i] == str2[j]):
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i+1][j],dp[i][j+1])    

    return dp[0][0]                
    
str1 = input('String1:')
str2 = input('String2:')
ans = lisI(str1,str2,0,0)
print(ans)
