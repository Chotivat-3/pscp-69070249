''' Wizard '''
N = int(input())
out = [0]*4
out.append(False)

def good1():
    """one or two"""
    score = list(map(int,input().split()))
    one, two = score[:3], score[3:]
    bet = [max(sum(one),sum(two))]
    out[0] += bet[0]
    for i in range(3):
        if bet == sum(one):
            out[i+1] += one[i]
        else:
            out[i+1] += two[i]
for _ in range(N):
    good1()

if out[1] > out[2]+out[3]:
    out[4]=True

print(out)