n = 6
def printIncOrder(n):
    if n == 0 :
        return
    printIncOrder(n-1)
    print(n)
printDecOrder(n)