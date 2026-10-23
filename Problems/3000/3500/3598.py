'''Tem'''
def tem(n):
    '''tem'''
    mytem = input().split()
    mytem = [float(i) for i in mytem]
    mytem.sort()
    print(f'SUM={sum(mytem):.2f}')
    print(f'AVG={sum(mytem)/n:.2f}')
    med = mytem[n//2] if n%2 else (mytem[n//2]+mytem[n//2-1])/2
    print(f'MEDIAN={med:.2f}')
    print(f'MAX={max(mytem):.2f}')
    print(f'MIN={min(mytem):.2f}')
    alert = [i for i in mytem if i >= 37.00]
    print(f'ALERT={len(alert)}')
    print('SORTED=', end='')
    print(*[f'{i:.2f}' for i in mytem])
tem(int(input()))
