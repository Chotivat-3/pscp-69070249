'''Q'''

n, l = map(int,input().split())
n_box = list(map(int,input().split()))
l_box = list(map(int,input().split()))
who = 0
tall = 0
for i in range(l):
    if l_box[i]-1 and n:
        who = n_box[l_box[i]-1]
        tall = max(n_box[:l_box[i]-1])
    if l_box[i]-1 and who <= tall:
        print(tall-who+1)
    else:
        print(0)
