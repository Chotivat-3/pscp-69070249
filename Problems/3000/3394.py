"""Go NExt"""
n, s = map(int,input().split())
student = [0]*n
for i in range(n):
    student[i]=int(input())
let_go = []
def go(st,std,lg):
    '''GoGO NAKA'''
    lg.append(std[st-1])
    print(let_go)
    if not std[st-1]:
        return -1
    if  st not in lg:
        std.pop(st-1)
        return 1

output = 1
while True:
    bk = go(s, student, let_go)
    if bk == -1 :
        break
    else:
        output += bk
    s += 1

print(output)
