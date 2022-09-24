def subsequences(s):
    n = len(s)
    if(n == 0):
        output = []
        output.append(" ")
        return output 

    smallerStr = s[1:]        
    smallerOutput = subsequences(smallerStr)

    output = []
    #Putting the elements of the substring in a list 
    for sub in smallerOutput:
        output.append(sub)

    #Copying the elements of the substring into the same list and appending the first element at the end of the list 
    for sub in smallerOutput:        
        output.append(s[0] + sub)

    return output 

str = input("String:")
ans = subsequences(str)
print(ans)
