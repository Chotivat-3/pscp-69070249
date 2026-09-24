""" HA HA HA """

x, y, z = int(input()), int(input()), int(input())

t = [x, y, z]
tall = []

for i in range(3):
    j = t[:]
    if not i :
        j.sort(reverse=True)
        tall.append(j)
    elif i == 1:
        tall.append(j)
    else:
        j.sort()
        tall.append(j)

key = []
while True:
    n = int(input())
    if not n :
        break
    key.append(n-1)

n=len(key)

for i in range(n):
    print(f'Input number {key[i]+1} stored.')
    if not key[i]:
        print( f"Descending order: {" ".join(list(map(str,tall[key[i]])))}" )
    elif key[i] == 1:
        print( f"Original order: {" ".join(list(map(str,tall[key[i]])))}" )
    else:
        print( f"Ascending order: {" ".join(list(map(str,tall[key[i]])))}" )
