import heapq
def kSmallestElement(arr,k):
    heap = arr[0:k]
    heapq._heapify_max(heap)
    n = len(arr)
    for i in range(k,n):
        if(heap[0] > arr[i]):
            heapq._heapreplace_max(heap,arr[i])    
    return heap 

li = [int(i) for i in input().split()]
k = int(input("K:"))
ans = kSmallestElement(li,k)
for ele in ans:
    print(ele,end=' ')

