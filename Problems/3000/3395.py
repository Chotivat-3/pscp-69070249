n, l = map(int,input().split())
n_box = list(map(int,input().split()))
l_box = list(map(int,input().split()))
for i in range(l):
    pos = l_box[i] - 1
    if pos <= 0:
        print(0)
        continue
    who = n_box[pos]
    tall = max(n_box[:pos])
    if who <= tall:
        print(tall - who + 1)
    else:
        print(0)
    else:
        print(0)
