def lis(li,i=0):
    n = len(li)
    if(i == n):
        return 0,0 

    #By default 
    including_max = 1
    #The subsequence goes from left to right
    # Indexing starts with 1 because incMax is there 
    for j in range(i+1,n):
        if(li[j] > li[i]):
            further_Inc_Max = lis(li,j)[0]
            including_max = max(including_max,1+further_Inc_Max)

    excluding_Max = lis(li,i+1)[1]            
    overallMax = max(including_max,excluding_Max)

    return including_max,overallMax 

arr = [int(i) for i in input().split()]
#[1] for calling the first answer 
ans = lis(arr)[1]
print(ans)
