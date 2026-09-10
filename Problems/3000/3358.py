"""PIGGY PIG"""
n = int(input())
pig = list(map(int,input().split()))
if n == 1:
    print(max(pig))
else:
    out = 0
    for i in range(0,n*2,2):
        x, y = pig[i], pig[i+1]
        out += max(x,y)
        if i != n*2-2:
            print(str(max(x,y)),end=" + ")
        else:
            print(str(max(x,y)),end=" = ")
            print(out)
