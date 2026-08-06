"""Swap"""

def swap(n,x):
    """Swap"""
    ns = str(n)
    ns = ns[::-1]
    ns = int(ns)

    if x == "+":
        print(f"{n} + {ns} = {n + ns}")
    elif x == "*":
        print(f"{n} * {ns} = {n*ns}")
swap(int(input()),input())
