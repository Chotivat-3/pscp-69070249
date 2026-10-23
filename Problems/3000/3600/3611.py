'''coffee shop'''
item = [float(input()) for _ in range(4)]
n_cof = int(input())

def pone(price,per, n):
    '''one'''
    return price+(n-1)*price*((100-per)/100)

def ptwo(price, per, mnprice, n) :
    '''two'''
    if price*n >= mnprice:
        return price*n*((100-per)/100)
    return price*n

def coffee (one,two):
    '''what i Choose'''
    if one<two:
        return [1, one]
    return [2, two]

out = coffee(pone(item[0],item[1], n_cof),ptwo(item[0], item[2], item[3], n_cof))
print(out[0])
print(f'{out[1]:.2f}')
