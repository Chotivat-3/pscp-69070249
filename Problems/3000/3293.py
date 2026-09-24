"""Frame"""
n = 5
inout = []
while n:
    try:
        X = input()
    except EOFError:
        X = ""
    inout.append(X.strip())
    n -= 1

big = 0
for i in inout:
    if len(i) >= big:
        big = len(i)

for i in range(1,8):
    if i in(1,7):
        print("*"*(big)+"****",end="")
    else:
        key = big - len(inout[i-2])
        print("*",end=" ")
        print(inout[i-2],end=" ")
        if key:
            print(" "*key,end="")
        print("*",end="")
    print()
