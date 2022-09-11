n = 3

sr = 0
sc = 0
dr = n-1
dc = n-1

# sr-> sourceRow
# sc-> sourceCol
# dr-> destinationRow
# dc-> destinationCol

def mazePath(sr, sc, dr, dc, asf):
    if  sr == dr and sc == dc :
        print(asf)
        return

    if sc + 1 <= dc:
        mazePath(sr, sc+1, dr, dc, asf+"h")
    if sr + 1 <= dr:
        mazePath(sr+1, sc, dr, dc, asf+"v")

mazePath(sr, sc, dr, dc, "")
    
    


