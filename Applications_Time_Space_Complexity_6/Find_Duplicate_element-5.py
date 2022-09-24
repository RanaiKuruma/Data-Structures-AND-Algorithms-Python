def findDuplicate(arr,n):
    n = len(arr)
    
    arrSum = 0
    for i in range(n):
        arrSum += arr[i]

    arrSumRest = int((n-2) * (n-1)/2)

    duplicateElement = arrSum - arrSumRest
    return duplicateElement


arr = [0,7,2,5,4,7,1,3,6]
n = len(arr)
print(findDuplicate(arr,n))
