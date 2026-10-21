'''Bus'''
POW = int(input())
N = int(input())
itall = []
t_banner = []
my_pres = []
box_bus = []
out = 0

for _ in range(N):
    pres = list(map(int,input().split()))
    itall.append(pres)
itall.sort()
for i in range(N):
    t_banner.append(itall[i][0])
    my_pres.append(itall[i][1:])

for i in range(N):
    thisban = t_banner[i]
    thispres = my_pres[i]
    repres = []
    for pr in box_bus:
        if pr == thisban:
            out += 1
        else:
            repres.append(pr)
    box_bus = repres
    for p in thispres:
        if i != N-1 and p in t_banner[i+1:] and len(box_bus) < POW:
            box_bus.append(p)
print(out)
