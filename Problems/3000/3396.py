'''แซงรอบ'''

n, t = map(int,input().split())
runner = []
out = set()
for i in range(n):
    runner.append(int(input()))
runner.sort()
out = [runner.pop(0)]

runnerver2 = list(map(lambda x:x*t,runner))

for i,v in enumerate(runnerver2):
    runnerver2[i] -= out[0]*t

    if runnerver2[i] < runner[i]:
        out.append(v//t)

print(len(out))
