'''Destiny'''
r1 = input()
n1 = len(r1)
r2 = input()
n2 = len(r2)

def plus(x,y):
    '''plus'''
    nxy = 0
    while True:
        nx, ny = len(x) , len(y)
        if nx < ny:
            x += x[nxy]
            nxy += 1
        else:
            break
    return x

if n1 < n2:
    r1 = plus(r1, r2)
elif n1 > n2:
    r2 = plus(r2, r1)

def coutlove(t1,t2):
    '''coutlove'''
    n = len(t1)
    re = ''
    for i in range(n):
        if t1[i] in "loveLOVE" or t2[i] in "loveLOVE":
            re += 'w'
        else:
            re += '$'
    return re

destiny = coutlove(r1,r2)

KEYW = destiny.count('w')

if not KEYW%2 and 'ww' not in destiny:
    destiny += '#'

if KEYW%2 :
    key = 'w'
    pit = 0
    while key in destiny:
        pit = len(key)
        key += 'w'
    destiny += str(pit)

print(destiny)
