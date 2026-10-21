'''bakata'''

def baka(n):
    '''bakata'''
    out = []
    for _ in range(n):
        key = True
        text = input()
        run = 0
        if 'baka' in text:
            key = False
        else:
            while run < len(text):
                if text[run:run+5] == 'bakka':
                    run += 5
                elif text[run:run+2] in ('ba', 'ka', 'ta'):
                    run += 2
                else:
                    key = False
                    break
        if key:
            out.append('yes')
        else:
            out.append('no')
    return out
for bakata in baka(int(input())):
    print(bakata)
