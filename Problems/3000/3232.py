"""KERORO"""
x, y = map(int,input().split())
dis = x
n = 1

while True:
    if dis >= y:
        print(n)
        break
    if x <= 0:
        print(-1)
        break
    x -= 2
    dis += x
    n += 1
