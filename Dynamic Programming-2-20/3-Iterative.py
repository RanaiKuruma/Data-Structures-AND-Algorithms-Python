def kNapSack(W,wt,val):
    n = len(val)
    dp = [[0 for i in range(W + 1)] for j in range(n + 1)]

    #Iterating through the matrix starting from 1 to exclude the 0th element
    for i in range(1,n + 1):
        for j in range(1,W + 1):

            #If the wt of the ith item is greater than the maximum wt then return the item in hand 
            # Taking start of item from (i-t)th instead of ith item due to list indexing     
            if(wt[i-1] > j):
                ans = dp[i - 1][j]

            else:
                #Including the ith item 
                ans1 = val[i - 1] + dp[i - 1][j - wt[i - 1]]
                #Excluding the ith item                 
                ans2 = dp[i - 1][j]
                ans = max(ans1,ans2)

            #You need to fill the matrix 
            # The relation dp[i][j] is made for filling the matrix     
            dp[i][j] = ans 

    return dp[n][W]                        

W = 5
wt = [1,2,4,5]
val = [5,4,8,6]
n = len(val)
ans = kNapSack(W,wt,val)
print(ans)
