'''Muddled Menu'''
oder_list = []
num = []
while True:
    menu = input()
    if menu == 'DONE':
        break
    elif menu ==  "SOMETHING'S WRONG":
        oder_list.clear()
    elif 'Can\'t do:' in menu:
        num.pop(oder_list.index(menu[10:]))
        oder_list.remove(menu[10:])
    else:
        oder_list.append(menu[:len(menu)-3])
        num.append(menu[-1])
n = len(oder_list)
out = []
for i in range(n):
    out.append([oder_list[i],num[i]])

def sot(x):
    x = x[1]
    if x == 'N':
        x == 999**999
    else:
        x = int(x)
    return x

print(oder_list, num)
print(out.sort(key=sot))
