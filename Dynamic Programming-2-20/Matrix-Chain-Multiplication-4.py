import sys 
def mcm(p,i,j):
    if(i == j):
        return 0 

    min_Value = sys.maxsize 
    for k in range(i,j):
        ans1 = mcm(p,i,k)
        ans2 = mcm(p,k+1,j)

        mCost = p[i-1] * p[k] * p[j]
        curr_Value = ans1 + ans2 + mCost 
        min_Value = min(min_Value,curr_Value )

    return min_Value 

p = [2,3,4,5,6]
# p = [1,2,3,4,5,6]
n = len(p) - 1 
ans = mcm(p,1,n)
print(ans)

