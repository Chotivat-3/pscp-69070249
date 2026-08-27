"""LOT"""
tx, nx = input().split()
ty, ny = input().split()

if tx == ty and nx == ny:
    print(1000000)
elif tx != ty and nx == ny:
    print(100000)
elif tx == ty and nx[2:5] == ny[2:5]:
    print(2000)
elif tx == ty and nx[3:5] == ny[3:5]:
    print(1000)
elif tx != ty and nx[2:5] == ny[2:5]:
    print(200)
elif tx != ty and nx[3:5] == ny[3:5]:
    print(100)
elif tx == ty:
    print(20)
else:
    print(0)
