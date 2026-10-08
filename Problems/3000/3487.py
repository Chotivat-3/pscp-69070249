'''ligt Up!!'''
def light(n):
    '''light like boy เป็นแบบนี้ก็ บ้อย บ่อย ห้ะ'''
    my_pole = []
    for _ in range(n):
        my_pole.append(int(input()))
    my_pole.sort()
    out_pole = []
    for i in range(n):
        out_pole.append(sum(my_pole[:i+1]))
    out = sum(out_pole)*2
    return out
print(light(int(input())))
