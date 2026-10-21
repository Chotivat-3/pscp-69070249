'''star'''
def star(n):
    '''star'''
    print('*'*n)
    if n > 2:
        print('*'*(n-2))
    if n > 4:
        print('*'*(n-4))
star(int(input()))
