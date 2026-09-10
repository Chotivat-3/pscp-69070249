"""RAB BRO"""
rab = input()
n = len(rab)
key = True
out = ''
pit = []

for i in range(n):
    if not i and rab[i] in 'aA':
        key = False
        pit.append(i)
        break
    if rab[i].lower() not in 'rabit':
        key = False
        pit.append(i)
        break
    if i != n-1 :
        if rab[i] in 'bB' and rab[i+1]not in 'iItT':
            key = False
            pit.append(i+1)
            break
        if i != n-1 and rab[i] in 'rR' and rab[i+1] not in 'aA':
            key = False
            pit.append(i+1)
            break
    if i :
        if rab[i] in 'aA' and rab[i-1] not in 'aArR':
            key = False
            pit.append(i)
            break
if key:
    aout = 0
    check = 'r'
    if 'ra' in rab.lower() or 'b' in rab.lower() and n > 1:
        for i in range(n):
            check += 'a'
            if check in rab.lower():
                aout += 1
        out = f'yes {aout}'
    else:
        if n == 1 and rab not in 'iItT':
            out = 'no 0'
        else:
            out = f'unknown {n}'
else:
    out = f'no {min(pit)}'

print(out)
