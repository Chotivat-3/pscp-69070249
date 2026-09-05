n = int(input())
while n<= 0:
    n = int(input())

for i in range (1,n+1):
    out = i
    if not i%15:
        out = 'Fizz Buzz'
    elif not i%5:
        out = 'Buzz'
    elif not i%3:
        out = 'Fizz'
    if i != n:
        print(out,end=" ")
    else:
        print(out)
