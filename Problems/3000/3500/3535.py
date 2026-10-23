'''class'''
def my_st():
    '''class'''
    overall = []
    while True:
        itid = input()
        if itid == 'END':
            break
        overall.append(int(itid))
    overall.sort()
    overall = [str(i)[:4] for i in overall]
    myid = list(set(i[0:4] for i in overall))
    myid.sort()
    for i,ide in enumerate(myid):
        if not i or i and myid[i-1][:2]!=ide[:2]:
            print(ide[:2], int(ide[2:4]), overall.count(ide))
        else:
            print('--', int(ide[2:4]), overall.count(ide))
my_st()
