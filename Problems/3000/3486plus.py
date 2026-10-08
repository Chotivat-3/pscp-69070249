'''Bullet'''
from math import hypot, sqrt
def falling():
    '''my bull '''
    n = int(input())
    t= []
    for _ in range(n):
        x, y, d = map(int,input().split())
        t.append((x, y, d))
    
falling()
