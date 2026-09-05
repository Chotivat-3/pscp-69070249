x = int(input())

out = ''
total = 1
while x:
    total*=x
    if x != 1:
        out += str(x)+'*'
    else:
        out += str(x)
    x-=1
print(out+'='+str(total))
