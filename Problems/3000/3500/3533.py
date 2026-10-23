'''Holi'''
def memo(t):
    '''Holi'''
    mynor = []
    myup = []
    myout = []
    myset = set(i for i in t)
    for i in myset:
        if i.islower():
            mynor.append([i,t.count(i)])
        else :
            myup.append([i,t.count(i)])
    myup.sort()
    mynor.sort()
    myout = mynor+myup
    for i in myout:
        num = i[1]
        if  num <= 5:
            i[1] = ['-'*num]
        else:
            main = num//5
            remain = num%5
            i[1] = ['-'*5+'|' for i in range(main)]
            if remain :
                i[1] += ['-'*remain]
            else :
                i[1][main-1] = '-'*5
    for i in myout:
        print(f'{i[0]} : {''.join(i[1])}')
memo(input())
