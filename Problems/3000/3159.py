"""Fac tor fac jai"""
n = int(input())
out = n

if not n:
    out = 1
else:
    n -= 1

while n:
    out *= n
    n -= 1

print(out)
