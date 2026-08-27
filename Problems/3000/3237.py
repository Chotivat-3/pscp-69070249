"""01"""

n = int(input())

for i in range (1,n+1):
    out = "0"*i
    if i > 2 and i != n:
        out = "0"+"1"*(i-2)+"0"
    print(out)
