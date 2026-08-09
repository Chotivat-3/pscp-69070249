"""WALK"""
walk = input()
x = 0
y = 0
for i in walk:
    if i == "N":
        y += 1
    if i == "S":
        y -= 1
    if i == "E":
        x += 1
    if i == "W":
        x -= 1
print(f"{x} {y} {abs(x)+abs(y)}")
