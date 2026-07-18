"""Heron guy!"""
import math as m
def heron_(a,b,c):
    """Heron"""
    s = (a+b+c)/2
    area = m.sqrt(s*(s-a)*(s-b)*(s-c))
    area = round(area, 3)
    print(f"{area:.3f}")
heron_(float(input()),float(input()),float(input()))
