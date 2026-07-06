"""Color"""
cm = ["Red","Yellow","Blue"]
c1 = input()
c2 = input()
def col(c_1,c_2):
    """C_Luv"""
    if c_1 == c_2 :
        if c_1 == cm[0] or c_2 == cm[0]:
            print(cm[0])
        elif c_1 == cm[1] or c_2 == cm[1]:
            print(cm[1])
        elif c_1 == cm[2] or c_2 == cm[2]:
            print(cm[2])
        else:
            print("Error")
    elif c_1 == cm[0] and c_2 == cm[1] or c_1 == cm[1] and c_2 == cm[0]:
        print("Orange")
    elif c_1 == cm[0] and c_2 == cm[2] or c_1 == cm[2] and c_2 == cm[0]:
        print("Violet")
    elif c_1 == cm[1] and c_2 == cm[2] or c_1 == cm[2] and c_2 == cm[1]:
        print("Green")
    else:
        print("Error")
col(c1,c2)
