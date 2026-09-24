""" HA HA HA """

arr = [0]*3
x, y, z = int(input()), int(input()), int(input())
arr[0], arr[1], arr[2] = x, y, z

for i in range(3):
    print(f'Input number {i+1} stored.')

while True:
    key = int(input())
    if not key:
        break
    if key == 1:
        print(f"Original order: {arr[0]} {arr[1]} {arr[2]}")
    elif key == 2:
        x = arr[:]
        x.sort(reverse=True)
        print(f"Descending order: {' '.join(map(str, x))}")
    else:
        x = arr[:]
        x.sort()
        print(f"Ascending order: {' '.join(map(str, x))}")

