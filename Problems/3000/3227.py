"""CARD"""
text = input()
tp = {"d":"diamonds","h":"hearts",
      "s":"spades","c":"clubs"}
cl = {"a":"ace","j":"jack","q":"queen","k":"king"}
out =""
if text[0] in "23456789":
    t = text[0]
    c = text[1].lower()
    out += f"{t} of {tp[c]}"
elif text[0] == "1":
    t = text[:2]
    c = text[2].lower()
    out += f"{t} of {tp[c]}"
else :
    t = text[0].lower()
    c = text[1].lower()
    out += f"{cl[t]} of {tp[c]}"
print(out)
