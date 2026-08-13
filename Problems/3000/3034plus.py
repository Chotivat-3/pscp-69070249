"""POT"""
n, k = map(int,input().split())
pot = []
for _ in range(k):
    pot.append(0)

while n:
    p = int(input())
    pot[p-1] += 1
    n -= 1
mn = min(pot)

while n < k:
    pot[n] -= mn
    n += 1

print(sum(pot))
