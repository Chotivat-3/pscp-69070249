"""ZODIAC"""
day = int(input())
month = int(input())-1#เพื่อเรียกใน list
day_rge = [range(0,20),range(0,19),range(0,21)
           ,range(0,20),range(0,21),range(0,22)
           ,range(0,23),range(0,23),range(0,23)
           ,range(0,24),range(0,22),range(0,22)
           ]
zodiac = {1:"capricorn",2:"aquarius",3:"pisces",4:"aries"
           ,5:"taurus",6:"gemini",7:"cancer",8:"leo",9:"virgo",
           10:"libra",11:"scorpio",12:"sagittarius"
           }
if day in day_rge[month]:
    month += 1#เพื่อใช้ key
    print(zodiac[month])
else:
    month += 2 #เพื่อเลื่อน key
    if month >= 13:
        month = 1
    print(zodiac[month])
