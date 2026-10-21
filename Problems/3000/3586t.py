'''bakata'''

def baka(n):
    '''bakata'''
    for _ in range(n):
        key = True
        text = input()
        mytext = text.split('a')
        print(mytext)
        for i, t in enumerate(mytext):
            if t not in ('b','k','t','kk','') :
                key = False
            if t == 'kk' and not i or t == 'kk' and i and mytext[i-1] != 'b' :
                key = False
            if t == 'k' and i and mytext[i-1] == 'b':
                key = False
        if key:
            print('yes')
        else:
            print('no')

baka(int(input()))
