"""PM SO SAD"""

n = int(input())
over = 0
peak = 0

cur_stack = 0
max_stack = 0

start = 0

for i in range(1,n+1):
    x = int(input())
    if i == 1:
        peak = x
    if x > peak :
        peak = x
    if x > 50 :
        over += 1
        cur_stack += 1
        if not start:
            start = i
    else :
        if cur_stack >= max_stack:
            max_stack = cur_stack
            if i > start :
                start = i
            cur_stack = 0

print(f"OVER = {over}")
print(f"PEAK = {peak}")
print(f"STREAK = {max_stack}")
print(f"START = {start}")
