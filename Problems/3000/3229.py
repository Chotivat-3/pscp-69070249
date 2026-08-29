"""Game point"""
p = int(input())
b = int(input())
p += b
d = int(input())

rk = 1
co = 0

if d > 3:
    p *= 1.5
    p = int(p)

if p >= 1500:
    rk = 5
elif p >= 1000:
    rk = 4
elif p >= 500:
    rk = 3
elif p >= 200:
    rk = 2

if rk == 5 and d >= 7 :
    co = 99
elif rk == 4 and b > 300:
    co = 88

print(p)
print(rk)
print(co)
