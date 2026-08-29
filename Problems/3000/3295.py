"""Letric"""
n = int(input())

out = 0

if n > 200:
    out += n%200*15
    out += 100*12 + 50*10 + 40*7 + 10*5
elif n > 100:
    out += n%100*12
    out += 50*10 + 40*7 + 10*5
elif n > 50:
    out += n%50*10
    out += 40*7 + 10*5
elif n > 10:
    out += n%10*7
    out += 10*5
else:
    out += n*5

out += n*0.5
out += (out*7)/100

print(f"{out:.1f}")
