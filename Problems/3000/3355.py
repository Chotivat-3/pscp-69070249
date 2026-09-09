"""REDUCE"""
t = []
out = []
while True:
    x = int(input())
    if x != -1:
        t.append(x)
    else:
        break
n = len(t)

for i in range(n):
    if i:
        if t[i] - t[i-1] > 1 :
            out.append(t[i])

print(t, out)