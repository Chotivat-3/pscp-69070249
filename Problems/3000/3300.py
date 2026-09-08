"""Work life balance"""#But ตอนนี้ไม่น่านะคับ
n = int(input())
over = 0
ok = 0

resttime = '11'
nr = 0
balance = ''

for _ in range(n):
    x = int(input())
    if x > 18:
        over += 1
    else:
        ok += 1

while over or ok :
    if over:
        balance += '1'
        over -=1
    if ok:
        balance += '0'
        ok -= 1

while True:
    key = balance.find(resttime)
    if key != -1:
        nr = len(resttime)-1
    else:
        break
    resttime += "1"

print(len(balance)+nr)
