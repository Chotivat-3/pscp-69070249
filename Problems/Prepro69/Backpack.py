"""สวัสดีฉันชื่อดอร่า"""
def back_pack ():
    """ครับ_กระเป๋าครับ"""
    bp = input().split(",")
    new_item = input()
    n_item = len(bp)
    if n_item > 5:
        while True:
            bp.pop(0)
            n_item -= 1
            if n_item == 5:
                break
    if bp == ["Empty"]:
        bp = []
        n_item = 0
    return bp, new_item, n_item
bp_, new_item_, n_item_ = back_pack()

def pick_pass ():
    """หยิบดีมั้ยน้า"""
    if new_item_ == "Stone":
        print("I don't need this!")
        print(bp_)
    else:
        if n_item_ == 5 :
            bp_.pop(0)
            bp_.append(new_item_)
            print(bp_)
        else :
            bp_.append(new_item_)
            print(bp_)
pick_pass()
