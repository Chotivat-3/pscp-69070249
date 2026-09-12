"""Bow BOW BOOOO!!"""
n = int(input())
boo = []
for _ in range (n):
    bow = input()
    boo.append(bow)
becheck = []
for i in boo:
    becheck.append(boo.count(i))
print(max(becheck))
