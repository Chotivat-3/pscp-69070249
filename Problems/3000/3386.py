''' Spy girl huh? '''
m , n = int(input()), int(input())
tm, tn, out_spy = [], [], []
for i in range (m):
    x = int(input())
    tm.append(x)
for j in range (n):
    y = int(input())
    tn.append(y)

for i in tm:
    for j in tn:
        if i == j:
            out_spy.append(i)

if out_spy:
    out_spy.sort(reverse=True)
    for i in out_spy:
        print(i)
else:
    print('Nope')
