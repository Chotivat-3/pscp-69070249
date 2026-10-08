'''Nood'''
price, paid = int(input()), int(input())
if price == paid :
    print('Good!')
elif price > paid :
    print('Need more cash!')
else:
    print(paid - price)
