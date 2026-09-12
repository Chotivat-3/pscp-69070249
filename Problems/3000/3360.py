'''Bread'''
w, h, m, n = map(int,input().split())

mlist = list(map(int,input().split()))
mm = []
mm.append(mlist[0])

nlist = list(map(int,input().split()))
nn = []
nn.append(nlist[0])

outlist = []

def cut(num,elist,topright):
    '''cut cut'''
    t = []
    for i in range(1,num):
        t.append(elist[i]-elist[i-1])
        if i == num-1:
            t.append(topright-elist[i])
    return t
if m>1:
    mm.extend(cut(m,mlist,w))
else:
    mm.append(w-mlist[0])
if n>1:
    nn.extend(cut(n,nlist,h))
else:
    nn.append(h-nlist[0])

for j in mm:
    for k in nn:
        outlist.append(j*k)
outlist.sort(reverse=True)
print(outlist[0], outlist[1])
