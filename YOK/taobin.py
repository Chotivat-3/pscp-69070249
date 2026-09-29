'''Tao'''

n = int(input())
m = int(input())
t = []
for i in range(n):
    x = []
    for j in range(m):
        x.append(int(input()))
    t.append(x)
st1 = int(input())
st2 = int(input())

for i in t:
    print(i)

while True:
    t_more = [-99]*4
    if st1 + 1 < n:
        t_more[0]=t[st1+1][st2]
    if st1 - 1 >= 0:
        t_more[1]=t[st1-1][st2]
    if st2 + 1 < m:
        t_more[2]=t[st1][st2+1]
    if st2 - 1 >= 0:
        t_more[3]=t[st1][st2-1]
    
    t_more2 = t_more[:]
    t_more2.sort()
    t_more2 = t_more2[-1]

    #pit = t_more.index(t_more2)
    for i in range (len(t_more)):
        if t_more[i]==t_more2:
            pit=i
    print(t_more, t_more2, pit)
    if t[st1][st2] < t_more2:
        if pit == 0:
            st1+=1
        if pit == 1:
            st1 -=1
        if pit == 2:
            st2 +=1
        if pit == 3:
            st2 -=1
    else:
        break

print(st1, st2)
print(t[st1][st2])
check = t[0][0]
for i in range(n):
    for j in range(m):
        if t[i][j] >= check :
            check = t[i][j]
if t[st1][st2] == check:
    print('Iced Americano, no sugar')
else:
    print('Hot Latte 300% sweetness')
