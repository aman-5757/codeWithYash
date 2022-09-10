str = "abc"

def printSubSequence(str,ans):
    if len(str) == 0:
        print(ans)
        return
    
    ch = str[0]         #a
    ros = str[1:]       #bc
    #aaega or yes wali call
    printSubSequence(ros, ans + ch)
    #nahi aaega or no wali call
    printSubSequence(ros, ans)


printSubSequence(str,"")
