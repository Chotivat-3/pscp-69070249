"""LOTO BOY"""
# หน่วย สิบ ร้อย #
x,y,z = input(),input(),input()
key = ['==','!=','>','>=','<','<=']

xlist, ylist, zlist, out = [], [], [], []

def organize(o,olist):
    '''organ'''
    o1, o2 = o.split()
    o2 = int(o2)
    if key[0] == o1:
        olist.append(o2)
    if key[1] == o1 :
        for i in range (10):
            if i != o2:
                olist.append(i)
    if key[2] in o1:
        for i in range (10):
            if i == o2 and key[3] == o1:
                olist.append(i)
            if i > o2:
                olist.append(i)
    if key[4] in o1:
        for i in range (10):
            if i < o2:
                olist.append(i)
            if i == o2 and key[5] == o1:
                olist.append(i)
organize(x,xlist)
organize(y,ylist)
organize(z,zlist)
nx, ny, nz = len(xlist), len(ylist), len(zlist)
OVERALL = nx*ny*nz

for ii in range(nx):
    for j in range(ny):
        for k in range(nz):
            out.append(f"{zlist[k]}{ylist[j]}{xlist[ii]}")
out = list(map(int,out))
out.sort()
for iii in range(OVERALL):
    print(f"{out[iii]:03d}")
