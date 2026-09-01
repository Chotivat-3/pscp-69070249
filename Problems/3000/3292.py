"""ARROW BOY"""
T = input().upper()
n = int(input())

MID = n
n = n*2 - 1

def left(num = n,mid=MID):
    """AL"""
    for i in range(1,num+1):
        if i <= mid :
            print(" "*(mid - i),end="")
            print("*"*(mid - i+1),end="")
        if i > mid :
            print(" "*(i - mid),end="")
            print("*"*(i - mid+1),end="")
        print()

def right(nn = n,mm=MID):
    """AR"""
    run = 1
    for i in range(1,nn+1):
        if i <= mm :
            if i != 1:
                print(" "*(i-1)*2,end="")
            print("*"*(mm - i+1),end="")
        if i > mm :
            run += 1
            if i != nn:
                print(" "*(mm - run)*2,end="")
            print("*"*(i - mm+1),end="")
        print()

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
