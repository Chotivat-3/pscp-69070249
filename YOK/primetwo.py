
n = int(input())

out = 0

for i in range(n+1):
    key = True
    for j in range(2,int(i**0.5)+1):
        if i % j == 0 :
            key = False
    if key and i >= 2 :
        print(i, end=" ")
        out += 1
print()
print('Total primes :',out)
