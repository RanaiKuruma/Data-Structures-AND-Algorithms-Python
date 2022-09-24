def pairSum(arr,n,num):
    pairSum = 0

    for i in range(n):

        for j in range(i+1,n):

            if(arr[i] + arr[j] == num):
                pairSum += 1

    return pairSum    

arr = [1,3,6,2,5,4,3,2,4]
n = len(arr)
num = 7
print(pairSum(arr,n,num))

