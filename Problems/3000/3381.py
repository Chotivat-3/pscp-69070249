""" point sort """

def plus(x):
    '''plus'''
    push = sum(x)
    return push
def to_y(y):
    '''only Y'''
    return y[1]

T = int(input())

def soted():
    '''sorted'''
    out = []
    n = int(input())
    for _ in range(n):
        e1, e2 = map(int,input().split())
        e = e1, e2
        out.append(e)
    out.sort(key=to_y,reverse=True)
    out.sort(key=plus)
    return out

for _ in range(T):
    op = soted()
    for i in op:
        print(" ".join(list(map(str,i))))
