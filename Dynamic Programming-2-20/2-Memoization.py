def lcs(str1,str2,i,j,dp):
    n1 = len(str1)
    n2 = len(str2)
    if(i == n1 or j == n2):
        return 0 

    if(str1[i] == str2[j]):
        if(dp[i+1][j+1] == -1):
            smallAns = lcs(str1,str2,i+1,j+1,dp)
            dp[i+1][j+1] = smallAns 
            ans = 1 + smallAns  
        else:
            ans = 1 + dp[i+1][j+1]    

    else:
        if(dp[i+1][j] == -1):
            lcs1 = lcs(str1,str2,i+1,j,dp)
            dp[i+1][j] = lcs1 
        else:
            lcs1 = dp[i+1][j]                

        if(dp[i][j+1] == -1):
            lcs2 = lcs(str1,str2,i,j+1,dp)
            dp[i][j+1] = lcs2 
        else:
            lcs2 = dp[i][j+1]            

        ans = max(lcs1,lcs2)

    return ans             

str1 = input('String1:')
str2 = input('String2:')
n = len(str1)
m = len(str2)
dp = [[-1 for j in range(m+1)]for i in range(n+1)]
ans = lcs(str1,str2,0,0,dp)
print(ans)
