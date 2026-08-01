"""PASSWORD"""
text = input()
n_text = len(text)
title = text[0].upper()
last = text[-1].upper()
#      1 2 3 4 5 6 7 8 9 10
num = [0,1,2,3,4,5,6,7,8,9]
key1 = ord(title)
key2 = ord(last)
for i in range(1,11):
    if i%2:
        key1+=num[i-1]
        num[i-1] = key1
    else:
        key2-=num[i-1]
        num[i-1] = key2
    key1 = ord(title)
    key2 = ord(last)
for i in range(10):
    num[i] = num[i]%n_text
    if num[i] > 9:
        num[i] = num[i]%10

num = list(map(str,num))
print(" ".join(num[2:8]))
