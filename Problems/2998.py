"""Distance??"""
import math as m
def dis_(x1,x2,z1,z2):
    """Distance_"""
    x = (x1-z1)**2
    z = (x2-z2)**2
    d = m.sqrt(x+z)
    print(d)
dis_(float(input()),float(input()),float(input()),float(input()))
