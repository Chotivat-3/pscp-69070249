"""Theif"""
n, k, t = map(int,input().split())

x = 1
turn = 0
if t== 1:
    turn = 1
else:
    while True:
        x += k
        if x >= n:
            x -= n
        turn += 1
        if x == 1 :
            break
        if x == t:
            turn += 1
            break

print(turn)
