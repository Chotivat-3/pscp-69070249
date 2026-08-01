"""HBD"""
import datetime as d
y1 = int(input())
m1 = int(input())
d1 = int(input())
y2 = int(input())
m2 = int(input())
d2 = int(input())
t1 = d.date(y1,m1,d1)
t2 = d.date(y2,m2,d2)
dif = t1-t2
#print(dif)
dif = abs(dif.days)
if dif > 7 :
    if t1 < t2 :
        print("1")
    else :
        print("2")
else:
    print("0")
