'''how many'''

def person():
    '''อ้ายมากี่คน'''
    p = [0, 0, 0]
    while True:
        hot_id = input()
        if not hot_id[0].isdigit():
            return p
        if hot_id[-1] in '13579':
            p[0] += 1
        else:
            p[1] += 1
        p[2] += 1
print(*person())
