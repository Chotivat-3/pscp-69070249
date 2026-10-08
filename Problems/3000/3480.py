'''Bird boy'''

n = int(input())
t = []
t.append(0)
t.extend(list(map(int,input().split())))
t.append(0)
love = 0

for i in range(1,n+1):
    if max(t[i-1],t[i],t[i+1]) == t[i]:
        love += 1
print(love)
