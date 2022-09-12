#flood fill

n = 5
m = 4

sr = 0
sc = 0
dr = n-1
dc = m-1

#2D maze
maze = [[0,1,0,0],[0,0,0,0],[0,1,0,0],[0,0,0,0],[1,0,1,0]]

def floodFill(maze, sr, sc , dr, dc, asf):
    #no entry
    if sr>dr or sr < 0 or sc > dc or sc < 0 or maze[sr][sc] == 1:
        return
    
    if sr == dr and sc == dc:
        print(asf)
        return

    maze[sr][sc] = 1    #mark
    #top
    floodFill(maze,sr-1,sc,dr,dc,asf+"t")
    #left
    floodFill(maze,sr,sc-1,dr,dc,asf+"l")
    #down
    floodFill(maze,sr+1,sc,dr,dc,asf+"d")
    #right
    floodFill(maze,sr,sc+1,dr,dc,asf+"r")
    maze[sr][sc] = 0    #unmark


def floodFillCount(maze, sr, sc , dr, dc) -> int:
    #no entry
    if sr>dr or sr < 0 or sc > dc or sc < 0 or maze[sr][sc] == 1:
        return 0
    
    if sr == dr and sc == dc:
        return 1

    myCount = 0

    maze[sr][sc] = 1    #mark
    #top
    myCount += floodFillCount(maze,sr-1,sc,dr,dc)
    #left
    myCount += floodFillCount(maze,sr,sc-1,dr,dc)
    #down
    myCount += floodFillCount(maze,sr+1,sc,dr,dc)
    #right
    myCount += floodFillCount(maze,sr,sc+1,dr,dc)
    maze[sr][sc] = 0    #unmark

    return myCount


floodFill(maze, sr, sc , dr, dc, "")
ans = floodFillCount(maze, sr, sc , dr, dc)

print(ans)