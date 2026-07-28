"""SAME?"""
n = int(input())
nn = int(input())
nnn = int(input())
if n == nn == nnn:
    print("all the same")
elif n==nn or n==nnn or nn==nnn:
    print("neither")
else:
    print("all different")
