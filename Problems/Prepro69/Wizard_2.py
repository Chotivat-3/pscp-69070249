"""พ่อมดใจแป๋ว?"""
def main():
    """เมนใครครับ?"""
    def item_ ():
        """สารพัดของกุ๊กกิ๊ก"""
        item = input().split(",")
        n_item = len(item)
        return n_item, item
    n, item = item_()
    if n > 6 :
        print("Cauldron Overflow")
    else:
        def c_t ():
            """นับเลขจ้ะ"""
            hn = item.count("herb")
            sn = item.count("slime")
            bn = item.count("bone")
            tn = item.count("tear")
            gn = item.count("gem")
            ct_ = {}
            ct_[hn]=20
            ct_[sn]=10
            ct_[bn]=30
            ct_[tn]=50
            ct_[gn]=100
            for i,j in ct_.items():
                if not i:
                    ct_[i] = 0
                if i >=2:
                    ct_[i] =  j*1.5
            mp = sum(ct_.values())
            return mp
        mp = c_t()
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
                text_ql += "Ok"
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
            else:
                print("Success!!")
                print(f"{rank}: {ma_point:.0f} (Quality: {ql}, Purity {pr}%)")
        success ()
main()
