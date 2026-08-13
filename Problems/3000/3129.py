"""Cafe lover"""
n = int(input())
n_day = n
soldout = 0

sold = int(input())
soldout += sold
mx = sold
mn = sold
n -= 1

while n :
    sold = int(input())
    soldout += sold
    if sold >= mx:
        mx = sold
    if sold <= mn:
        mn = sold
    n -= 1
print(soldout)
print(mx)
print(mn)
print(f"{soldout/n_day:.1f}")
