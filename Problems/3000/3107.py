"""Bonus !!!"""
item = input().split(" ")
POSIT = item[0].upper()
WAGE = int(item[1])
SALARY = int(item[2])
DM = {1:6/100,2:8/100,3:10/100}
DB = {1:5/100,2:6/100,3:7/100}
DG = {1:4/100,2:5/100,3:6/100}
out = 0
def posit(p=POSIT):
    """position"""
    p_out = 0
    if p == "M":
        p_out += 1500
    elif p == "B":
        p_out += 1000
    elif p == "G":
        p_out += 500
    return p_out
out += posit()
def bonus(d,w=WAGE,s=SALARY):
    """bonus!!"""
    b_out = 0
    if w < 5:
        b_out += s*d[1]
    elif w <= 10:
        b_out += s*d[2]
    elif w > 10:
        b_out += s*d[3]
    return b_out
if POSIT == "M":
    out += bonus(DM)
elif POSIT == "B":
    out += bonus(DB)
elif POSIT == "G":
    out += bonus(DG)
print(f"{out:.0f}")
