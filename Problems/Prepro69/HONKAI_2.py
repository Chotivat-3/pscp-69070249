"""Honkai"""
def h ():
    """Honkai ขยันออกโจทย์มากกั๊บ"""
    name = input()
    a = int(input()) #Crystal
    b = int(input()) #Char
    c = int(input()) #Equip
    total = 0
    semi = 0
    aa = a/280
    uaa = aa//10*10
    bb = 0
    cc = 0
    roll = aa + b + c
    if a < 0 or b < 0 or c < 0  :
        return
    print(f"Current Rolls = {roll:.0f}")

    def spin () :
        """จุ่มลุ้นโชค"""
        if uaa >= 330 :
            print(f"Enough for Full \"{name}\" Set, Goodluck! :)")
            return
        if b >= 90 and c >= 240 :
            print(f"Enough for Full \"{name}\" Set, Goodluck! :)")
            return
        if b < 90 :
            if c < 240 :
                bb = 90 - b
                cc = 240 - c
                #ubb = bb//10*10
                #ucc = cc//10*10
                semi = bb + cc #โรลขาด
                total = (semi - aa)*280
                if total <= 0 :
                    print(f"Enough for Full \"{name}\" Set, Goodluck! :)")
                else:
                    print(f"Crystal to Collect for \"{name}\" = {total:.0f}")
            elif c >= 240 :
                bb = 90 - b
                #cc = 240 - c
                #ubb = bb//10*10
                #ucc = cc//10*10
                semi = bb #โรลขาด
                total = (semi - aa)*280
                if total <= 0 :
                    print(f"Enough for Full \"{name}\" Set, Goodluck! :)")
                else:
                    print(f"Crystal to Collect for \"{name}\" = {total:.0f}")
                
        if b >= 90 :
            if c < 240 :
                #bb = 90 - b
                cc = 240 - c
                #ubb = bb//10*10
                #ucc = cc//10*10
                semi = cc #โรลขาด
                total = (semi - aa)*280
                if total <= 0 :
                    print(f"Enough for Full \"{name}\" Set, Goodluck! :)")
                else:
                    print(f"Crystal to Collect for \"{name}\" = {total:.0f}")
            elif c >= 240 :
                print(f"Enough for Full \"{name}\" Set, Goodluck! :)")

    spin ()
h()