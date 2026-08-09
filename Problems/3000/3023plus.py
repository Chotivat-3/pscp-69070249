"""Cal!!"""
text_num = input()
n_num = len(text_num)
num = int(text_num)
out = 0

if n_num == 1 :
    out = num * 2
    if num == 1:
        out = 1
else:
    out = 0
    num_check = 10**(n_num-1)
    num_check = num - num_check +1

### แพทเทริน การเพิ่ม 9*1 90*2 900*3 9000*4 ...
    for i in range(1,n_num):### คือ ให้*=เลขชี้กำลัง
        out += (9*10**(n_num-(i+1)))*(n_num-i)

###  จำนวน +,= |  จำนวนหลัก*จำนวนเลขในหลักท้าย
    out += num + n_num*num_check

print(out)
