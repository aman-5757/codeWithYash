#return total number of ways of mazePath
n = 3
sr = 0
sc = 0
dr = n-1
dc = n-1
def countWays(sr, sc, dr, dc)-> int :
    if  sr == dr and sc == dc :
        return 1
    myCount = 0
    if sc + 1 <= dc:
        myCount += countWays(sr, sc+1, dr, dc)
    if sr + 1 <= dr:
        myCount += countWays(sr+1, sc, dr, dc)

    return myCount
    

ans = countWays(sr,sc,dr,dc)
print(ans)