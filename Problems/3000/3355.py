<<<<<<< HEAD
'''short'''
nl=[]
out = ''
while True:
    x = int(input())
    if x != -1:
        nl.append(x)
    else:
        break
n = len(nl)
if not nl:
    print()
elif n == 1:
    print(nl[0])
else:
    out = []
    out.append(nl[0])
    for i in range(n):
        if i and nl[i] - nl[i-1] == 1:
            try :
                if nl[i+1] - nl[i] > 1:
                    out.append(-1*nl[i])
            except IndexError:
                out.append(-1*nl[i])
        if i and nl[i] - nl[i-1] > 1:
            out.append(nl[i])
    n = len(out)
    for i in range(n):
        if not i :
            if out[i+1] < 0:
                print(out[i],end="")
            else:
                print(out[i],end=", ")
        elif i and i != n-1 and out[i+1]>0:
            print(out[i],end=", ")
        else:
            print(out[i],end="")
=======
"""REDUCE"""
t = []
out = []
while True:
    x = int(input())
    if x != -1:
        t.append(x)
    else:
        break
n = len(t)

for i in range(n):
    if i:
        if t[i] - t[i-1] > 1 :
            out.append(t[i])

print(t, out)
>>>>>>> 97cb694942951e23407b10d2facdd9b05d5aa456
