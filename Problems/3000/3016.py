"""Power_Up"""
def seven(x):
    "seven_up"
    n = x%4
    match n :
        case 0 :
            print(1)
        case 1 :
            print(7)
        case 2 :
            print(9)
        case 3 :
            print(3)
seven(int(input()))
