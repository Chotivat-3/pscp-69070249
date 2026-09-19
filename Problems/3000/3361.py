'''Car'''

n = int(input())

car = []
pr = []
out = 0

for i in range(n):
    x, y = map(int,input().split())
    pr.append(x)
    car.append(y)

car = car[::-1]
check = car[0]

for i in range (1,n):
    if check < car[i] :
        check = car[i]
    else:
        out += 1

print(out)
