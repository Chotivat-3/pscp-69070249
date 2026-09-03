x = input()
y = int(input())
out = ''

for i in range(1,y+1):
    out += x*i
    if i!= y:
        out += ","

print(out)
