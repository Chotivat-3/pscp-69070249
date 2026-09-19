'''prime'''

n = int(input())

def prime(x):
    '''prime'''
    if x < 2 :
        return False
    for i in range(2, int(x ** 0.5) +1):
        if x % i == 0:
            return False
    return True
out = 0
for j in range(n+1):
    if prime(j):
        print(j,end=' ')
        out += 1

print('Total primes :',out)
