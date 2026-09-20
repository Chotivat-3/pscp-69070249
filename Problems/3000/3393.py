'''Cave Explorer'''
size = int(input())
cave = input().split()
cod = cave.index('1')
walk = input()
for i in walk:
    cave[cod] = '0'
    if cod and i == 'L':
        cod -= 1
    if cod != size-1 and i == 'R':
        cod += 1
    if cave[cod] == '2':
        cave[cod] = '1'
        break
    cave[cod] = '1'
print(" ".join(cave))
