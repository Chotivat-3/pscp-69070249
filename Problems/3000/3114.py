"""PARKING"""
import datetime as dt
import math as m

item = input().split(".")
HR1 = int(item[0])
MI1 = int(item[1])

item = input().split(".")
HR2 = int(item[0])
MI2 = int(item[1])

def tt():
    """cal time"""
    tt1 = dt.datetime(1,1,1,HR1, MI1)
    tt2 = dt.datetime(1,1,1,HR2, MI2)
    return tt1,tt2

if HR1 < 0 or HR1 >=24 or HR2 < 0 or HR2 >= 24:
    OUT = "ERROR"
elif MI1 < 0 or MI1 >= 60 or MI2 < 0 or MI2 >= 60:
    OUT = "ERROR"
elif HR2 < HR1 or HR1==HR2 and MI2 < MI1:
    OUT = "ERROR"
else:
    t1,t2 = tt()

    minute = (t2 - t1).total_seconds()/60

    hr = m.ceil(minute/60)

    if hr > 7:
        hr =7
    time = {1:25, 2:50, 3:80, 4:110, 5:145, 6:180, 7:250}

    if minute <= 15 :
        OUT = "FREE"
    else:
        OUT = time[hr]

print(OUT)
