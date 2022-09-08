n = 3
def pzz(n):
    if n == 0 :
        return
    print(n)
    pzz(n-1)

    print(n)
    pzz(n-1)
    
    print(n)
pzz(n)

#ans-- 20 -- 21 length 