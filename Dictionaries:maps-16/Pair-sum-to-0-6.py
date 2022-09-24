def pairSum(arr,n):
    pairSum = 0
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i] + arr[j] == 0):
                pairSum += 1 
    return pairSum 

arr = [int(i) for i in input().split()]
n = len(arr)
ans = pairSum(arr,n)
print(ans)
