"""Overlapping"""
import math as m
def cir():
    """Circle"""
    x1 = int(input())
    y1 =int(input())
    r1 = int(input())
    x2 = int(input())
    y2 =int(input())
    r2 = int(input())
    dis = m.sqrt((x2-x1)**2+(y2-y1)**2)
    dis = dis - (r1+r2)
    if dis <= 0:
        print("overlapping")
    else:
        print("no overlapping")
cir()
