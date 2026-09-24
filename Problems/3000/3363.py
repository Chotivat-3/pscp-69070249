""" Spread !!! """

x, y = map(int,input().split())
box = []

for i in range(x):
    for j in range(y):
        box.append(0)

r1, r2 = map(int,input().split())

n = int(input())
vis = []
for i in range(n):
    e = list(map(int,input().split()))
    vis.append(e)

run = 0
for i in range(x):
    for j in range(y):
        for k in vis:
            if i==k[0] and j==k[1]:
                box[run] = 100
            elif abs(i-k[0])<=1 and abs(j-k[1])<=1:
                box[run] = max(60,box[run])
            elif abs(i-k[0])<=2 and abs(j-k[1])<=2:
                box[run] = max(20,box[run])
        run += 1

run = 0
print(box.count(0))
for i in range(x):
    for j in range(y):
        if i == r1 and j == r2:
            print(f"{box[run]}%")
        run += 1
