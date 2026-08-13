"""SUM SUM"""
n = int(input())
couple = []
while n:
    x = int(input())
    y = int(input())
    couple.append(max(x,y))
    n -= 1

total_couple = sum(couple)
if len(couple) == 1:
    print(couple[0])
else:
    print(f"{" + ".join(list(map(str,couple)))} = {total_couple}")
