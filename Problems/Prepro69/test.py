text = input()

word = ""
first = True

for ch in text:
    if ch == " ":
        if len(word) >= 4:
            word = word[::-1]

        if not first:
            print(" ", end="")
        print(word, end="")

        first = False
        word = ""
    else:
        word += ch

# จัดการคำสุดท้าย
if len(word) >= 4:
    word = word[::-1]

if not first:
    print(" ", end="")
print(word, end="")