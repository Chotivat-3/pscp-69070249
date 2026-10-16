"""WAD"""
import json
n = int(input())
Dih = {}
cat = 0
fox = 0
for _ in range(n):
    data = json.loads(input())
    Dih.update(data)

if "Garfield" not in Dih:
    if "Cat01" not in Dih.values():
        Dih["Garfield"] = "Cat01"

if "Fubuki" not in Dih:
    if "Fox01" not in Dih.values():
        Dih["Fubuki"] = "Fox01"

for name, code in Dih.items():
    if code.startswith("Cat"):
        cat += 1
    elif code.startswith("Fox"):
        fox += 1

print(f"Cat : {cat}")
print(f"Fox : {fox}")

cats = []
foxes = []

for name, code in Dih.items():
    if code.startswith("Cat"):
        cats.append((name, code))
    elif code.startswith("Fox"):
        foxes.append((name, code))
cats.sort(key=lambda x: x[1])
foxes.sort(key=lambda x: x[1])
for name, code in cats:
    print(f"{name} : {code}")
for name, code in foxes:
    print(f"{name} : {code}")