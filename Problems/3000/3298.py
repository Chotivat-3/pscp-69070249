"""BUU"""
rab = input()
key = rab.lower()

out = ''
bumax = 0

if "buu" in key:
    check = "buu"
    while True:
        if check in key:
            bumax = check.count("u")
            check += "u"
        else:
            break
elif 'b' in key:
    n = key.find('b')
    lim = len(key)
    out = rab[:n+1]+'U'*(lim-n-1)
else:
    n = len(key)//3
    out += "BUU"*n
    rn = len(key)%3
    if rn == 1:
        out+="B"
    if rn == 2:
        out+="BU"

if bumax:
    out = f'Yes {bumax}'

print(out)
