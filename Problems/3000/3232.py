"""KERORO"""
x, y = map(int,input().split())

if not x%2:
    n = (x+2)/2
    xn = 0
else:
    n = (x+1)/2
    xn = 1

dis = n/2*(x+xn)

