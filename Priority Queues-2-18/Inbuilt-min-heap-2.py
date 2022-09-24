import heapq 

li = [1,5,4,8,7,9,11]
#By default it constructs a min heap 
heapq.heapify(li)
# print(li)

#To push an element 
# heapq.heappush(li,2)
# print(li)

#To pop an element 
#Top most element of the min heap is gone i.e min element of the min heap is gone 
# heapq.heappop(li)
# print(li)

#Replaces the min element in the min heap i.e the top most element in min heap and replaces it with the number 
heapq.heapreplace(li,6)
print(li)


