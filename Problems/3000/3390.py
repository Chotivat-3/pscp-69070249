'''array'''
m1, m2 = (map(int,input().split())), map(int,input().split())
m3, m4, m5 = map(int,input().split()), map(int,input().split()),  map(int,input().split())
matrix = list(m1), list(m2), list(m3), list(m4), list(m5)
out = '-1 -1'
for i in range(5):
    for j in range(5):
        if matrix[i][j]%2:
            out = f"{i} {j}"
print(out)
