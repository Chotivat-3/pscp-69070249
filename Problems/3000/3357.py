"""Magical Giraffe"""
n = int(input())
gi = []
if n == 1 :
    print(1)
else:
    out = 0
    for _ in range (n):
        gi.append(int(input()))
    for i in range(n):
        if not i:
            if gi[i] > gi[i+1]:
                out += 1
        elif i == n-1:
            if gi[i] > gi[i-1]:
                out += 1
        else:
            if gi[i-1] < gi[i] and gi[i] > gi[i+1]:
                out += 1
    print(out)
