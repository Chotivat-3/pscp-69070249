''' Wizard '''
N = int(input())
out = [0]*4
out.append('NO')

def good1():
    """one or two"""
    score = list(map(int,input().split()))
    one, two = score[:3], score[3:]
    bet = [max(one[i], two[i]) for i in range(3)]
    out[0] += sum(bet)
    for i in range(1,4):
        out[i]+=bet[i-1]

for _ in range(N):
    good1()

if out[1] > out[2]+out[3]:
    out[4]='YES'

print('Total:',out[0])
print('Fire:', out[1])
print('Water:', out[2])
print('Earth:', out[3])
print('Bonus:', out[4])
