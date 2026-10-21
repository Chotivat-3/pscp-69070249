'''Cut Cut'''
def cutbread():
    '''my cut boy'''
    w, h, m, n = map(int,input().split())
    disx = [int(i) for i in input().split()]
    disx = [disx[i] if not i else disx[i]-disx[i-1] for i in range(m)]
    disx.append(w-sum(disx))
    disy = [int(i) for i in input().split()]
    disy = [disy[i] if not i else disy[i]-disy[i-1] for i in range(n)]
    disy.append(h-sum(disy))
    out = []
    for x in disx:
        for y in disy:
            out.append(x*y)
    out.sort(reverse=True)
    return out[0], out[1]
print(*cutbread())
