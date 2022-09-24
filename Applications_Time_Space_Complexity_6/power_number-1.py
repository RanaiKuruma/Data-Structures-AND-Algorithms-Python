def power(x, n):
    # Please add your code here
    #Base Case
    if(n==0):
        return 1
    return x*power(x,n-1)

# Main
# Use it in Competitive Coding
from sys import setrecursionlimit
setrecursionlimit(11000)
x, n=list(int(i) for i in input().strip().split(' '))
print(power(x, n))
