"""Is PRIME"""

def isprime(num):
    '''is prime'''
    if num == 1:
        return 'NO'
    for i in range(2,int(num**0.5)+1):
        if not num % i:
            return 'NO'
    return 'YES'
print(isprime(int(input())))
