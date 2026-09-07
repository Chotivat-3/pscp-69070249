x,k= input().split()
x = int(x)
start = ord(k)+(x/2)
if k == "#":
    for i in range(1,x+1):
        for j in range(1,x+1):
            if j in (i,x+1-i):
                print(k,end="")
            else:
                print("-",end="")
        print()