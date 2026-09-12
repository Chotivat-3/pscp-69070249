"""INFLATION"""
k,n = float(input()),int(input())
out = int((k*100))
###      *100 ทั้งบน ทั้ง ล่าง ###
for _ in range(n):
    out += out*381//10000
print(f"{out//100}.{out%100:02d}")
