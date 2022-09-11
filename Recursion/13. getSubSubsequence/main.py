str = "abc"

def getSubsequence(str)->list:
    if len(str) == 0:
        baseAns = []
        baseAns.append("")
        return baseAns
    
    ch = str[0]
    recAns = getSubsequence(str[1:])
    myAns = []
    for r in recAns:
        myAns.append(r)

    for r in recAns:
        myAns.append(ch+r)

    return myAns

ans = getSubsequence(str)
print(ans)

