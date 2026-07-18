"""Fence"""
info = input()
P = int(input())
info = info.split(" ")
W = int(info[0])
L = int(info[1])
N = int(info[2])
def cal ():
    """Fence"""
    fence = ((W+L)*2)*N
    total = (((W+L)*2)*N)*P
    print(f"{fence}\n{total}")
cal()
