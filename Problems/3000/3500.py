'''Sairahat'''

def decode(code):
    '''rahat'''
    if not code.startswith('68'):
        return False
    if code[2:4] != '07':
        return False
    if code[4]!= '0' or int(code[5:]) not in range(1,329):
        return False
    return True
if decode(input()):
    print('Yes')
else :
    print('No')
