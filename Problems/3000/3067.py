"""DE/IN?"""
n = float(input())
nn = float(input())
nnn = float(input())
if n < nn < nnn:
    print("increasing")
elif nnn < nn < n:
    print("decreasing")
else:
    print("neither")
