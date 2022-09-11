str = "65616"       #also try "612"

def decodeWays(str, ans):
    if len(str) == 0:
        print(ans)
        return
    

    #str of atleast one len exists
    if str[0] == '0':
        return

    
    #str of atleast one len exists not starting with zero
    ch = str[0]     #str wala six
    intCh = int(ch) #int wala six

    #firstCall
    decodeWays(str[1:] , ans + chr(ord('a') + intCh -1))        #(5616,f)

    if len(str) > 1:
        #maybe 2nd call appicable
        #It will be only applicable if char[0] + char[1] <= 26

        ch2 = str[1]
        intCh2 = int(ch2)

        val = int(ch + ch2)

        if val <= 26:
            decodeWays(str[2:] , ans + chr(ord('a') + val -1))

    





    






decodeWays(str, "")

