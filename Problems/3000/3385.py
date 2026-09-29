'''Bus'''
p = int(input())
n = int(input())
box_bus = []
out = 0

for i in range(1,n+1):
    pres = list(map(int,input().split()))
    while i in box_bus:
        box_bus.remove(i)
        out += 1
    for j in pres[1:]:
        if j > i and len(box_bus) < p:
            box_bus.append(j)

print(out)

