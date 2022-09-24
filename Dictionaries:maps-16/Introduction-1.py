b = [] # Creation of list 
a = {} # Creaton of dictinary 
# print(type(a))

#one-way
a = {'the':2,'a':5,10000:'str'}
# print(a)

#second - way
# print(len(a))
b = a.copy()
# print(b)

#third way 
c = dict([('the',3),('a',10),(2,3)])
# print(c)

#fourth way 
d = dict.fromkeys(['abc',32,4])
# print(d)
#2 args at max 
d = dict.fromkeys(['abc',32,4],10)
print(d)

# Dictionary are muttable change the values 

