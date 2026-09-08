"""Real THAI"""
def myreal():
    """REAL"""

    money = int(input())
    day = int(input())
    thiplus = 1000
    thi=thiplus
    n = 0

    while day :
        k = int(input())

        if thiplus >= 200:
            maxday = 200
        else :
            maxday = thiplus

        while k:
            price = int(input())
            if price >= 333:
                rat = 200
                if money < price - 200:
                    k -= 1
                    continue
            else:
                rat = price - (price*40)//100
            if maxday >= rat :
                maxday -= rat
                if money >= price - rat:
                    money -= price - rat
                    thiplus -= rat
                    n += 1
            elif 0 < maxday <= rat:
                if money >= price - maxday:
                    money -= price - maxday
                    thiplus -= maxday
                    maxday = 0
                    n += 1
            elif money >= price:
                money -= price
                n += 1
            k -= 1
        day -= 1

    print(n)
    print(money)
    print(thi-thiplus)
myreal()
