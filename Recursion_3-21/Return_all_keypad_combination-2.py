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

def keypad(n):
    if(n == 0):
        output = []
        output.append(" ")
        return output 

    smallerInt = n // 10 
    lastDigit = n % 10 
    smallerOutput = keypad(smallerInt)
    d = getString(lastDigit)

    output = []
    for i in smallerOutput:
        for j in d:
            combination = i + j 
            output.append(combination)

    return output 

n = int(input('N:'))
ans = keypad(n)
print(ans)

