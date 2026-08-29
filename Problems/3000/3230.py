"""WH++HOTEL"""
n = input()
pit = 0
key_pit = False
one = ["9","10","11","12","14"]

while pit < 5:
    if int(n[pit]) > 5:
        key_pit = True
        break
    pit += 1

if key_pit:
    one = one[pit]
else:
    one = "13"

two = "0"
if n == n[::-1] and int(n[0]) + int(n[-1]) > 5:
    two = "1"
elif n == n[::-1] and int(n[1]) * int(n[-2]) > 5:
    two = "2"

if n != n[::-1] and not n[-1] and int(n[0]) // int(n[-1]) > 5:
    two = "1"
elif n != n[::-1] and int(n[1]) - int(n[-2]) > 5:
    two = "2"

tplus = 0
tmul = 1
three = "0"

for i in n:
    tplus += int(i)
    tmul *= int(i)
if tplus > 25:
    three = "1"
elif tmul > 55:
    three = "2"

print(one+two+three)
