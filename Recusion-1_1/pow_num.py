def pow_n(x, n):
    if(n == 0):
        return 1
    else:
        return x * pow_n(x, n-1)    

x = int(input())
n = int(input())        

print(pow_n(x, n))
