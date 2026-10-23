'''Full'''
def rerat(t):
    '''dace guy'''
    def sot(x):
        '''sot'''
        return t.find(x)
    myt = set()
    for i in t:
        myt.add(i)
    remain = []
    for i in myt:
        mycount = t.count(i)
        if mycount%2:
            remain.append(i)
    if remain:
        remain.sort(key=sot)
        return "".join(remain)
    return 'fully paired'
print(rerat(input()))
