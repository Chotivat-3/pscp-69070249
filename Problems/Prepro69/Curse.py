"""จ้า"""
def b () :
    """จ้ะ"""
    x = float(input())
    y = float(input())
    s = (input())
    nU = int(s.count("U")) # -y
    nD = int(s.count("D")) # +y
    nL = int(s.count("L")) # +x
    nR = int(s.count("R")) # -x
     
    if nU >= 0 :
        y -= 1*nU
    if nD >= 0 :
        y += 1*nD
    if nL >= 0 :
        x += 1*nL
    if nR >= 0 :
        x -= 1*nR
   
    print(x,y)
b()
