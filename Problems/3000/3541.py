'''Coke V2'''
def coke(a, b, c, d):#a-price b-promo c-newprice d-want
    '''coke zero'''
    if not b or not d :
        return a*d
    # one 10 10 10 7 | two 10 10 7 10 10 7  a10 b3 c7 d10
    part1 = a*b + c
    part2 = ((d - b - 1)//b)*(part1-a) + ((d - b - 1)%b)*a
    return part1 + part2
print(coke(int(input()),int(input()),int(input()),int(input())))
