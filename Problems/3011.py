"""Colors"""
def c_ (x1,x2):
    """Colors"""
    match x1:
        case "Red":
            match x2 :
                case "Red":
                    color = f"{x1}"
                case "Yellow":
                    color  = "Orange"
                case "Blue":
                    color  = "Violet"
                case _ :
                    color = "Error"
        case "Yellow":
            match x2 :
                case "Yellow":
                    color = f"{x1}"
                case "Red":
                    color  = "Orange"
                case "Blue":
                    color  = "Green"
                case _ :
                    color = "Error"
        case "Blue":
            match x2 :
                case "Blue":
                    color = f"{x1}"
                case "Red":
                    color  = "Violet"
                case "Yellow":
                    color  = "Green"
                case _ :
                    color = "Error"
        case _:
            color = "Error"
    print(color)
c_(input(),input())
#40min