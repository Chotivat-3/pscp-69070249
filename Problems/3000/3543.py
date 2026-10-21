'''is prime'''

def myprime(n):
    '''is prime'''
    key = True
    for i in range(2,int(n**0.5)+1):
        if not n%i:
            key = False
            break
    if n>1 and key:
        print('Yes')
        out = []
        for i in range(2,n):
            for j in range(2,int(i**0.5)+1):
                if not i%j:
                    break
            else:
                out.append(i)
        print(*out, n)
    else:
        print('No')
myprime(int(input()))
