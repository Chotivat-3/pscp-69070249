"""X_SHAPE"""
num, kit = input().split()
num = int(num)

for i in range(num):
    for j in range(num):
        if kit == "#":
            if j in (i,num-1-i):
                print(kit,end='')
            else:
                print('-',end='')
        else:
            if j in (i,num-1-i):
### ตรงนี้ คือ ระยะห่าง ระหว่าง i ถึง จุดกึ่งกลาง เพราะมันจะเพิ่มลด ตาม ตำแหน่ง i
## ที่เปลี่นไป เป็นลูกเล่นที่มองไม่ออก
                print(chr(ord(kit)+abs(i-num//2)),end='')
            else:
                print('-',end='')
    print()
