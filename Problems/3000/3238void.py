"""X_SHAPE"""
num, kit = input().split()
num = int(num)

mid = num//2
if num%2 :
    mid += 1

def x(k,n=num):
    """x-shape"""
    run = k
    if run > 126 :
        run -= 126-32
    for i in range(1,n+1):
        out = ''
        if not n%2 and i == mid+1:
            continue
        if i <= mid:
            run -= 1
            if run < 33 :
                run = 126
        if i > mid:
            run += 1
            if run > 126:
                run = 33
        for j in range(1,n+1):
            if i in (j,n+1-j) :
                out += chr(run)
            else:
                out += "-"
        print(out)
        if not n%2 and i == mid:
            print(out)
        #print("run =", run, i)
if kit != "#":
    st = ord(kit)+ mid
    x(st)
else:
    for z in range(1,num+1):
        htout = ''
        if not num%2 and z == mid+1:
            continue
        for y in range(1,num+1):
            if z in (y,num+1-y) :
                htout += "#"
            else:
                htout += "-"
        print(htout)
        if not num%2 and z == mid:
            print(htout)
