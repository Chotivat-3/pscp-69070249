"""IT BOSS"""

key = input()
up = ['  *  ', ' *** ', '* * *', '  *  ', '  *  ']
dw = ['  *  ', '  *  ', '* * *', ' *** ', '  *  ']
lf = ['  *  ', ' *   ', '*****', ' *   ', '  *  ']
rt = ['  *  ', '   * ', '*****', '   * ', '  *  ']

for i in range(5):
    out = ''
    for j in key:
        if j == 'U':
            out += up[i] + ' '
        if j == 'D':
            out += dw[i] + ' '
        if j == 'L':
            out += lf[i] + ' '
        if j == 'R':
            out += rt[i] + ' '
    print(out)
