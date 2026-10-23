'''GCD'''

def gcd(a,b):
    '''gcd'''
    myre = -1
    while True:
        if not b:
            return a
        myre = a%b
        if not myre:
            return b
        a = b
        b = myre
print(gcd(int(input()), int(input())))
