'''SUMSUM'''
def overall():
    '''sumall'''
    out = 0
    wanted = int(input())
    while True:
        x = int(input())
        if x < 0:
            break
        out += x
        if out == wanted:
            return out
    return out
print(overall())
