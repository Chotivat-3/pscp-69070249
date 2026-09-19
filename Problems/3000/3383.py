"""SET"""
n, m = int(input()), int(input())
a = []
b = []

for _ in range (n):
    x = int(input())
    a.append(x)
for _ in range (m):
    x = int(input())
    b.append(x)

a, b = set(a),set(b)
out = list(a-b)
out.sort()

print(' '.join(list(map(str,out))))
