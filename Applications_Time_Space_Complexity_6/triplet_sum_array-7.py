def tripletSumArray(arr,n,num):
    tripletSum = 0

    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if(arr[i] + arr[j] + arr[k] == num):
                    tripletSum += 1

                # else:
                #     return 0

    return tripletSum 


inputList = [int(ele) for ele in input().split()]                    
n = len(inputList)
print(tripletSumArray(inputList,n,10))

