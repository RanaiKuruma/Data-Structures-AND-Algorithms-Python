def intersection(arr1, arr2, n, m) :
    arr1.sort()
    arr2.sort()

    i = 0
    j = 0
    n = len(arr1)
    m = len(arr2)

    while(i < n and j < m):
        if(arr1[i] < arr2[j]):
            i += 1
        elif(arr2[j] < arr1[i]):
            j += 1

        else:
            print(arr1[i])
            i += 1
            j += 1        


if __name__ == '__main__':
    arr1 = [6, 9, 8, 5]  
    n = len(arr1)          
    arr2 = [9, 2, 4, 1, 8]
    m = len(arr2)
    intersection(arr1, arr2, n, m)
