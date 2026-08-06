"""Castle Boy!"""
def castle(n):
    """castle"""
    # จบที่ชั้นไหน
    end = 0
    while True:
        end += 1
        if end**2 >= n:
            break
    # คำนวณวิธี
    ex = end*2 - 2
    sol = 0
    if not ex:
        return sol
    #กรณี ที่ ชั้น และ ห้อง เป็นเลข ชนิดเดียวกัน วิธีการ จะเท่ากับ ชั้น*2-2
    if end%2 and n%2 or not end%2 and not n%2 :
        sol += ex
    #กรณี ที่ต่างชนิดกัน จะ -1 วิธี
    if end%2 and not n%2 or not end%2 and n%2 :
        sol += ex-1

    return sol
print(castle(int(input())))
