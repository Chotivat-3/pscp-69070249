"""Check Check !! Boom!"""
n_shop,n_check = map(int,input().split(" "))
item = []
while n_shop:
    item.append(input())
    n_shop -= 1

check = list(map(int,input().split(" ")))

c_t = []
out = [0]*n_check

for i in item:
    x,y = map(int,i.split(" "))
    time = range(x,y)
    c_t.append(time)

for i in c_t:
    for j in range(n_check):
        if check[j] in i:
            out[j]+=1

out = list(map(str,out))
print(" ".join(out))
