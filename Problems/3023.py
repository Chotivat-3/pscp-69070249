"""Calculator"""
N = int(input())
NP = N - 1
NE = 1
def cal (n=N,np=NP,ne=NE):
    """Cal"""
    for i in range(1,n+1):
        if i >= 10:
            n += 1
        if i >= 100:
            n += 1
        if i >= 1000:
            n += 1
        if i >= 10000:
            n += 1
        if i >= 100000:
            n += 1
    n_total = n + np + ne
    if n == 1 :
        n_total = 1
    print(n_total)
cal()
