"""Flower Boy"""

l, n = map(int,input().split())

totalpush = 0
pushin = 0
run = 1

RE = l*(l+1)/2#อนุกรม
totalpush += RE #first_one

while True:#sec_two...end
    if totalpush >= n:
        break
    run += 1
    pushin += l**2*(run-1) + RE
    totalpush += pushin
    pushin = 0

print(run)
