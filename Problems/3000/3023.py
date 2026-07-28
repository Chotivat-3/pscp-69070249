"""Calculator"""
N = int(input())
NP = N - 1
NE = 1
def cal (n=N,np=NP,ne=NE):
    """Cal"""
    n_ = 0
    for i in range(1,n+1):
        n_ += len(str(i))
    n_total = n_  + np + ne
    if n == 1 :
        n_total = 1
    print(n_total)
cal()
