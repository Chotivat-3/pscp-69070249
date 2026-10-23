'''med'''

def med(t):
    '''med'''
    myt=list(map(float,t.split(', ')))
    myt.sort()
    num = len(myt)
    if num%2:
        out = int((myt[num//2])*100)
    else:
        out = int((myt[num//2-1])*100 + (myt[num//2])*100)
        out //= 2
    main = out//100
    remain = out%100
    return f"{main}.{remain:02d}"
print(med(input()))
