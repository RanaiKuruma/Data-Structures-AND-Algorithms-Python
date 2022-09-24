def lis(arr,i,n):
    if(i == n):
        return 0,0

    inc_Max = 1 
    for j in range(i+1,n):
        if(arr[j] >= arr[i]):
            further_Max = lis(arr,j,n)[0]        
            inc_Max = max(inc_Max,1+further_Max)

    exc_Max = lis(arr,i+1,n)[1]            
    overall_Max = max(inc_Max,exc_Max)

    return inc_Max,overall_Max 
    
arr = [int(i) for i in input().split()]
ans = lis(arr,0,len(arr))[1]
print(ans)