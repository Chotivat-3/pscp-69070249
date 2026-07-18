"""Bill"""
expenses = int(input())
def cal_bill (ex):
    """What_bill?"""
    w_m = 0
    if ex >= 10000:
        w_m += 1000
    else:
        w_m += ex*(10/100)
        if w_m < 50 :
            w_m = 50
    vat = (ex + w_m)*(7/100)
    overall = ex + w_m + vat
    overall = round(overall,2)
    print(f"{overall:.2f}")
cal_bill(expenses)
