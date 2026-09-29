'''ham ham'''
t1, t2, out =input(), input(), 0
n = len(t1)
for i in range(n):
    if t1[i] != t2[i]:
        out+=1
print(out)
