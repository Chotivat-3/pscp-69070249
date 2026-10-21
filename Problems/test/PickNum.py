'''pick num'''

t = list(map(int,input().split()))
pos, neg, ze = 0, 0, 0
for i in t:
    if not i:
        ze += 1
    if i > 0:
        pos += 1
    if i < 0:
        neg += 1
print(f"Positive: {pos}")
print(f"Negative: {neg}")
print(f"Zero: {ze}")
