'''Histrogram'''
MYTEXT = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
text = input()
t = [0]*52

for i, alpa in enumerate(MYTEXT):
    t[i]=text.count(alpa)

for i, num in enumerate(t):
    if num:
        print(f"{MYTEXT[i]} = {num}")
