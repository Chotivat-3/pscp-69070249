"""Stat"""
n = int(input())

total = 0

for i in range(n):
    x = int(input())
    if not i:
        mx = x
        mn = x
    else:
        if x > mx:
            mx = x
        if x < mn:
            mn = x
    total += x

print(f"MIN: {mn:.3f}")
print(f"MAX: {mx:.3f}")
if n:
    print(f"AVG: {total/n:.3f}")
else:
    print("AVG: 0.000")
