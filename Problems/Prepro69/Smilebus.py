"""ซูเปอร์ สไมล์ บัส"""
def x() :
    """ซูเปอร์ สไมล์ บัส"""
    r = int(input())#รอบ(ไม่เกิน5)
    hop = str(input())#HOP CARD
    ag = int(input())#age
    total = 0
    if r >= 1 :
        d = float(input())
        s = int(input())
        ep = int(input())
        pm =d*(ep-s)
        if 0 < pm < 6 :
            pm = 15
        elif 6 <= pm < 18 :
            pm = 20
        else :
            pm = 25
        total = total + pm
    if r >= 2 :
        d = float(input())
        s = int(input())
        ep = int(input())
        pm =d*(ep-s)
        if 0 < pm < 6 :
            pm = 15
        elif 6 <= pm < 18 :
            pm = 20
        else :
            pm = 25
        total = total + pm
    if r >= 3 :
        d = float(input())
        s = int(input())
        ep = int(input())
        pm =d*(ep-s)
        if 0 < pm < 6 :
            pm = 15
        elif 6 <= pm < 18 :
            pm = 20
        else :
            pm = 25
        total = total + pm
    if r >= 4 :
        d = float(input())
        s = int(input())
        ep = int(input())
        pm =d*(ep-s)
        if 0 < pm < 6 :
            pm = 15
        elif 6 <= pm < 18 :
            pm = 20
        else :
            pm = 25
        total = total + pm
    if r >= 5 :
        d = float(input())
        s = int(input())
        ep = int(input())
        pm =d*(ep-s)
        if 0 < pm < 6 :
            pm = 15
        elif 6 <= pm < 18 :
            pm = 20
        else :
            pm = 25
        total = total + pm
    if ag <= 12:
        print("Payment: FREE")
        return
    if ag > 12 and hop == "yes" :
        if total >= 40 :
            print("Payment: 40 THB")
            print("Max Fare Reached")
        elif total < 40 :
            print(f"Payment: {total} THB")
    elif ag > 12 and hop != "yes" :
        print(f"Payment: {total} THB")
x()
