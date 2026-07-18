""" BOOM BOOM BAKUDAN BOOM!"""#บูสก่อนอ่านโจทย์แล้วผมท้อ
def ikea ():
    "ikea ikea?"
    #item1
    nam_1 = str(input())
    p_1 = int(input())
    n_got_1 = int(input())
    red_1 = int(input())
    # item2
    nam_2 = str(input())
    p_2 = int(input())
    n_got_2 = int(input())
    red_2 = int(input())
    n_want =int(input())
    #คำนวณให้ได้เท่าที่ต้องการ?
    nn1 = (n_want+n_got_1-1)//n_got_1
    nn2 = (n_want+n_got_2-1)//n_got_2
    #print(nn1,nn2)
    #price1_2
    p_1 = (p_1*nn1)-(p_1*nn1)*(red_1/100)
    #pr_1 = p_1//n_got_1
    p_2 = (p_2*nn2)-(p_2*nn2)*(red_2/100)
    #pr_2 = p_2//n_got_2
    #n_got
    n_got_1 = n_got_1*nn1
    n_got_2 = n_got_2*nn2
    #PTS POINT
    pts_1 = p_1//10*10
    pts_2 = p_2//10*10
    print(f"{nam_1}: {n_got_1:.0f} - {p_1:.2f} THB. (+{pts_1:.0f} PTS)") # clear
    print(f"{nam_2}: {n_got_2:.0f} - {p_2:.2f} THB. (+{pts_2:.0f} PTS)") # clear
    #แต้มมากกว่าคุ้มกว่า
    #ได้เยอะกว่่าคุ้มกว่า
    #ถูกกว่าคุ้มกว่า
    def order() :
        """ order """
        if pts_1 == pts_2 :
            if n_got_1 > n_got_2 :
                print(f"{nam_1} is better in amount of {n_got_1:.0f}"
                f" with {p_1:.2f} THB and {pts_1:.0f} PTS.")
            elif n_got_2 > n_got_1 :
                print(f"{nam_2} is better in amount of {n_got_2:.0f}"
                f" with {p_2:.2f} THB and {pts_2:.0f} PTS.")
            else :
                print(f"Both {nam_1} and {nam_2} has equal in every condition.")
        elif n_got_1 > n_got_2 :
            print(f"{nam_1} is better in amount of {n_got_1:.0f}"
            f" with {p_1:.2f} THB and {pts_1:.0f} PTS.")
        elif n_got_2 > n_got_1 :
            print(f"{nam_2} is better in amount of {n_got_2:.0f}"
            f" with {p_2:.2f} THB and {pts_2:.0f} PTS.")
        elif n_got_2 == n_got_1 :
            if p_1 <= p_2 :
                print(f"{nam_1} is better in amount of {n_got_1:.0f}"
                f" with {p_1:.2f} THB and {pts_1:.0f} PTS.")
            if p_2 <= p_1 :
                print(f"{nam_2} is better in amount of {n_got_2:.0f}"
                f" with {p_2:.2f} THB and {pts_2:.0f} PTS.")
    order()
ikea()
