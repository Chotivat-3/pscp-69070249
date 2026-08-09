"""Milk"""
P = float(input())
CP = int(input())
S = int(input())
M = float(input())

def milk (p=P,cp=CP,s=S,m=M):
    """milk"""

    n_bot = m//p
    n_cp = n_bot

    if not cp:
        print(f"{n_bot:.0f}")
    else:
        n_total =  0
        n_total += n_bot
        while n_cp >= cp :
            ## loop นี้อะ ต้องการ วน จนกว่า ขวดใหม่ที่ได้จะ น้อยกว่าฝาที่เอาไปแลกโปร แถม
            n_newbot = (n_cp//cp)*s
            ## คือ ฝาขวด จะยังเหลือ คือเศษ ที่เหลือจากครั้งที่แล้ว + ด้วย ฝาใหม่ที่ได้
            n_cp -= n_cp - (n_cp%cp + n_newbot)
            n_total += n_newbot

        print(f"{n_total:.0f}")
milk()
