arr = [10,20,30,40,50]
idx = 0

def printEleForw(idx,arr):
    if idx == len(arr):
        return
    
    print(arr[idx])
    printEleForw(idx+1, arr)


printEleForw(idx,arr)
