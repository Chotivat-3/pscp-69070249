"""Surprise Vote"""
al = float(input())
mx = float(input())
num = (3*mx)-2
if  mx < 10 :
    if mx <= 2 :
        print("Not surprising")
    elif al < num :
        print("Surprising")
    else :
        print("Not surprising")
elif al <= num :
    print("Surprising")
else :
    print("Not surprising")
