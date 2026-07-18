"""Buffet"""
def buffet ():
    """I love buffet"""
    x_come = int(input())
    y_push = int(input())
    a_bt = int(input())
    z_come = int(input())
    n_x = z_come//x_come
    n_xx = z_come%x_come
    out = 0
    if x_come >= y_push :
        if z_come >= x_come:
            out += a_bt*((y_push*n_x)+n_xx)
        else:
            out += a_bt*z_come
    else:
        out += a_bt*z_come
    print(out)
buffet()
