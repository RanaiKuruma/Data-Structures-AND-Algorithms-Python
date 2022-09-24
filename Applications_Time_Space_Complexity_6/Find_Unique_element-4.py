def findUnique(arr, n) :
    n=len(arr)
    uniqueElement = 0

    for i in range(n):
        uniqueElement ^= arr[i]

    return uniqueElement    

arr = [6,1,6,3,4,3,1]
n=len(arr)
print(findUnique(arr,n))

                
        