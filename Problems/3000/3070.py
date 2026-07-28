"""ODD EVEN"""
n = int(input())
nn = int(input())
nnn = int(input())
even = 0
if not n%2:
    even += 1
if not nn%2:
    even += 1
if not nnn%2:
    even += 1
print(even)
print(3-even)
