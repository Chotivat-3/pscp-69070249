"""HBD"""
def mm(m):
    """cal m"""
    m_= 0
    for i in range(m):
        if i+1 in [1,3,5,7,8,10,12]:
            m_ += 31
        elif i+1 == 2:
            m_ += 28
        else:
            m_ += 30
    return m_
y1 = int(input())
m1 = int(input())
d1 = int(input())
M1 = mm(m1)
t1 = y1*365 + M1 + d1
if not y1%4 and y1%100 or not y1%400 or y1 <= 1582 and not y1%4:
    t1 += 1
y2 = int(input())
m2 = int(input())
d2 = int(input())
M2 = mm(m2)
t2 = y2*365 + M2 + d2
if not y2%4 and y2%100 or not y2%400 or y2 <= 1582 and not y2%4:
    t2 += 1
if abs(t1 - t2) <= 7 :
    print(0)
elif t1 < t2 :
    print(1)
else :
    print(2)
