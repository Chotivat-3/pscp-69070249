a  = 'aa #1'
out = []
pit = -1
for i in a:
    pit += 1
    if i.isdigit() or i == 'N':
        break
out.append(a[:pit-2])
out.append(a[pit:])
print(out)
