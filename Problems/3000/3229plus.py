"""Game counting"""
base = int(input())
bonus = int(input())
day = int(input())

total = base + bonus
if day > 3:
    total *= 1.5
    total = int(total)

print(total)
rk = 1
cd = 0

if total >= 1500:
    rk = 5
    if day >= 7:
        cd = 99
elif total >= 1000:
    rk = 4
    if bonus > 300:
        cd = 88
elif total >= 500:
    rk = 3
elif total >= 200:
    rk = 2

print(rk)
print(cd)
