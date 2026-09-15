'''Tuple'''
t = tuple(input().split())
f = input()
n = t.count(f)
k = t.index(f)
for _ in range(n):
    print(' '.join([str(k)] * n))
