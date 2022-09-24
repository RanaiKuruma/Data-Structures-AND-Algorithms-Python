def isBalanced(string):
    s = []
    for char in string:
        if char in '(':
            s.append(char)
        elif char in ')':
            s.pop()       

    #If stack is not empty then only you will be able to pop
    if(not s):
        return True 
    return False               


str = input()
ans = isBalanced(str)
if(ans):
    print('true')
else:
    print('false')


