"""Sell man"""
n = int(input())
car = []
out = 0

for _ in range(n):
    x,y = map(int,input().split())
    car.append((x,y))

def only_y(xy):
    return xy[1]
car.sort(key=only_y,reverse=True)
dele = []

for j in range (n):
    if j and car[j][0] > car[0][0] and car[j][1] < car[0][1]:
        dele.append[j]
        out += 1

for i in dele:
    car.remove(car[i])
n = len(car)

print(out)
