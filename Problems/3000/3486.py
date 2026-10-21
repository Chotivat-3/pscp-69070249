'''Bullet'''
from math import hypot, sqrt
def falling():
    '''my bull '''
    n = int(input())
    t= []
    for _ in range(n):
        x, y, d = map(int,input().split())
        t.append([d, x, y])
    t.sort()
    def check(put):
        '''check'''
        re = [put[1],put[2]]
        for i in range(1,1001):
            if put[0] == hypot(put[1]+i,put[2]):
                re[0] = i
                return re
            if put[0] == hypot(put[1],put[2]+i):
                re[1] = i
                return re
            if put[0] == hypot(put[1]+i,put[2]+i):
                re[0] = i
                re[1] = i
                return re
            if put[0] == hypot(put[1]-i,put[2]):
                re[0] = i
                return re
            if put[0] == hypot(put[1],put[2]-i):
                re[1] = i
                return re
            if put[0] == hypot(put[1]-i,put[2]-i):
                re[0] = i
                re[1] = i
                return re
            if put[0] == hypot(put[1]-i,put[2]+i):
                re[0] = i
                re[1] = i
                return re
            if put[0] == hypot(put[1]+i,put[2]-i):
                re[0] = i
                re[1] = i
                return re
        return 0
    for i in t:
        myans = check(i)
        if myans:
            print(" ".join(list(map(str,myans))))
            break
falling()
