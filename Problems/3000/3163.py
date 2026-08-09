"""For what"""
n = int(input())
total = 0
ev = 0
od = 0

while n:
    x = int(input())
    total += x
    if not x % 2:
        ev += 1
    else:
        od += 1
    n -= 1

print("SUM", total)
print("EVEN", ev)
print("ODD", od)
