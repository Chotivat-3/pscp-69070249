''' Wizard '''
N = int(input())
out = [0]*4
out.append(False)

def good1():
    """one or two"""
    score = list(map(int,input().split()))
    one, two = score[:3], score[3:]
    bet = [max(one[0],two[0]),max(one[1],two[1]),max(one[2],two[2])]
    out[0] += sum(bet)
    for i in range(3):
        out[i+1] += bet[i]

for _ in range(N):
    good1()

print(out)