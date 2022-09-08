arr = [10,20,30,40,50]
idx = 0

def printEleForw(idx,arr):
    if idx == len(arr):
        return
    
    printEleForw(idx+1, arr)
    print(arr[idx])


printEleForw(idx,arr)
