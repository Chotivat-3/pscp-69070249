'''Muddled Menu'''
oder_list = []
menu, num = '',''
while True:
    put = input()
    if '#' in put:
        menu, num = put.rsplit(" #")
    if put == 'DONE':
        break
    if put == 'CLOSED':
        oder_list.clear()
        break
    if put ==  "SOMETHING'S WRONG":
        oder_list.clear()
    elif 'Can\'t do:' in put:
        oder_list.remove(put[10:])
    elif num.isdigit():
        oder_list.insert(int(num)-1,menu)
    elif num == 'N':
        oder_list.append(menu)

print('Full Course:', oder_list, 'Reversed:', oder_list[::-1])
