'''ball'''

def fall(m):
    '''ball'''
    m = m*100
    n = 1
    while True:
        if  m*((3/5)**n) < 1:
            return n-1
        n += 1
print(fall(float(input())))
