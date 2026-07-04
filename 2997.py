"""Elo"""
a = int(input())
b = int(input())
type_ = input()
def ea_(x1,x2):
    """Ea"""
    s_a = 1/(1+(10**((x2-x1)/400)))
    s_a = round(s_a,2)
    print(f"{s_a:.2f}")
def eb_(x1,x2):
    """Ea"""
    s_b = 1/(1+(10**((x1-x2)/400)))
    s_b = round(s_b,2)
    print(f"{s_b:.2f}")
match type_:
    case "A":
        ea_(a,b)
    case "B":
        eb_(a,b)
