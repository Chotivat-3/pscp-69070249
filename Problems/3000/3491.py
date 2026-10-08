'''RunGame'''
try :
    run = list(map(int,input().split()))
except EOFError:
    run = [0]
out = 0
for i,dis in enumerate(run):
    if not i :
        out += abs(dis)
    else :
        out += abs(dis-run[i-1])
print(out)
