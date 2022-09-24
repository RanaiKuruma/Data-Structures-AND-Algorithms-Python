# Method - 1
# def rotateArray(arr,n,d):
# 	# Storing the first d elements in the array
# 	temp = []
# 	i = 0
# 	while(i<d):
# 		temp.append(arr[i])
# 		i += 1

# 	i = 0
# 	# Iterating through the rest of the list
# 	while(d<n):
# 		arr[i] = arr[d]
# 		i += 1
# 		d += 1
# 	arr = arr[:i] + temp
# 	return arr


# inputArray = [int(ele) for ele in input().split()]
# n = len(inputArray)
# print(rotateArray(inputArray,n,2))

# Method - 2
def rotateArray(arr,n,d):
	temp = arr[:d]
	arr[:] = arr[d:n] + temp 
	return arr 

array = [int(i) for i in input().split()]	
n = len(array)
d = int(input())
ans = rotateArray(array,n,d)
print(ans)
