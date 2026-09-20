c = list(map(float,input().split()))
c = list(map(lambda x: x*10, c))
c = list(map(int,c))
tpc = {1:[c[0],'Plastic'],2:[c[1],'Can'],3:[c[2],'Glass']}
for i in tpc:
    print(i)