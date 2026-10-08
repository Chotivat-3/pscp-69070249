'''Divide'''
n = int(input())
out = []
for i in range(1,n+1):
    if not i%3 or not i%5:
        out.append(i)
print(sum(out))
