"""Milk TEA!!! LUV IT"""

item = input().split(" ")
top = item[0].upper()
v_top = float(item[1])

top_item = {"H":5,"O":3,"J":2}
out = v_top*top_item[top]

item = input().split(" ")
tea = item[0].upper()
sweat = int(item[1])
v_tea = float(item[2])

swr = [12, 18, 25]
swt = [15, 20, 30]
swm = [10, 15, 20]

def cal (switem,sw=sweat,v=v_tea):
    """cal sweat!!"""
    sw_out = v*switem[sw-1]
    return sw_out

if tea == "R":
    out += cal(swr)
if tea == "T":
    out += cal(swt)
if tea == "M":
    out += cal(swm)

if not out%1 :
    print(f"{out:.0f}")
else:
    print(out)
