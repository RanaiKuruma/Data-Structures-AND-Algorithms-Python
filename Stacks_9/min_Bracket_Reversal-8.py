def countBracketReversals(string):
    if(len(string) == 0):
        return 0
        
    if(len(string) % 2 != 0):
        return -1

    s = []
    for char in string:
        if char == '{':
            s.append(char)

        elif(char == '}'):
            if(s == []):
                print()

            if(s != []):
                s.pop()

            else:
                s.append(char)

    count = 0
    while(len(s) != 0):
        c1 = s.pop()
        c2 = s.pop()

        if(c1 == c2):
            count += 1

        else:
            count += 2

    return count


string = input()
ans = countBracketReversals(string)
print(ans)
