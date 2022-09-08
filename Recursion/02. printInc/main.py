n = 6
def printDecOrder(n):
    if n == 0 :
        return
    printDecOrder(n-1)
    print(n)
printDecOrder(n)