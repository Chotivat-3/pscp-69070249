"""Conan"""
text = input()
k = int(input())

KEY = "abcdefghijklmnopqrstuvwxyz"
out =""
for i in text:
    n = KEY.rfind(i)
    n += k
    while n > 25:
        n %= 26# 0-25 = 26 ตัว
    out += KEY[n]

print(out)
