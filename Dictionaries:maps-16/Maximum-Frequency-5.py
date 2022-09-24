def maxFreq(arr):
    d = dict()
    for i in arr:
        if i in d:
            d[i] = d.get(i, 0) + 1
        else:
            d[i] = 1

    max = 0
    for x in arr:
        if d[x] > max:
            max = d[x]
            num = x        
            
    return num  

arr = [int(i) for i in input().split()]
ans = maxFreq(arr)
print(ans)
