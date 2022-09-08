n = 5
x = 2
def powLinear(x,n):
    if n == 0 :
        return 1
    recAns = powLinear(x,n-1)
    return x * recAns
ans = powLinear(x,n)
print(ans)