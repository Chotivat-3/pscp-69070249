x = int(input())
y = int(input())
d = int(input())
n=0
for i in range(x,y+1):
    if i%d == 0: # x if x == 0 run {if not x:}
        print(i,end=" ")
        n+=1
print('count='+str(n))
