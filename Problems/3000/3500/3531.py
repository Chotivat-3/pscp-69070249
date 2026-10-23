'''Find sm lost guy'''
def who(n):
    '''For What'''
    must_have = set(i for i in range(1,n+1))
    got = set()
    while True:
        g = int(input())
        if not g:
            break
        got.add(g)
    out = []
    for i in must_have.difference(got):
        out.append(i)
    out.sort()
    for i in out:
        print(i)
who(int(input()))
