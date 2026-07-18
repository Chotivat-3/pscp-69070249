"""Password"""
def x_1 ():
    """Check!"""
    tes_1 = 0 #lower
    tes_2 = 0 #Upper
    tes_3 = 0 #Num
    p_ = input()
    def lower_ (x):
        """ISlow"""
        for i in x:
            tes = 0
            if i.islower():
                tes += 1
                break
        return tes
    tes_1 += lower_(p_)
    def upper_ (x):
        """ISup"""
        for i in x:
            tes = 0
            if i.isupper():
                tes += 1
                break
        return tes
    tes_2 += upper_(p_)
    def num_ (x):
        """ISnum"""
        for i in x:
            tes = 0
            if i.isdigit():
                tes = 1
                break
        return tes
    tes_3 += num_(p_)
    s_m = tes_1 + tes_2 + tes_3
    match s_m :
        case 1:
            print("Weak..")
        case 2:
            print("Average")
        case 3:
            print("Strong!")
x_1()
