"""CODE"""
t = input()
n = len(t)
out = ''
let = 0
dig = 0
for i in range(n):
    if t[i].isalpha():
        out+=t[i].upper()
        let+=1
    elif t[i].isdigit():
        out+=t[i]
        dig+=1
    elif i and t[i-1].isalnum():
        out+='-'
if out:
    print(f"CODE = {out.strip('-')}")
else:
    print("CODE = NONE")
print(f"LETTERS = {let}")
print(f"DIGITS = {dig}")
