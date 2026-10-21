'''cal ver 2'''
def cal(n):
    '''cal ver 2'''
    if n == 1:
        return n
    out = n
    num = len(str(n))
    for i in range(1,num):
        out += i*9*10**(i-1)
    out += (n-10**(num-1) + 1)*num
    return out
print(cal(int(input())))
