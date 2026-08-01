"""Promotion"""
item = input().split(" ")
p = int(item[0])
b = int(item[1])
c = int(item[2])
overall = p + b + c
out = p*25 + b*40 +c*55
if overall >= 3 :
    print(f"{out*90//100:.0f}")
else:
    print(out)
