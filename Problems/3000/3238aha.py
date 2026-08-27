"""X-Shape"""

num, kit = input().split()
num = int(num)
kit = ord(kit)
mid = [num//2+1,num//2+1]
if not num%2:
    mid[1] = (num//2)
mid = sorted(mid)
top = kit+mid[1] 


def x_shape (n1 = 1,n2 = num,run=kit):
    """XXXX"""

    for i in range (n1,n2):
        for j in range(1,num+1):
            if i in (j,num+1-j):
                print(chr(run-i+1), end ="")
            else:
                print("-", end ="")
        print()

x_shape(1,mid[0],top)
if not num%2 :
    x_shape(mid[0],mid[1]+1)
else:
    x_shape(mid[0],mid[0]+1)