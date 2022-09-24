def lcs(str1,str2,i,j):
    if(i == len(str1) or j == len(str2)):
        return 0 

    if(str1[i] == str2[j]):
        return 1 + lcs(str1,str2,i+1,j+1) 

    else:
        lcs1 = lcs(str1,str2,i+1,j)
        lcs2 = lcs(str1,str2,i,j+1)       
        ans = max(lcs1,lcs2)

    return ans 

s1 = input("String1:")
s2 = input("String2:")
ans = lcs(s1,s2,0,0)
print(ans)
