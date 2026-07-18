"""Chant_t!!!"""
def main():
    """เมนเทอเมน"""
    def p_1(p1):
        """person1"""
        x1 = p1.lower()
        pt_1 = 0
        for i in x1:
            if i == "a":
                pt_1+=1
            if i == "e":
                pt_1+=1
            if i == "i":
                pt_1+=1
            if i == "o":
                pt_1+=1
            if i == "u":
                pt_1+=1
        return p1.upper(),pt_1
    def p_2(p2):
        """person1"""
        x2 = p2.lower
        pt_2 = 0
        for i in x2():
            if i == "a":
                pt_2+=1
            if i == "e":
                pt_2+=1
            if i == "i":
                pt_2+=1
            if i == "o":
                pt_2+=1
            if i == "u":
                pt_2+=1
        return p2.upper(),pt_2
    p1_,pt1 = p_1(input())
    p2_,pt2 = p_2(input())
    if pt1 == pt2 :
        print("Draw! The skill have dispel each others!")
    elif pt1 > pt2 :
        print(f"{p1_}!!!")
        print("Player 1 Wins!")
    else:
        print(f"{p2_}!!!")
        print("Player 2 Wins!")
main()
