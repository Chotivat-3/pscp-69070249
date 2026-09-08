"""Letric"""
n = int(input())

out = 0

if n > 200:
    out += (n-200)*15
    out += 1200 + 500 + 280 + 50
elif n > 100:
    out += (n-100)*12
    out += 500 + 280 + 50
elif n > 50:
    out += (n-50)*10
    out += 280 + 50
elif n > 10:
    out += (n-10)*7
    out += 50
else:
    out += n*5

out *= 100
vat = (out*7/10000)*100
ft = n*100//2

out = out + vat + ft
rm = int(out%100//10)
out = int(out//100)

print(f"{out}.{rm}")
