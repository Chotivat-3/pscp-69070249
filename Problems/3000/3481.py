'''ลอดช่องวัดเจด'''
l, n = map(int,input().split())

bridge = []
box = []
for i in range(n):
    x,y = map(int,input().split())
    bridge.append(range(x,y))

for i in range(1,l):
    ps = 0
    for j in bridge:
        if i in j:
            ps += 1
    box.append(ps)
if box:
    print(max(box))
else:
    print(1)
