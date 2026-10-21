x = [ 1, 2 ,3 ,4 ]
def xx(y):
    for i in y:
        print(i)
        print(y)
        y.remove(i)
        print(y)
xx(x)