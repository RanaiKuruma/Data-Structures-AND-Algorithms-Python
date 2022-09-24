def getString(d):
    if(d == 2):
        return 'abc'

    if(d == 3):
        return 'def'

    if(d == 4):
        return 'ghi'

    if(d == 5):
        return 'jkl'

    if(d == 6):
        return 'mno'

    if(d == 7):
        return 'pqrs'

    if(d == 8):
        return 'tuv'

    if(d == 9):
        return 'wxyz'

def printKeypad(input,output):
    if(input == 0):
        print(output)
        return 

    smallerDigit = input // 10
    lastDigit = input % 10 

    d = getString(lastDigit)    

    for i in d:
        newStr = i + output  
        printKeypad(smallerDigit,newStr)
    
if __name__ == '__main__':            
    i = int(input())
    o = " "
    ans = printKeypad(i,o)
    ans
