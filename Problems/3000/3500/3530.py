'''SqFree'''
def sq(n):
    '''Sqfree'''
    mynum, out = set(i for i in range(1,n+1)), set()
    for num in mynum:
        for myr in range(2,int(n**(1/2))+1):
            if not num%myr**2:
                out.add(num)
                break
    return len(mynum.difference(out))
print(sq(int(input())))
