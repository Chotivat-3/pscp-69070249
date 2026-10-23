'''RABBIRD'''

def rbd(n, leg):
    '''rbd'''
    if leg%2 or leg < n*2 or leg > n*4 :
        return 'Impossible'
# leg = r*4 + b*2, n = r+b ,r = n-b
# leg = 4n-2b, b = (4n-leg)//2
    b = (4*n-leg)//2
    return f"{n-b} {b}"

print(rbd(int(input()), int(input())))
