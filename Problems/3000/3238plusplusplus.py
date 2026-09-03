"""X SHAPE"""
num, kit = input().split()
num = int(num)

for i in range(num):
    for j in range(num):
        if kit == "#":
            if i in (j-1,num - j):
                print(kit,end="")
            else:
                print("-",end ="")
        else:
            run = ord(kit) + abs(i - (num - 1)/2)
            if i in (j-1,num - j):
                print(chr(int(run)),end="")
            else:
                print("-",end ="")
    print()
