'''เข้าแถว'''

n, l = map(int,input().split())
q = list(map(int,input().split()))
t = list(map(int,input().split()))
spc = []
for i in t:
    spc.append(q[i-1])

for i in range(l):
    if not i:
        print(i)
    elif max(q[:q.index(spc[i])]) >= spc[i]:
        print(max(q[:q.index(spc[i])]) - spc[i] + 1)
    else:
        print(0)
