"""BUS SEAT"""
nr, nc, xx = int(input()), int(input()), int(input())
x = [[]]
for _ in range(nr-1):
    x.append([])

seat = 1
for i in range(nc):
    if i :
        seat += nr
    x[0].append(seat)

seat = x[0]

for j in range(1,nr):
    seat = list(map(lambda x:x+1,seat))
    x[j] = seat

x.reverse()

for e in x:
    for ix in range(nc):
        if e[ix]==xx:
            e[ix]='XX'
        else:
            e[ix]=f"{e[ix]:02d}"

run = 0
if nr%2:
    run += 1
for io in range(nr):
    run+=1
    print(" ".join(x[io]))
    if not run%2 and io != nr-1:
        print()
