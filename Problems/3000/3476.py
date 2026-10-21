'''Cute Cat'''
from json import loads
n = int(input())
cat = {"Garfield":"Cat01"}
fox = {"Fubuki":"Fox01"}
for _ in range(n):
    in_put = loads(input())
    check = list(in_put.values())
    if 'Cat' in check[0] :
        if '01' in check[0] and "Garfield" in cat and cat["Garfield"] == "Cat01":
            cat.pop("Garfield")
        if 'Fubuki' in in_put:
            fox.pop("Fubuki")
        cat.update(in_put)
    else:
        if '01' in check[0] and "Fubuki" in fox and fox["Fubuki"] == "Fox01":
            fox.pop("Fubuki")
        if "Garfield" in in_put:
            cat.pop("Garfield")
        fox.update(in_put)

cat_key = list(cat.keys())
fox_key = list(fox.keys())
cat_fox = cat.copy()
cat_fox.update(fox)

def sot(x):
    '''sort'''
    x = cat_fox[x]
    x = int(x[3:])
    return x

cat_key.sort(key=sot)
fox_key.sort(key=sot)

print( "Cat :", len(cat))
print('Fox :', len(fox))

for i in cat_key:
    print(f"{i} : {cat[i]}")
for i in fox_key:
    print(f"{i} : {fox[i]}")
