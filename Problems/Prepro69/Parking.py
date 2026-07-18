"""PARKING"""
def x() :
    """PARKING"""
    type_ = str(input()).lower()
    type_time = str(input()).lower()
    t_1 = int(input())
    t_2 = int(input())
    def a() :
        """allowed?"""
        if type_ == "vip" :
            print("Parking allowed")
        elif type_ == "regular" :
            if type_time == "weekday" and  6 <= t_1 <= t_2 <= 22 : # 6 <= t_1 <= t_2 <= 22
                print("Parking allowed")
            else :
                print("Parking not allowed")
        elif type_ == "visitor" :
            if type_time == "weekend" and 9 <= t_1 <= t_2 <= 18 :# 9 <= t_1 <= t_2 <= 18
                print("Parking allowed")
            else :
                print("Parking not allowed")
        else :
            print("Membership is invalid")
    a()
x()
