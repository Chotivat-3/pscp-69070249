"""สหกรณ์"""
from math import ceil
mem = input().lower()
n = int(input())
out = 0
while n :
    out += float(input())
    n -= 1
if mem == 'y':
    out = out*(95/100)
elif mem == 'n' and out >= 500 :
    out = out*(97/100)
out = ceil(out*100)/100
out = f"{out:.2f}"
print(out)