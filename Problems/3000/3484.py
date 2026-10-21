'''Robot MANOCH'''

def robot():
    '''robot boy'''
    n, p = map(int,input().split())
    t = []
    wrongy, totaly = [0]*n, [0]*n
    for _ in range(n):
        t.append(list(map(int,input().split())))
    for i in t:
        print(' '.join(list(map(str,i))),end=' ')
        wrongx, totalx = 0, 0
        for j, wrong in enumerate(i) :
            if wrong:
                wrongx += 1
                totalx += wrong
                wrongy[j] += 1
                totaly[j] += wrong
        print(wrongx, totalx)
    print(' '.join(list(map(str,wrongy))))
    print(' '.join(list(map(str,totaly))))
    print(sum(wrongy), sum(totaly), f"{p*sum(totaly):.2f}")
robot()
