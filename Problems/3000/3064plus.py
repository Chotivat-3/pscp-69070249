"""HBD"""
def artid(y):
    """cal"""
    return not y%4 and y%100 or not y%400 or y <= 1582 and not y%4
y1 = int(input())*360
m1 = int(input())*30
d1 = int(input())
t1 = y1 + m1 + d1
y2 = int(input())*360
m2 = int(input())*30
d2 = int(input())
t2 = y2 + m2 + d2
if artid(y1) and artid(y2)and y1 == y2:
    if m1//30 == 2:
        t1 += 1
    if m2//30 == 2:
        t2 += 1
if abs(t1 - t2) <= 7 :
    print("0")
elif t1 < t2 :
    print("1")
else :
    print("2")
