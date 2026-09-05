"""ARROW BOY"""

k = int(input())
n = int(input())

mid = n//2+1

for i in range (1,n+1):
    if i < mid:
        print(" "*(mid - i),end="")
    if i > mid:
        print(" "*(i - mid),end="")
    for _ in range (1,k+1):
        print("*",end="")
    print()
