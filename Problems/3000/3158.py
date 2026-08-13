"""Power up"""
n = int(input())
out = 0
while n:
    out += n**2
    n -= 1
print(out)
