"""INFLATION"""

p = float(input())
y = int(input())

for _ in range(y):

    p += p*3.81/100
    bp, sp = str(p).split(".")
    bp = int(bp)
    sp = int(sp[:2])
    p = bp+sp/100

print(f"{p:.2f}")
