"""BrickBridge"""

A = int(input())#mini
B = int(input())#big
G = int(input())#goal

def cal (a=A,b=B,g=G):
    """cal"""
    n_b = g//5
    n_b = min(n_b,b)
    n_a = g - n_b*5
    key = n_a - a
    if key <= 0 :
        print(n_a)
    else:
        print(-1)
cal()
