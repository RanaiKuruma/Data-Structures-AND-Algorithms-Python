def reverseStack(inputStack,outputStack):
    while(len(inputStack) != 1):
        eleFirstStack = inputStack.pop()
        outputStack.append(eleFirstStack)

    lastEleFirstStack = inputStack.pop()        

    while(len(outputStack) != 0):
        eleSecondStack = outputStack.pop()
        inputStack.append(eleSecondStack)

    reverseStack(inputStack,outputStack)        
    inputStack.append(lastEleFirstStack)
    
print("Input Stack :",end=" ")
inputStack = [int(i) for i in input().split()]
outputStack = []

print("Output Stack :",end= " ")
while(len(inputStack) != 0):
    print(inputStack.pop(),end= " ")
