import heapq 
def kLargest(arr,k):
    heap = arr[0:k]
    heapq.heapify(heap)
    n = len(arr)

    for i in range(k,n):
        if(heap[0] < arr[i]):
            heapq.heapreplace(heap,arr[i])
    return heap 

arr = [int(i) for i in input().split()]
k = int(input('K:'))
ans = kLargest(arr,k)
for ele in ans:
    # print(ele,end=' ')
    print(ele)

