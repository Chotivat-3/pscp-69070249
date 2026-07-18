"""Wizard"""
def wz ():
    """Wizard"""
    item = input().split(",")
    n = len(item)
    sk = []
    rank = ""
    if n > 6 :
        print("Cauldron Overflow")
    else:
        for _ in range (n):
            sk.append(input())
        if sk.count("bad") == n:
            print("Potion Exploded!")
        else:
            pr = 100
            for i in sk:
                match i :
                    case "good":
                        pr -= 10
                    case "bad":
                        pr -=20
            hn = item.count("herb")*20
            sn = item.count("slime")*10
            bn = item.count("bone")*30
            tn = item.count("tear")*50
            gn = item.count("gem")*100
            if hn//20 >= 2 :
                hn = 30
            if sn//10 >= 2 :
                sn = 15
            if bn//30 >= 2 :
                bn = 45
            if tn//50 >= 2 :
                tn = 75
            if gn//100 >= 2 :
                gn = 150
            mp = hn+sn+bn+tn+gn
            pr_=""
            if pr < 0:
                pr = 0
            mp = mp*pr//100
            if pr == 100:
                pr_+=f"(Quality: Excellent, Purity {pr:.0f}%)"
            elif 80 <= pr < 100:
                pr_+=f"(Quality: Fine, Purity {pr:.0f}%)"
            elif 50 <= pr < 80:
                pr_+=f"(Quality: OK, Purity {pr:.0f}%)"
            else:
                pr_+=f"(Quality: Awful, Purity {pr:.0f}%)"
            if mp >= 100:
                rank += "s"
            elif 50 <= mp < 100:
                rank += "A"
            else :
                rank += "B"
            print("Success!!")
            print(f"Rank {rank}: {mp} {pr_} ")
wz()
