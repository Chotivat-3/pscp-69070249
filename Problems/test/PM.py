"""PM"""
N = int(input())
over = 0
peak = 0
streak = ""
streak_out = 0
start = 0

for i in range(N):
    x = int(input())
    if not i :
        peak = x
    if x > peak:
        peak = x
    if x > 50 :
        streak += "1"
        over += 1
    else:
        streak += "0"

if over:
    check = "1"
    while True:
        if check in streak:
            streak_out = len(check)
            check+="1"
        else:
            break
    start = streak.rfind("1"*streak_out)+1

print(f"OVER = {over}")
print(f"PEAK = {peak}")
print(f"STREAK = {streak_out}")
print(f"START = {start}")
