"""Slayer quest!!"""
def slayer_xp(n):
    """EXP"""
    slayx_=0
    for _ in range (n):
        x1 = input()
        match x1 :
            case "I":
                slayx_ += 5
            case "II":
                slayx_ += 25
            case "III":
                slayx_ += 100
            case "IV":
                slayx_ += 500
    return slayx_,n
x_, n_ =slayer_xp(int(input()))
def calculate_level(x,n):
    """LV"""
    lv_ = 1
    Title = ""
    if 0 <= x < 100 :
        Title = "Noob"
    elif 100 <= x < 300 :
        lv_ = 2
        Title = "Novice"
    elif 300 <= x < 600 :
        lv_ = 3
        Title = "Skilled"
    elif 600 <= x < 1000 :
        lv_ = 4
        Title = "Destroyer"
    elif 1000 <= x < 1500 :
        lv_ = 5
        Title = "Bulldozer"
    elif 1500 <= x < 2500 :
        lv_ = 6
        Title = "Savage"
    elif 2500 <= x < 4000 :
        lv_ = 7
        Title = "Deathripper"
    elif 4000 <= x < 6000 :
        lv_ = 8
        Title = "Necromancer"
    elif  x >= 6000 :
        lv_ = 9
        Title = "Grim Reaper"
    for _ in range(n):
        print("Quest Completed")
    print(f"Total Slayer Quest: {n}")
    print(f"Total Slayer EXP: {x}")
    print(f"Total Slayer Level: {lv_}")
    print(f"Title: {Title}")
calculate_level(x_, n_)
