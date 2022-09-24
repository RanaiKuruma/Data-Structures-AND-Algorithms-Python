import heapq 

li = [1,5,4,7,8,9,2,3]
heapq._heapify_max(li)
# print(li)

#To remove an element 
# heapq._heappop_max(li)
# print(li)

#To replace the element 
heapq._heapreplace_max(li,0)
# print(li)

#To insert an element 
# li.append(6)
#Will compare the left and the right child of max heap and then insert
heapq._siftdown_max(li,0,len(li)-1)
# print(li)
