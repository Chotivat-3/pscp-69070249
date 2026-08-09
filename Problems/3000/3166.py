"""Avr SCORE"""
n = int(input())
score = []
key = 1
while n:
    x = int(input())
    score.append(x)
    n -= 1

total_avr = sum(score)/len(score)

for i in score:
    if i < 50:
        key = 0
        break

if key and total_avr >= 60:
    print(f"{total_avr:.1f}")
    print("PASS")
else:
    print(f"{total_avr:.1f}")
    print("FAIL")
