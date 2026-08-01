"""Ramen"""
out = 0

item = input().split(" ")
size = item[0].lower()
tase = item[1].lower()

ss = {"r":60,"t":80}
sm = {"r":80,"t":100}
sl = {"r":100,"t":120}

topitem = {"P":15,"E":10}

if size == "s":
    out += ss[tase]
if size == "m":
    out += sm[tase]
if size == "l":
    out += sl[tase]

item = input()
if item != "N":
    item = item.split(" ")
    top = item[0]
    n = int(item[1])
    out += n*topitem[top]

print(out)
