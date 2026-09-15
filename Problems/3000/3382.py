'''BackARD'''
out = []

while True:
    x = input()
    if x == 'NULL':
        break
    out.append(x)
out = out[::-1]
for i in out:
    print(i)
