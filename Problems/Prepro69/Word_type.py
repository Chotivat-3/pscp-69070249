""" ขอร้อง """
def x ():
    """ ขอร้อง """
    x = str(input())
    x_1 = []
    G_ = {}
    x_1.extend(x.split())

    for x_1 in x_1 :
        k_ = ''.join(sorted(x_1))
        if k_ not in G_ :
            G_[k_] = []
        G_[k_].append(x_1)
    res = list(G_.values())
    print(res)
x()
