"""ARROW วอดส์"""
T = input()
N = int(input())

def left():
    """left"""
    for i in range(N,1,-1):
        star = "*"*(i)
        space = " "*(i)
        print(f"{space}{star}")
    for i in range(1,N+1):
        star = "*"*(i)
        space = " "*(i)
        print(f"{space}{star}")

def right():
    """right"""
    for i in range(N,1,-1):
        star = "*"*(i)
        space = " "*(N-i)*2
        print(f"{space}{star}")
    for i in range(1,N+1):
        star = "*"*(i)
        space = " "*(N-i)*2
        print(f"{space}{star}")

if T == "RL":
    right()
    left()
if T == "LR":
    left()
    right()
if T == "L":
    left()
if T == "R":
    right()
