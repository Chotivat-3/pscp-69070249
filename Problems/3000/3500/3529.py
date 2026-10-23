'''Shift'''
def detext(t):
    '''detext'''
    check = {"what", "when", "why", "which", "who",
             "this", "there", "where", "the", 
             "is", "am", "are", "you", "we", 
             "they", "he", "she", "it", 'hi', 'hello'
             }

    atoz = 'abcdefghijklmnopqrstuvwxyz'
    atozup = atoz.upper()
    myt = t
    out = ''
    while True:
        out = ''
        for i in myt:
            if i in atoz:
                run = int(atoz.find(i))-1
                if run <= -1 :
                    run = 25
                out += atoz[run]
            elif i in atozup:
                run = int(atozup.find(i))-1
                if run <= -1 :
                    run = 25
                out += atozup[run]
            else:
                out += i
        myt = out
        for i in check:
            if i in out.lower().split()[::-1] and len(i) >= 3 :
                return out
print(detext(input()))
