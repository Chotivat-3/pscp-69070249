"""Safe lock"""
text = input()
digit = int(input())
if text == "H" and digit == 4567:
    print("safe unlocked")
elif text == "H":
    print("safe locked - change digit")
elif digit == 4567:
    print("safe locked - change char")
else:
    print("safe locked")
