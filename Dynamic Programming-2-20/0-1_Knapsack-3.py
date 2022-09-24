def kNapSack(W,val,wt,n,i):
    if(i == n):
        return 0 

    if(wt[i] > W):
        ans = kNapSack(W,val,wt,n,i+1)
    else:
        #Including the ith item 
        ans1 = val[i] + kNapSack(W-wt[i],val,wt,n,i+1)
        #Excluding the ith item 
        ans2 = kNapSack(W,val,wt,n,i+1)
        ans = max(ans1,ans2)

    return ans 

# val = [200,300,100]
val = [24,13,23,15,16]
# wt = [20,25,30]
wt = [12,7,11,8,9]
W = 26
n = len(val)
ans = kNapSack(W,val,wt,n,0)
print(ans)
