n = 6
def printDecOrder(n):
    if n == 0 :
        return
    print(n)
    printDecOrder(n-1)
printDecOrder(n)