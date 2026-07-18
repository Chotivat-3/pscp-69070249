"""Bunny Shopping"""
item = input()
item = item.split(" ")
carrot = int(item[0])
cabbage = int(item[1])
tomato = int(item[2])
def cal (i1=carrot,i2=cabbage,i3=tomato):
    """How much"""
    total = i1*10 + i2*25 + i3*3
    print(total)
cal()
