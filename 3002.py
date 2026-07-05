"""Cyan_Who?"""
def password(x1,x2,x3):
    """passTT"""
    n1 = len(x1)
    n2 = len(x2)
    if n1 >= 5 and n2 >= 5 :
        print(f"{x1[:2]}{x2[-1]}{x3[-1]}")
    else:
        print(f"{x1[0]}{x3}{x2[-1]}")
password(input(),input(),input())
