"""PM"""
N = int(input())
over = 0
PEAK = 0
STREAK = ""
START = 0

x = int(input())
PEAK = x
if x > 50 :
    STREAK += "1"
    over += 1
else:
    STREAK += "0"
N -= 1

while N :
    x = int(input())
    if x > PEAK :
        PEAK = x
    if x > 50:
        STREAK += "1"
        over += 1
    else:
        STREAK += "0"
    N -= 1

def out_st(st = STREAK):
    """STREAK OUT"""
    lim = len(st)
    num = 0
    start = 0
    o_max = 0
    if st.find("1") != -1:
        start = st.find("1")
        o_first = 0
        for i in range(0,lim):
            num += 1
            if st[i] == "1":
                o_first += 1
            else :
                o_max = o_first
                o_first = 0
                break
        print(num, o_first)
        if num != lim:
            for i in range(num,lim):
                if st[i] == "1":
                    o_first += 1
                else :
                    if o_first >= o_max:
                        o_max = o_first
                        start = i - (o_first-1)
                    o_first = 0
        if o_first:
            o_max = o_first
            start = lim - num +1
    return o_max, start
streak_out, START = out_st()

print(f"OVER = {over}")
print(f"PEAK = {PEAK}")
print(f"STREAK = {streak_out}")
print(f"START = {START}")
