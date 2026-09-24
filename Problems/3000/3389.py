''' Smart collector '''
N = int(input())

def collect():
    '''collect'''
    out = []
    c = list(map(float,input().split()))
    c = list(map(lambda x: x*10, c))
    c = list(map(int,c))
    tpc = {0:[c[0],'Plastic'],1:[c[1],'Can'],2:[c[2],'Glass']}
    total = sum(c)
    out.append(f"{total//10}.{total%10}")
    if total > 500:
        out.append("Overloaded")
    for i in range(3):
        if tpc[i][0]>200:
            out.append(f"Check Type {tpc[i][1]}")
    return out

for _ in range(N):
    print(', '.join(collect()))
