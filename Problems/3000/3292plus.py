"""ARROW วอดส์"""
T = input()
N = int(input())

def left():
    """left"""
    for i in range(N,1,-1):
        star = "*"*(i)
        space = " "*(i-1)
        print(f"{space}{star}")
    for i in range(1,N+1):
        star = "*"*(i)
        space = " "*(i-1)
        print(f"{space}{star}")

def right():
    """right"""
    for j in range(N,1,-1):
        star = "*"*(j)
        space = " "*(N-j)*2
        print(f"{space}{star}")
    for j in range(1,N+1):
        star = "*"*(j)
        space = " "*(N-j)*2
        print(f"{space}{star}")

n = len(T)
for o in range(n):
    if T[o] == "R":
        right()
        if o != n-1:
            print()
    if T[o] == "L":
        left()
        if o != n-1:
            print()
