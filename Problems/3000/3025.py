"""Bad_Season!"""
SS_ = {1:"winter" ,2:"winter" ,3:"winter"
       ,4:"spring" ,5:"spring" ,6:"spring"
       ,7:"summer" ,8:"summer" ,9:"summer"
       ,10:"fall" ,11:"fall" ,12:"fall"
       }
M = int(input())
D = int(input())
def what_season(m=M,d=D):
    """Season"""
    divi_3 = [3,6,9,12]
    if m in divi_3 :
        if d >= 21:
            m += 1
            if m == 13:
                m = 1
    print(SS_[m])
what_season()
