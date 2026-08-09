"""Specific"""
x, y = map(int,input().split())
spec = []
for i in range(x,y+1):
    if i % 2 and i % 3 and i % 5 and i % 7 and i != 1:
        spec.append(i)
    if i in [2,3,5,7]:
        spec.append(i)
spec = list(map(str,spec))
if spec:
    print(' '.join(spec))
print(f"Total primes: {len(spec)}")
