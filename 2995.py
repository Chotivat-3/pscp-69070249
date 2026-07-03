"""ตรวจสอบบัตรนศ."""
def x(x_):
    """ตรวจสอบ"""
    n = len(x_)
    a = x_[2]
    b = x_[3]
    if n == 8 :
        if a == "1" and b == "6":
            print("yes")
        else:
            print("no")
    else:
        print("no")
x(x_=input())
