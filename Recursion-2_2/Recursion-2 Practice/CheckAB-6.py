def checkAB(s):
    # Base Case
    n = len(s)
    if (n == 0):
        return True
    
    # Induction Hypothesis
    if (s[0] == 'a'):
        
        if (s[1:3] == 'bb'):
            return True
        
        else:
            return False 
        

str = input()
ans = checkAB(str)
if(ans is True):
    print('true')
else:
    print('false')    

    
