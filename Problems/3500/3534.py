'''Filter'''
from json import loads
def fer(forall, fil):
    '''filter'''
    my_point = loads(forall)
    myout = []
    for i in list(my_point.keys()):
        if int(float(my_point[i])*100) >= int(fil*100):
            myout.append(i)
    myout = [int(i) for i in myout]
    myout.sort()
    myout = [str(i) for i in myout]
    if not myout:
        print('Nope')
        return
    for i in myout:
        print(f"{i}	{float(my_point[i]):.2f}")
fer(input(), float(input()))
