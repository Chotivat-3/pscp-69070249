"""INFLATION"""

p = float(input())
p = int(p*100)
y = int(input())
for _ in range(y):

    p += p*381//10000

tp = p//100
rp = p%100

print(f"{tp}.{rp:02d}")
