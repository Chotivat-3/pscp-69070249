def plus(x):
    out = sum(x)
    return out


d = []

for i in range(5):
    e,a = map(int,input().split())
    d.append([e,a])


print(d)

print(plus(d))