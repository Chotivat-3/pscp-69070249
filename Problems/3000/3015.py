"""Buffet"""
x = int(input())
y = int(input())
a = int(input())
z = int(input())
def cal_buffet(come,call,bth,in_buff):
    """What a deal"""
    out = 0
    n = in_buff//call
    if in_buff >= come :
        if come >= call :
            out += bth*call*n
        else :
            out += bth*in_buff
    else :
        out += bth*in_buff
    print(f"{out:.0f}")
cal_buffet(x,y,a,z)
