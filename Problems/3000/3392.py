""" HA HA HA """

arr = [0]*50
x, y, z = int(input()), int(input()), int(input())
put = (x, y, z)

for i in range(3):
    arr[i]= put[i]
    print(f'Input number {i+1} stored.')

while True:
    key = int(input())
    if not key:
        break
    if key == 1:
        print(f"Original order: {arr[0]} {arr[1]} {arr[2]}")
    elif key == 2:
        x = arr[:3]
        x.sort(reverse=True)
        x = list(map(str,x))
        print(f"Descending order: {' '.join(x)}")
    else:
        x = arr[:3]
        x.sort()
        x = list(map(str,x))
        print(f"Ascending order: {' '.join(x)}")
