"""พ่อมดใจแป๋ว?"""
def main():
    """เมนใครครับ?"""
    def item_ ():
        """สารพัดของกุ๊กกิ๊ก"""
        item = input().split(",")
        n_item = len(item)-item.count("")
        return n_item, item
    n, item = item_()
    if not n:
        print("")
    elif n > 6 :
        print("Cauldron Overflow")
    else:
        def c_t (ts_, mbase):
            """นับเลขจ้ะ"""
            if not ts_ :
                mbase = 0
            elif ts_ >= 2 :
                mbase = mbase+mbase//2
            return mbase
        mp = (c_t(item.count("herb"),20)
              +c_t(item.count("slime"),10)
              +c_t(item.count("bone"),30)
              +c_t(item.count("tear"), 50)
              +c_t(item.count("gem"), 100))
        def stir_ ():
            """คนจ้าคน"""
            Ql_ = []
            text_ql= ""
            for _ in range(n):
                ql = input()
                Ql_.append(ql)
            pc_ql = 100
            for q in Ql_:
                match q :
                    case "good":
                        pc_ql -= 10
                    case "bad":
                        pc_ql -=20
            if pc_ql < 0:
                pc_ql = 0
            if Ql_.count("bad") == n :
                text_ql += "Potion Exploded!"
            elif pc_ql == 100 :
                text_ql += "Excellent"
            elif 80 <= pc_ql < 100 :
                text_ql += "Fine"
            elif 50 <= pc_ql < 80 :
                text_ql += "OK"
            else :
                text_ql += "Awful"
            return pc_ql, text_ql
        pr, ql = stir_()

        def mana():
            """มานีเป็นเพื่อนกับมานะ?"""
            rk = ""
            m_ = (mp*pr)//100
            if m_ >= 100:
                rk += "Rank S"
            elif  50 <= m_ < 100:
                rk += "Rank A"
            elif 0 <= m_ < 50:
                rk += "Rank B"
            return rk, m_
        rank, ma_point = mana()
        def success ():
            """pls_pass!"""
            if ql == "Potion Exploded!":
                print("Potion Exploded!")
            elif not ql :
                print("ตั้งใจหน่อยจ้ะ")
            else:
                print("Success!!")
                print(f"{rank}: {ma_point:.0f} (Quality: {ql}, Purity {pr:.0f}%)")
        success ()
main()
