"""Pot"""
pit = input().split(" ")
N = int(pit[0])
K = int(pit[1])
def cal (k=K,n=N):
    """cal_passenger"""
    n_k = k
    nn = 0
    k_list = []
    out_klist = []
    while n :
        r = int(input())
        k_list.append(r)
        n -= 1
    for _ in range(n_k):
        out_klist.append(0)
    for i in k_list:
        out_klist[i-1] += 1
    min_p = min(out_klist)
    while n_k :
        out_klist[nn] -= min_p
        nn += 1
        n_k -= 1
    print(sum(out_klist))
cal()
