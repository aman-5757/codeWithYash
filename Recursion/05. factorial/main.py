n = 6
def factorial(n):
    if n == 0 :
        return 1
    recAns = factorial(n-1)
    return n * recAns
ans = factorial(n)
print(ans)