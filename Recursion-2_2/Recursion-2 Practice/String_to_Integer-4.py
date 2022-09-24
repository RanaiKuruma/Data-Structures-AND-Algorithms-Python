def stringToInt(s):
    # Base Case 
    n = len(s)
    if(n == 1):
        return ord(s[0]) - ord('0')

    # Induction Hypothesis
    # Second Character
    b = stringToInt(s[1:])    

    # First Character
    a = ord(s[0]) - ord('0')

    a = a * pow(10, n - 1) + b
    return a


str = input()
print(stringToInt(str))

