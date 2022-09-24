def checkRedundantBrackets(expression) :
    temp = 0
    l = len(expression)
    for i in range(l-1):
        si = expression[i]
        ei = expression[i+1]
        if(si == '(' and ei == ')'):
            return True 
        elif(si == '(' and ei == '('):
            temp = 2
        elif(si == ')' and ei == ')' and temp == 2):
            return True 
    return False 

expression = input()
if checkRedundantBrackets(expression) :
	print("true")
else :
	print("false")
