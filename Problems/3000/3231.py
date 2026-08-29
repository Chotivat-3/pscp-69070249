"""DICE!!"""
g = input()
r = input()

if g not in "123456" or r not in "123456":
    print("Invalid")
elif g == r:
    print("Correct!")
else:
    print("Wrong!")
