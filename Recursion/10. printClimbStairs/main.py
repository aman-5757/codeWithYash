n = 5

#asf --> answer so far

def printClimbStairs(n, asf):
    if n == 0 :
        print(asf)
        return
    
    if  n-1 >= 0:
        printClimbStairs(n-1,asf+"1")
    if n-2 >= 0:
        printClimbStairs(n-2,asf+"2")

def countClimbStairs(n):
    if n == 0 :
        return 1
    
    myAns = 0

    if  n-1 >= 0:
        myAns += countClimbStairs(n-1)
    if n-2 >= 0:
        myAns += countClimbStairs(n-2)

    return myAns

printClimbStairs(n,"")

ans = countClimbStairs(n)
print(ans)
