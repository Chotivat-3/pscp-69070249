'''Car'''

n = int(input())
car = []
pr = []
out = 0
for i in range(n):
    x, y = input().split()
    c = y, x
    car.append(c)
    pr.append(x)

car.sort(reverse=True)
for i in range (n):
    if i != n-1 and car[i][1]<car[i+1][1]:
        out += 1
    if i == n-1 and car[i][1] > min(pr):
        out += 1
print(out)
