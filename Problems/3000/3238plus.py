"""X_SHAPE"""
num, kit = input().split()
num = int(num)
az = "abcdefghijklmnopqrstuvwxyz"
if kit not in az:
    az = az.upper()
ht = "#"*26

mid = num//2
if num%2 :
    mid += 1

def x(k,pit,n=num):
    """x-shape"""
    run = k
    while run > 25:
        run -= 26
    step = 0
    for i in range(1,n+1):
        #print(run)
        if not n%2 and i == mid+1:
            continue
        if run == -26 or run == 26:
            run = 0
        run -= 1
        step += 1
        for j in range(1,n+1):
            if j == i or n+1 - j == i :
                print(pit[run],end="")
            else:
                print("-",end="")
        if not n%2 and i == mid:
            print()
            for j in range(1,n+1):
                if j == i or n+1 - j == i :
                    print(pit[run],end="")
                else:
                    print("-",end="")
        print()
        if step >= mid:
            run += 2

if kit == "#":
    ht_p = ht.rfind(kit)
    st = ht_p+ mid
    x(st,ht)
else:
    az_p = az.rfind(kit)
    st = az_p+ mid
    x(st,az)
