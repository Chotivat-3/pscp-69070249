"""ARROW BOY"""

k = int(input())
n = int(input())

run = 0
mid = n//2+1

for i in range (1,n+1):
    if run < mid:
        run += 1
    if run >= mid:
        run -= 1
    print(" "*(run),end="")

    for _ in range (1,k+1):
        print("*",end="")
    print()
