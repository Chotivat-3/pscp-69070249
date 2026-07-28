"""Pass"""

def cal (hw,m,f):
    """cal"""
    key = hw>=5 and m>=20 and f>=25
    if key:
        print("pass")
    else:
        print("fail")
cal(int(input()),int(input()),int(input()))
