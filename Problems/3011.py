"""Colors"""
c = []
c.append(input())
c.append(input())
c1 = c[0]
c2 = c[1]
def c_ (x1,x2):
    """Colors"""
    for i in c :
        if i != "Red" or i != "Yellow" or i != "Blue":
            color = "Error" 
            break
    if x1 == x2 :
        color  = f"{x1}"
    if color != "Error":
        match x1:
            case "Red":
                if x2 == "Yellow":
                    color  = "Orange"
                else:
                    color  = "Violet"
            case "Yellow":
                if x2 == "Red":
                    color  = "Orange"
                else:
                    color  = "Green"
            case "Blue":
                if x2 == "Red":
                    color  = "Violet"
                else:
                    color  = "Green"
    return color
color = c_(c1,c2)
print(color)
