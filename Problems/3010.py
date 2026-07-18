"""Quadrant"""
X = int(input())
Y = int(input())
def qd_ ():
    """Where?"""
    if not X and not Y:
        print('O')
    elif not Y:
        print("X")
    elif not X:
        print("Y")
    elif X > 0 and Y > 0:
        print("Q1")
    elif X < 0 < Y:
        print("Q2")
    elif X < 0 and Y < 0:
        print("Q3")
    elif Y < 0 < X:
        print("Q4")
qd_()
