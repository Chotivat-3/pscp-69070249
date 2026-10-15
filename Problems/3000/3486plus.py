'''Bullet'''
def falling():
    '''my bull '''
    n = int(input())
    bullet = [tuple(map(int,input().split())) for _ in range(n)]
    for mx in range(1001):
        for my in range(1001):
            for x, y, d in bullet:
                if (mx-x)**2 + (my-y)**2 != d**2:
                    break
            else :
                return mx, my
print(*falling())
