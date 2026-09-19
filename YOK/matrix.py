'''matrix'''

n = int(input())
x = int(input())
y = int(input())
out = ''

for i in range(n):

    for j in range(n):
        out += f"({i},{j})"
        if j != n-1:
            out += " "
        if i == x and j == y:
            break
    if i != n-1:
        out += '\n'
    if f'({x},{y})' in out:
        break

print(out)
