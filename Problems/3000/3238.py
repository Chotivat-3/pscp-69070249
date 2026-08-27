"""X_SHAPE"""
num, kit = input().split()
num = int(num)
az = "abcdefghijklmnopqrstuvwxyz"
if kit not in az:
    az = az.upper()
HT = "#"*26

mid = num//2
if num%2 :
    mid += 1

def x(k,pit,n=num):
    """x-shape"""
    run = k
    if run > 25:
        run = run%26
    step = 0
    for i in range(1,n+1):
        if not n%2 and i == mid+1:
            continue
        if run in (-26, 26):
            run = 0
        run -= 1
        step += 1
        out = ''
        for j in range(1,n+1):
            if i in (j,n+1-j) :
                out += pit[run]
            else:
                out += "-"
        print(out)

        if not n%2 and i == mid:
            print(out)

        if step >= mid:
            run += 2

if kit == "#":
    ht_p = HT.rfind(kit)
    st = ht_p+ mid
    x(st,HT)
else:
    az_p = az.rfind(kit)
    st = az_p+ mid
    x(st,az)
