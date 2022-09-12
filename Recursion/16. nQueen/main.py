n = 4

chess = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]

def nQueen(chess, row)->int:
    if row == len(chess):
        return 1

    myAns = 0

    for col in range(len(chess)):
        if isQueenSafe(chess, row, col):
            chess[row][col] = 1
            myAns += nQueen(chess,row+1)
            chess[row][col] = 0
    
    return myAns


# helper function to see if Queen  is safe or not
def isQueenSafe(chess, row, col)-> bool:
    #1. row-1, col

    for r in range(row-1 , -1, -1):
        if chess[r][col] == 1:
            # print( r , col)
            return False
        
    #2. row-1, col + 1

    # for(r = row-1, c = col + 1 ; r > -1 && c < n ; r-- , c++)
    # for (i,j) in [(i,j) for i in range(x) for j in range(y) ]
    
    # for (r,c) in [(r,c) for r in range(row-1 , -1, -1) for c in range(col+1, n)]

    # print("loop 2")
    for (r,c) in [(r,c) for r in range(row-1 , -1, -1) for c in range(col+1, n)]:
        if chess[r][c] == 1:
            return False

    #3. row-1,col-1
    
    for (r,c) in [(r,c) for r in range(row-1 , -1, -1) for c in range(col-1, -1,-1)]:
        if chess[r][c] == 1:
            return False

    return True


    


ans = nQueen(chess, 0)  
print(ans)



