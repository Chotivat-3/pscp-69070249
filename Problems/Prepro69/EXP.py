"""EXP"""
def e() :
    """EXP"""
    lv = int(input())
    exp_left = int(input())
    exp_got = int(input())
    exp = exp_left + exp_got
    st_lv = lv

    while True :
        exp_capacity = (lv/2)*1000
        #exp = exp - exp_capacity
        if exp >= exp_capacity :
            exp -= exp_capacity
            lv += 1
        else :
            break
        #return lv , exp , exp_capacity
    exp_capacity_next = (lv/2)*1000
    st_lv = lv - st_lv
    #exp_capacity = (lv//2)*1000
    #exp = exp - exp_capacity
    print(f"level: {lv}")
    print(f"EXP : {exp:.0f}/{exp_capacity_next:.0f}")
    print(f"Level +{st_lv}")

e()