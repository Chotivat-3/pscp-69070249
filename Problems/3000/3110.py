"""สงครามส่งด่ว ปึ้ง!"""
fare = {"BKK CNX":30 ,"CNX UBP":40 ,"UBP BKK":40,
        "BKK PKT":50 ,"PKT CNX":60 ,"UBP PKT":70}

base = {"BKK CNX":10 ,"CNX UBP":15 ,"UBP BKK":20,
        "BKK PKT":25 ,"PKT CNX":30 ,"UBP PKT":40}

key = fare.keys()
key_in = input()
w = float(input())
out = 0

if key_in not in key:
    out = "Error"
else:
    out += w*fare[key_in]+base[key_in]
    out = f"{out:.2f}"

print(out)
