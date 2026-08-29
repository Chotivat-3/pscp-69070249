"""TICKET BOY"""

def ticket(n):
    """TICKET"""
    tick = n
    while tick:
        price = 0
        try:
            a, t = map(int,input().split())
            if a >= 15:
                tick -= t
                if a <= 22:
                    price += t*(120)
                elif a >= 60:
                    price += t*(75)
                else:
                    price += t*(150)
                if tick < 0:
                    print(-2)
                    tick += t
                else:
                    print(f"{price} {tick}")
            else:
                print(-1)
        except EOFError:
            break
ticket(int(input()))
