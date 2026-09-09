"""LOTO BOY"""
x,y,z = input(),input(),input()
def what(w):
    """WHATTT"""
    if ">" in w:
        if "=" in w:
            w = range(int(w[-1]),10)
        else:
            w = range(int(w[-1])-1,10)
    if "<" in w:
        if "=" in w:
            w = range(0,int(w[-1])+1)
        else:
            w = range(0,int(w[-1])-1)
    if "==" in w:
        w = range(int(w[-1]),int(w[-1])+1)
    return w
x = what(x)
y = what(y)
z = what(z)
nx, ny, nz = n = len(x), len(y), len(z)
n = len(x)*len(y)*len(z)
out = ['0']*n
