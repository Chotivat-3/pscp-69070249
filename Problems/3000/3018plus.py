"""RectangleArea"""
pit = input().split(" ")
x1 = int(pit[0])
y1 = int(pit[1])
w1 = int(pit[2])
h1 = int(pit[3])
pit = input().split(" ")
x2 = int(pit[0])
y2 = int(pit[1])
w2 = int(pit[2])
h2 = int(pit[3])
xw1 = x1+w1
yh1 = y1+h1
xw2 = x2+w2
yh2 = y2+h2
def cal ():
    """Cal"""
    xe = min(xw1,xw2)
    xs = max(x1,x2)
    dx = xe - xs
    ye = min(yh1,yh2)
    ys = max(y1,y2)
    dy = ye - ys
    print(dx*dy)
def overlab():
    """overlap or not"""
    key_y = y2<=yh1 and yh2>=y1
    key_x = x2<=xw1 and xw2>=x1
    if key_x and key_y:
        cal()
    else:
        print("no overlapping")
overlab()
