#Accesing data in dictionary
a = {1:2,3:4,'list':[1,2,3],'dict':{1:2}}
# print(a)

#To access elements you need to use the actual key 
# print(a[1])
# print(a[3])
# print(a['list'])
# print(a['dict'])

#Another way 
# print(a.get(1))
# print(a.get('list'))
# print(a.get('dict'))

#Gives you none
#If the key is not there it will return None 
# print(a.get('li'))

#It will return the value associated with if key is present otherwise the second argument is returned 
# print(a.get('li',0))

#To get all the keys
# print(a.keys())

#To get all the values
# print(a.values())

#Using a for loop

# #Prints all the keys 
# for i in a:
#     print(i)

#Generally in this
# #Prints all the keys and values
# for i in a:
#     print(i,a[i])

# #Prints all the values
# for i in a.values():
#     print(i)

#To check wheter a key is in a dictionary or not 
# print('list' in a)
# print('li' in a)


