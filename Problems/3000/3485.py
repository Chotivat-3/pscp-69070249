'''Only One'''

def only():
    '''one'''
    n = int(input())
    out = []
    myitems = list(map(int,input().split()))
    myitems.sort()
    for i in range(n):
        if myitems.count(myitems[i]) == 1:
            out.append(myitems[i])
    print(" ".join(list(map(str,out))))
only()
