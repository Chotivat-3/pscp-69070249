"""สหกรณ์ เอ้ะ?"""
from decimal import Decimal, ROUND_HALF_UP #ai ref ด้วย***

mem = input()
n = int(input())
out = Decimal("0")

while n :
    out += Decimal(input())
    n -= 1
if mem == 'Y':
    out = out*Decimal("0.95")
elif mem == 'N' and out >= 500 :
    out = out*Decimal("0.97")

##       กำหนดจุดปัดเศษ   2 ตำแหน่ง -> 0.01 บอกว่าจะปัดขึ้น

out = out.quantize(Decimal("0.01"),ROUND_HALF_UP)#ตรงนี้ๆ!

print(f"{out:.2f}")
