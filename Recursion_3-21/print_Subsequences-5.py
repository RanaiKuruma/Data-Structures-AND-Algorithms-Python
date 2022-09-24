def printSubs(inputStr,output):
    n = len(inputStr)   
    if(n == 0):
        print(output)
        return 

    #Excluding first character 
    printSubs(inputStr[1:],output)        

    #Including firstCharacter
    newString = output + inputStr[0] 
    printSubs(inputStr[1:],newString)

if __name__ == '__main__':
    str = input('String:')
    ans = printSubs(str," ")
    ans
