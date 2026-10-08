'''Cir Reg'''
from math import pi
r, a, b = float(input()), float(input()), float(input())
cir = 2*pi*r
reg = (a+b)*2
out = ''
if cir == reg:
    out = 'Equal'
elif cir > reg:
    out = 'Circle is longer'
else:
    out = 'Rectangle is longer'
print(out)
print(f"{abs(cir-reg):.5f}")
