'''febo'''

def f(n):
    '''febo'''
    if not n:
        return 0
    if n == 1:
        return 1
    return f(n-1)+f(n-2)
print(f(int(input())))
