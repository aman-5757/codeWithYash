n = 4
def printDecIncOrder(n):
    if n == 0 :
        return
    print(n)
    printDecIncOrder(n-1)
    print(n)
printDecOrder(n)