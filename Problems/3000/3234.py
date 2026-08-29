"""Crismak"""
tp, n = input().split()
pallet = ["Red","Green","Blue"]
out = ""
n = int(n)
k = 0

if tp == "G":
    k = 1
if tp == "B":
    k = 2

while n:
    out += pallet[k]+" "
    k += 1
    if k > 2:
        k=0
    n -= 1

print(out.rstrip())
