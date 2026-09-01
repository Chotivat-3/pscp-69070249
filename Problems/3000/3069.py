"""ZODIAC"""
day = int(input())
month = int(input())
match month :
    case 1 :
        if day in range(0,20):
            print("capricorn")
        else: 
            print("aquarius")
    case 2 :
        if day in range(0,19):
            print("aquarius")
        else: 
            print("pisces")
    case 3 :
        if day in range(0,21):
            print("pisces")
        else: 
            print("aries")
    case 4 :
        if day in range(0,20):
            print("aries")
        else: 
            print("taurus")
    case 5 :
        if day in range(0,21):
            print("taurus")
        else: 
            print("gemini")
    case 6 :
        if day in range(0,22):
            print("gemini")
        else: 
            print("cancer")
