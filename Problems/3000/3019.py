"""Safe like You!"""
PW = "H"
PN = "4567"
def re_check(x1,x2):
    """Check your password"""
    x2 = str(x2)
    if x1+x2 == PW+PN:
        print("safe unlocked")
    elif x1 == PW:
        print("safe locked - change digit")
    elif x2 == PN:
        print("safe locked - change char")
    else:
        print("safe locked")
re_check(input(),int(input()))
