"""PARKING"""

item = input().split(".")
t1 = int(item[0])
m1 = int(item[1])

item = input().split(".")
t2 = int(item[0])
m2 = int(item[1])

time = {1:25, 2:50, 3:80, 4:110, 5:145, 6:180, 7:250}
dis = t2*60+m2 - t1*60+m1

print(dis)
