
def pairStar(input, output,i=0):
    # appending current char
    output += input[i]  

    # Base Case
    n = len(input)
    if(i == n - 1):
        print(output)
        return

    # Induction Hypothesis
    if(input[i] == input[i + 1]):
        output += '*'  

    pairStar(input, output,i+1)

if __name__ == '__main__':
    oldString = input()    
    newString = ''
    ans = pairStar(oldString, newString)
