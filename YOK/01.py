x = int(input())
key = x
n = 0

while key:
    key//=10
    n+=1#นับเลข
key = x

x1 = key//10**(n-1)#ย่อรูป while
x2 = key%10
xx = x1+x2

print(n, x1, x2, xx)
