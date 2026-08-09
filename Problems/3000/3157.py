"""สะสมแต้ม"""
out = 0
n = int(input())
while n:
    x = input()
    if x == "+":
        out += 10
    if x == "-":
        out -= 5
    n-=1
print(out)
