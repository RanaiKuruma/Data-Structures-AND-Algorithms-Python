def checkPalindrome(s):
    n = len(s)
    si = 0
    ei = n-1

    #Base Case 
    if(s[si] == s[ei]):
        return True 
    if(s[si] != s[ei]):
        return False 
        
    # Induction Hypothesis    
    return checkPalindrome(s)        

# Driver Program
str = input()    
ans = checkPalindrome(str)
if(ans is True):
    print('true')
else:
    print('false')    

